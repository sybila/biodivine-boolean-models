use std::process::exit;
use regex::Regex;
use std::path::Path;

/// This binary will try to analyse the files in `models` directory and group them into easily
/// processable groups into the bundle directory. Specifically, it will produce the following:
///  - `bundle/all-aeon`, `bundle/all-bnet`, and  - `bundle/all-sbml`
///  - `bundle/inputs-true-aeon`, `bundle/inputs-true-bnet`, and  - `bundle/inputs-true-sbml`
///  - `bundle/inputs-false-aeon`, `bundle/inputs-false-bnet`, and  - `bundle/inputs-false-sbml`
///  - `bundle/inputs-free-aeon`, `bundle/inputs-free-bnet`, and  - `bundle/inputs-free-sbml`
fn main() {
    let root = std::env::current_dir().unwrap();
    let models_dir = root.join("models");
    let bundle_dir = root.join("bundle");

    if !models_dir.exists() {
        eprintln!("Models directory not found.");
        exit(128);
    }

    if !bundle_dir.exists() {
        std::fs::create_dir_all(bundle_dir.clone()).unwrap();
    }

    // Create paths for bundles
    std::fs::create_dir_all(bundle_dir.join("all-aeon")).unwrap();
    std::fs::create_dir_all(bundle_dir.join("all-bnet")).unwrap();
    std::fs::create_dir_all(bundle_dir.join("all-sbml")).unwrap();

    std::fs::create_dir_all(bundle_dir.join("inputs-true-aeon")).unwrap();
    std::fs::create_dir_all(bundle_dir.join("inputs-true-bnet")).unwrap();
    std::fs::create_dir_all(bundle_dir.join("inputs-true-sbml")).unwrap();

    std::fs::create_dir_all(bundle_dir.join("inputs-false-aeon")).unwrap();
    std::fs::create_dir_all(bundle_dir.join("inputs-false-bnet")).unwrap();
    std::fs::create_dir_all(bundle_dir.join("inputs-false-sbml")).unwrap();

    std::fs::create_dir_all(bundle_dir.join("inputs-free-aeon")).unwrap();
    std::fs::create_dir_all(bundle_dir.join("inputs-free-bnet")).unwrap();
    std::fs::create_dir_all(bundle_dir.join("inputs-free-sbml")).unwrap();

    let models_dir_regex = Regex::new(r"\[var:\d+]__\[id:(\d+)]__.+").unwrap();

    for source in std::fs::read_dir(models_dir).unwrap() {
        let source = source.unwrap();
        let name = source.file_name().to_str().unwrap().to_string();
        if name.starts_with(".") {
            // Skip dot-files
            continue;
        }
        let id = if let Some(matched) = models_dir_regex.captures(name.as_str()) {
            matched[1].to_string()
        } else {
            eprintln!("Unrecognized file/directory in models: {}.", name);
            exit(128);
        };

        move_to_bundle(id.as_str(), &source.path(), "model", &bundle_dir, "all");
        if source.path().join("model_inputs_free.aeon").exists() {
            move_to_bundle(id.as_str(), &source.path(), "model_inputs_free", &bundle_dir, "inputs-free");
            move_to_bundle(id.as_str(), &source.path(), "model_inputs_false", &bundle_dir, "inputs-false");
            move_to_bundle(id.as_str(), &source.path(), "model_inputs_true", &bundle_dir, "inputs-true");
        }
        println!("Processed model id {}.", id);
    }
}

// Distribute an aeon/bnet/sbml file to the respective bundle directories.
fn move_to_bundle(id: &str, model_dir: &Path, name_prefix: &str, bundle_dir: &Path, bundle_prefix: &str) {
    let model_path = model_dir.join(name_prefix);

    std::fs::copy(
        model_path.with_extension("aeon"),
        bundle_dir
            .join(&format!("{}-aeon", bundle_prefix))
            .join(&format!("{}.aeon", id))
    ).unwrap();

    std::fs::copy(
        model_path.with_extension("bnet"),
        bundle_dir
            .join(&format!("{}-bnet", bundle_prefix))
            .join(&format!("{}.bnet", id))
    ).unwrap();

    std::fs::copy(
        model_path.with_extension("sbml"),
        bundle_dir
            .join(&format!("{}-sbml", bundle_prefix))
            .join(&format!("{}.sbml", id))
    ).unwrap();
}