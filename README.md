# Biodivine Boolean Models (BBM) Benchmark Dataset

**What is this?** BBM is a collection of Boolean models (Boolean networks) used in systems biology. It aims to be a comprehensive collection suitable for benchmarking and testing new tools and methods. At the moment, there are **210+ models** from major model repositories (GINsim, CellCollective, Biomodels, etc.) or individual publications. Additionally, the repository is configured to automatically check integrity of all models and generate different model formats for different tools.

Note that this is **not** a biological database. Each model has a link to the original source where you can find more biologically relevant data. However, we do not aim to preserve or categorise this additional information in any way.

If you want to know more, you can read our [technical report](./report/report.pdf).

**Where are the models?** If you just need individual models, you can head to the `./models` directory where each model has a subdirectory containing `bnet`/`aeon`/`sbml` source files as well as JSON metadata file and a human-friendly readme. There is also a `models/summary.csv` file with the full list of models. Alternatively, you can download one of the "edition archives" in the [repository releases](https://github.com/sybila/biodivine-boolean-models/releases). These contain the same model files as the `./models` directory, but are grouped by model format and exported as a single directory, so they are easier to digest by scripts or programs.

> Note on model inputs: By default, all inputs (entities with no incoming regulations) are represented as "free" variables (i.e. their update function is omitted). However, this is not supported by all tools. If you need to, you can change this input representation when generating a custom "edition" of the dataset (see below).

> Note on multivalued models: The dataset also includes Booleanized versions of multi-valued models. If you wish to exclude these, they can be identified using the keyword `multi-valued`.

### Citation

If you found this dataset useful in your academic work, you can cite the [technical report](https://doi.org/10.1101/2023.06.12.544361):

```
Repository of logically consistent real-world Boolean network models
Samuel Pastva, David Safranek, and others
bioRxiv 2023.06.12.544361; doi: https://doi.org/10.1101/2023.06.12.544361
```

### Custom Model Editions

If you need models with specific properties, you can use `bundle.py` to generate custom model editions. In particular, for each edition you can pick the desired format (`bnet`/`aeon`/`sbml`), desired input representation (`free`, constant `true` or `false`, or the `identity` function), and you can filter the models using a Python expression (e.g. you want to only include models with specific keywords).

Once you have [AEON.py](https://github.com/sybila/biodivine-aeon-py) installed (`pip install biodivine_aeon`), you can simply run `python3 bundle.py` and answer the script prompts with your desired specification. For inspiration, here are several filter expression that can be useful for generating custom editions:

```
# Models with at least 10 variables and 5 inputs:
len(variables) > 10 and len(inputs) > 5
# Models that are on GINsim but not on CellCollective:
'ginsim' in metadata['keywords'] and not 'cellcollective' in metadata['keywords']
# Models with variable ERK that are originally multi-valued.
'ERK' in variables and 'multi-valued' in metadata['keywords']
```

### Contributing

We accept new models and improvements through issues and pull request. In [CONTRIBUTING.md](./CONTRIBUTING.md), you can find how to let us know about a new model through an issue or a pull request.

### Random networks

Currently, we only accept networks that have a demonstrated relationship with some biological system. However, we do not assume any specific level of curation---the models can be hand made, inferred from data, or anything in between. This rules out randomly generated models though. If you would also like to test your tool on randomly generated networks, we can recommend [this](https://zenodo.org/record/3714876#.YxXVYi8Rr0o) or [this](https://github.com/daemontus/artifact_cav2021/tree/master/benchmarks_random) dataset (and the associated network generators). 

### Unresolved issues

When working with the dataset, you may want to consider the following limitations:

- [ ] GINsim model export automatically "hides" some logical errors in models ([Issue 57](https://github.com/sybila/biodivine-boolean-models/issues/57)).
- [ ] Regulatory network data is unavailable for `.bnet` models ([Issue 61](https://github.com/sybila/biodivine-boolean-models/issues/61)).
- [ ] Extra metadata available in `.sbml` models is erased by the static analysis workflow ([Issue 60](https://github.com/sybila/biodivine-boolean-models/issues/60)).
- [ ] In the future, we may incorporate more structural metadata; SCCs of the regulatory graph, feedback vertex set, positive/negative edges, etc. ([Issue 59](https://github.com/sybila/biodivine-boolean-models/issues/59)).

> Copyright of all models belongs to their respective authors and/or publishers. All other information is provided as is for free reproduction.