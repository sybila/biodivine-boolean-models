use biodivine_lib_param_bn::symbolic_async_graph::SymbolicAsyncGraph;
use biodivine_lib_param_bn::{BooleanNetwork, FnUpdate, RegulatoryGraph, VariableId};
use regex::Regex;
use std::convert::TryFrom;
use std::path::Path;
use std::process::exit;

fn main() {
    let arguments = std::env::args().collect::<Vec<_>>();
    let check = arguments.len() > 1 && arguments[1] == "--check";

    let root = std::env::current_dir().unwrap();
    let sources_dir = root.join("sources");
    let models_dir = root.join("models");

    if !sources_dir.exists() {
        eprintln!("Missing sources directory.");
        exit(128);
    }

    if !models_dir.exists() {
        eprintln!("Group does not contain a models directory.");
        exit(128);
    }

    let source_dir_regex = Regex::new(r"(\d+)_([A-Z0-9-]+)").unwrap();

    for source in std::fs::read_dir(sources_dir).unwrap() {
        let source = source.unwrap();
        let name = source.file_name().to_str().unwrap().to_string();
        if name.starts_with(".") {
            // Skip dot-files
            continue;
        }
        let (id, name) = if let Some(matched) = source_dir_regex.captures(name.as_str()) {
            (matched[1].to_string(), matched[2].to_string())
        } else {
            eprintln!(
                "Unrecognized file/directory in sources directory: {}.",
                name
            );
            eprintln!("Note that a model directory must be ID_NAME where:");
            eprintln!(" - ID is a number.");
            eprintln!(
                " - NAME is a non-empty name containing uppercase letters, numbers, and dashes."
            );
            exit(128);
        };

        println!("Synchronization of model {} (ID {}) ...", name, id);

        let model_url = read_source_url(&source.path());
        println!(" - model source: `{}`", model_url);

        let network = read_source_model(&source.path());
        // A quick pass to ensure that parameters are represented without identity regulations.
        let network = normalize_parameters(network);
        check_consistency(&network, &source.path());

        println!(" - model file exists and is consistent.");

        let benchmark_name = format!("[var:{}]__[id:{}]__[{}]", network.num_vars(), id, name);
        let output_dir = models_dir.join(benchmark_name);
        std::fs::create_dir_all(output_dir.clone()).unwrap();

        if check {
            check_metadata(&network, model_url.as_str(), &output_dir);
            println!(" - metadata consistent.");
        } else {
            write_metadata(&network, model_url.as_str(), &output_dir);
            println!(" - metadata written.");
        }

        if check {
            check_network(&network, &output_dir, "model");
            println!(" - direct translation checked.");
        } else {
            write_network(&network, &output_dir, "model");
            println!(" - direct translation created.");
        }

        if !network_inputs(&network).is_empty() {
            if check {
                check_network(
                    &fix_network_inputs(&network, true),
                    &output_dir,
                    "model_inputs_true",
                );
                check_network(
                    &fix_network_inputs(&network, false),
                    &output_dir,
                    "model_inputs_false",
                );
                check_network(
                    &free_network_inputs(&network),
                    &output_dir,
                    "model_inputs_free",
                );
                println!(
                    " - model has {} inputs, input specific translations checked.",
                    network_inputs(&network).len()
                );
            } else {
                write_network(
                    &fix_network_inputs(&network, true),
                    &output_dir,
                    "model_inputs_true",
                );
                write_network(
                    &fix_network_inputs(&network, false),
                    &output_dir,
                    "model_inputs_false",
                );
                write_network(
                    &free_network_inputs(&network),
                    &output_dir,
                    "model_inputs_free",
                );
                println!(
                    " - model has {} inputs, input specific translations created.",
                    network_inputs(&network).len()
                );
            }
        } else {
            println!(" - model has no inputs.");
        }
    }

    println!("DONE!");
}

/// Read a model from the source directory as a Boolean network.
fn read_source_model(source_dir: &Path) -> BooleanNetwork {
    if source_dir.join("source.sbml").exists() {
        let file = std::fs::read_to_string(source_dir.join("source.sbml")).unwrap();
        BooleanNetwork::try_from_sbml(file.as_str()).unwrap().0
    } else if source_dir.join("source.bnet").exists() {
        let file = std::fs::read_to_string(source_dir.join("source.bnet")).unwrap();
        BooleanNetwork::try_from_bnet(file.as_str()).unwrap()
    } else if source_dir.join("source.aeon").exists() {
        let file = std::fs::read_to_string(source_dir.join("source.aeon")).unwrap();
        BooleanNetwork::try_from(file.as_str()).unwrap()
    } else {
        eprintln!(
            "No source model (.sbml/.aeon/.bnet) found in {}.",
            source_dir.display()
        );
        exit(128);
    }
}

/// Read a source url of a particular model.
fn read_source_url(source_dir: &Path) -> String {
    let file = source_dir.join("url.txt");
    if !file.exists() {
        eprintln!("No url.txt file found in {}.", source_dir.display());
        exit(128);
    }
    let url = std::fs::read_to_string(file).unwrap();
    if url.is_empty() {
        eprintln!("Empty source url in {}.", source_dir.display());
        exit(128);
    }

    url
}

/// Write the given network as sbml, bnet and aeon to the given path with the given base "name".
fn write_network(network: &BooleanNetwork, path: &Path, name: &str) {
    let path = path.join(name);
    std::fs::write(path.with_extension("sbml"), network.to_sbml(None)).unwrap();
    std::fs::write(path.with_extension("bnet"), network.to_bnet().unwrap()).unwrap();
    std::fs::write(path.with_extension("aeon"), network.to_string()).unwrap();
}

/// The same as `write_network`, but checks that the networks exist.
fn check_network(network: &BooleanNetwork, path: &Path, name: &str) {
    let path = path.join(name);
    let sbml = std::fs::read_to_string(path.with_extension("sbml")).unwrap();
    assert_eq!(sbml, network.to_sbml(None));
    let bnet = std::fs::read_to_string(path.with_extension("bnet")).unwrap();
    assert_eq!(bnet, network.to_bnet().unwrap());
    let aeon = std::fs::read_to_string(path.with_extension("aeon")).unwrap();
    assert_eq!(aeon, network.to_string());
}

/// Check consistency of a network with its regulatory graph.
fn check_consistency(network: &BooleanNetwork, source_dir: &Path) {
    let graph = SymbolicAsyncGraph::new(network.clone());
    if let Some(error) = graph.err() {
        eprintln!(
            "Cannot construct a graph from the model in {}. Problems:",
            source_dir.display()
        );
        eprintln!("{}", error);
        exit(128);
    }
}

/// This function is used to replace parameters specified as auto-regulated identity variables
/// with proper parameters.
fn normalize_parameters(network: BooleanNetwork) -> BooleanNetwork {
    // Detect variables
    let fake_parameters = network
        .variables()
        .filter(|id| {
            let has_one_regulator = network.regulators(*id) == vec![*id];
            let identity = FnUpdate::Var(*id);
            let has_identity_update = network.get_update_function(*id) == &Some(identity);
            has_one_regulator && has_identity_update
        })
        .collect::<Vec<_>>();

    if fake_parameters.is_empty() {
        return network;
    }

    // Create a copy of the original graph excluding regulations of fake parameters.
    let names = network
        .variables()
        .map(|id| network.get_variable_name(id).clone())
        .collect::<Vec<_>>();
    let mut new_graph = RegulatoryGraph::new(names);
    for reg in network.as_graph().regulations() {
        if fake_parameters.contains(&reg.get_target()) {
            // Don't copy regulations for fake parameters.
            continue;
        }
        new_graph
            .add_regulation(
                network.get_variable_name(reg.get_regulator()),
                network.get_variable_name(reg.get_target()),
                reg.is_observable(),
                reg.get_monotonicity(),
            )
            .unwrap();
    }

    // Copy the rest of the network, but keep the update functions for fake parameters free.
    let mut new_network = BooleanNetwork::new(new_graph);
    for var in network.variables() {
        if !fake_parameters.contains(&var) {
            let update = network.get_update_function(var).clone();
            new_network.set_update_function(var, update).unwrap();
        }
    }

    new_network
}

/// Compute the network input variables.
fn network_inputs(network: &BooleanNetwork) -> Vec<VariableId> {
    network
        .variables()
        .filter(|v| network.regulators(*v).is_empty())
        .collect()
}

/// Compute the network output variables.
fn network_outputs(network: &BooleanNetwork) -> Vec<VariableId> {
    network
        .variables()
        .filter(|v| network.targets(*v).is_empty())
        .collect()
}

/// Create a copy of the given network with all input variables fixed to a constant.
fn fix_network_inputs(network: &BooleanNetwork, value: bool) -> BooleanNetwork {
    let mut result = network.clone();
    for v in network_inputs(network) {
        result
            .set_update_function(v, Some(FnUpdate::Const(value)))
            .unwrap();
    }
    result
}

/// Create a copy of the given network with all inputs variables unspecified.
fn free_network_inputs(network: &BooleanNetwork) -> BooleanNetwork {
    let mut result = network.clone();
    for v in network_inputs(network) {
        result.set_update_function(v, None).unwrap();
    }
    result
}

fn write_metadata(network: &BooleanNetwork, url: &str, path: &Path) {
    std::fs::write(path.join("metadata.txt"), get_metadata(network, url)).unwrap();
}

fn check_metadata(network: &BooleanNetwork, url: &str, path: &Path) {
    let current = std::fs::read_to_string(path.join("metadata.txt")).unwrap();
    assert_eq!(current, get_metadata(network, url));
}

/// Compute metadata of a Boolean network.
fn get_metadata(network: &BooleanNetwork, url: &str) -> String {
    let mut metadata = format!("url: {}\n", url);
    metadata.push_str(format!("variables: {}\n", network.num_vars()).as_str());
    metadata.push_str(format!("inputs: {}\n", network_inputs(network).len()).as_str());
    metadata.push_str(format!("outputs: {}\n", network_outputs(network).len()).as_str());
    metadata.push_str(
        format!(
            "regulations: {}\n",
            network.as_graph().regulations().count()
        )
        .as_str(),
    );
    metadata.push_str(
        format!(
            "largest scc: {}\n",
            network
                .as_graph()
                .components()
                .into_iter()
                .max_by_key(|scc| scc.len())
                .unwrap()
                .len()
        )
        .as_str(),
    );
    metadata
}
