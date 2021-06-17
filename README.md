# Biodivine Boolean Models (BBM)

**What is this?** BBM is a collection of Boolean models (Boolean networks) used in systems biology. It aims to be a comprehensive collection suitable for benchmarking and testing new tools and methods. At the moment, there are **145 models** from major model repositories (GINsim, CellCollective, Biomodels) or individual publications. Additionally, the repository is configured to automatically check integrity of all models and generate different model formats for different tools.

This is **not** a biological database. Each model in this collection has a link to the original source where you can find more biologically relevant information. However, we do not aim to preserve or categorise this information in any way.

**What you'll find in the collection?** In the `./models` directory, each Boolean network is stored in a separate *model directory*. The directory name always contains the *number of variables*, a unique *model id*, and a short human-readable *name*. In every model directory, you can find `metadata.txt` file that contains additional structural properties of the model (no. of inputs, outputs, regulations, source url, etc.).

Each model directory then contains a `model.sbml`, `model.aeon`, and `model.bnet` files that actually contain the structure of the model. The model in each file is the same, but different tools may require a different formats, hence we provide all three.

 - `bnet` is the simplest format - it only contains the logical update functions without any information about the regulatory graph of the network.
 - `aeon` directly lists the logical update functions as well, but also contains information about the regulatory graph of the network.
 - `sbml` is XML based, and most universally used, but also the most complicated to parse and work with.

> If the model has *input* variables (sometimes called constants or parameters), i.e. variables that do not depend on any other variable, we also generate different model files for different assignment of input variables. Specifically, there is a `model_inputs_false` and `model_inputs_true` file where the value of inputs is fixed to the particular constant. Additionally, we generate `model_inputs_free`, where the update functions for the input variables are omitted (some tools interpret this as "unknown but constant" value).

**I just want the models:** If you only need one type of model file, you can have a look at the [repository releases](https://github.com/sybila/biodivine-boolean-models/releases). There are model bundles based on the type of the model (`bnet`/`aeon`/`sbml`), and the values of inputs. Each bundle contains the model files named using the model ids, so they should be much easier to process as a batch, compared to the directory structure in `./models`.  

### Citation

If you found the BBM collection useful in your research, we'll be glad if you can cite us. Soon, there should be a citable report published on ArXiv which we will link here. Until then, you can reference this github repository directly. 

## Submit a new model

We are always open to adding new models to the collection. The submission process is very easy - all you'll need is a github account, and an installation of the [Rust compiler](https://www.rust-lang.org). Simply fork this repository and create a new model directory in `./sources`: the name consists of a unique model id and a short model name using uppercase letters. Afterwards, place a `source.sbml`, `source.bnet`, or `source.aeon` model file into this directory, together with a `url.txt` file with the source where the model can be found online (for example, the DOI of the paper where the model is published). 

Finally, run the following command:

```bash
cargo run --release --bin sync
```

This will generate an entry in the `./models` directory and validate all model files. You can then submit all new files as a single pull request. In case of any problems, feel free to contact us.

Alternatively, you can create an issue with a model url that you think should be added, and we will try to add it as soon as possible.

### Misc

To validate the models without actually overwriting the `./models` directory (such as for validity checking), you can run:

```
cargo run --release --bin sync -- --check
```

Additionally, to generate the release bundles into the `./bundle` directory, you can use:

```
cargo run --release --bin bundle
```