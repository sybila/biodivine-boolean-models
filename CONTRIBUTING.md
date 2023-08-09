# Contributing

If you know about a model that is not included in the dataset, we would very much like to hear about it. You can either let us know (using issues) or include the model yourself (using pull requests).

**Search for the model:** First, please make sure that the model isn't included already. The easiest option is to search for the associated model publication or author names directly in the repository. If the model is already included, its metadata files will contain this information. Additionally, it is a good idea to similarly search for open issues, since the model may be already submitted but not incorporated yet.

**Create an issue:** To let us know about the model, simply create an issue, ideally using the title `[Model] Publisher/Journal name (YYYY)` (see other issues for title examples). The issue description should contain the bibliographic entry of the model publication and/or other useful information for retrieving the model (e.g. a git repository where the source files are stored, etc.). Based on this information, we will try to incorporate the model as soon as possible.

**Create a pull request:** If you want to speed up the process, you can also incorporate the model on your own:

1. Create a local fork of this repository, go to the `sources` folder, find the `999_TEMPLATE` folder and duplicate it. 
2. Rename the duplicate folder using the model ID and the model name that you wish to use. IDs are assigned incrementally (so if the last model has ID 232, your model ID is 233). The model name can be arbitrary, but please use capital letters, numbers and dashes only. 
3. Inside the model directory, add the bibliographic entry into `citation.bib` and other metadata into `metadata.json` (in particular publication DOI, model URL and keywords; The meaning of keywords is detailed in the [technical report](./report/report.pdf)). 
4. You can also add other arbitrary notes to the `notes.md` file (e.g. how the model was obtained, known interesting properties, etc.). 
5. Add the model as `source.bnet`/`source.aeon`/`source.sbml` file. You can also include any other (reasonably small) files that you consider relevant. For example, you can include a GINsim or PyBoolNet model file, or a PDF description of the model. These files will not be processed or distributed in any way though---they are merely for completeness and/or future reference.
6. In the repository root, run `python3 sync.py YOUR_MODEL_ID` to run static analysis on the new model. If there are no problems, you should see basic structural info about your model. You can also verify that the model is correctly exported in the `models` directory. For this step, you need the [AEON.py](https://github.com/sybila/biodivine-aeon-py) tool---to install it, run the `pip3 install biodivine-aeon==0.2.0` command.
7. If there are any issues, the script will output a list of problems that need to be fixed. At this point, you can either fix the issues yourself (however, please include the list of changes compared to the published version in the `notes.md` file), or you can submit the PR in this state and we will attempt to resolve the issues.
8. Finally, please also update the `online_only_table_1.xlsx` and possibly `online_only_table_2.xlsx` files to include the new model and submit the pull request (you can also submit without doing this, but we will have to update the tables).