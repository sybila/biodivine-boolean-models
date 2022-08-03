# Biodivine Boolean Models (BBM) Benchmark Dataset

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

If you found this dataset useful in your research, you can cite the ArXiv technical report that describes the collection:

### Contributing

If you know about a model that is not included in the dataset, we would very much like to hear about it. You can either let us know (using issues) or include the model yourself (using pull requests).

**Search for the model:** First, please make sure that the model isn't included already. The easiest option is to search for the associated model publication or author names directly in the repository. If the model is already included, its metadata files will contain this information. Additionally, it is a good idea to similarly search for open issues, since the model may be already submitted but not incorporated yet.

**Create an issue:** To let us know about the model, simply create an issue, ideally using the title `[Model] Publisher/Journal name (YYYY)` (see closed issues for title examples). The issue description should contain the bibliographic entry of the model publication, and/or other useful information for retrieving the model (e.g. a git repository where the source files are stored, etc.). Based on this information, we will try to incorporate the model as soon as possible.

**Create a pull request:** If you want to speed up the process, you can also incorporate the model on your own:

1. Create a local fork of this repository, go to the `sources` folder, find the `999_TEMPLATE` folder and duplicate it. 
2. Rename the duplicate using the model ID and the model name that you wish to use. IDs are assigned incrementally (so if the last model has ID 232, your model ID is 233). The model name can be arbitrary, but please only use capital letters, numbers and dashes. 
3. Inside the model directory, add the bibliographic entry into the `citation.bib` file and other metadata into `metadata.json` (in particular publication DOI, model URL and keywords; The meaning of keywords is detailed either here in the README, or in the technical report on ArXiv). 
4. You can also add other arbitrary notes to the `notes.md` file (e.g. how the model was obtained, known interesting properties, etc.). 
5. Add the model as `source.bnet`/`source.aeon`/`source.sbml` file. You can also include any other (reasonably small) files that you consider relevant. For example, you can include a GINsim or PyBoolNet model file, or a PDF description of the model. These files will not be processed or distributed in any way though---they are merely for completeness and/or future reference.
6. In the repository root, run `python3 sync.py YOUR_MODEL_ID` to run static analysis on the new model. If there are no problems, you should see basic information about your model. You can also verify that the model appeared in the `models` directory. For this step, you need the [AEON.py](https://github.com/sybila/biodivine-aeon-py) tool---to install it, run the `pip3 install biodivine-aeon` command.
7. If there are any issues, the script will output a list of problems that need to be fixed. At this point, you can either fix the issues yourself (however, please include the list of changes in the `notes.md` file), or you can submit the PR in this state and we will attempt to resolve the issues.
8. Finally, please also update the `report.tex` and `report.bib` files to include the new model (the table of models at the end of the document) and submit the pull request.

### Unresolved issues

When working with the dataset, you may want to consider the following limitations:

- [ ] GINsim model export automatically "hides" some logical errors in models ([Issue 57](https://github.com/sybila/biodivine-boolean-models/issues/57)).
- [ ] Regulatory network data is unavailable for `.bnet` models ([Issue 61](https://github.com/sybila/biodivine-boolean-models/issues/61)).
- [ ] Extra metadata available in `.sbml` models is erased by the static analysis workflow ([Issue 60](https://github.com/sybila/biodivine-boolean-models/issues/60)).
- [ ] In the future, we may incorporate more structural metadata; SCCs of the regulatory graph, feedback vertex set, positive/negative edges, etc. ([Issue 59](https://github.com/sybila/biodivine-boolean-models/issues/59)).

> Copyright of all models belongs to their respective authors and/or publishers. All other information is provided as is for free reproduction.