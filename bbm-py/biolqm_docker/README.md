# Minimal ginsim/biolqm docker environment

Here, we define a simple docker image that has `ginsim` and `biolqm` installed. 
These can be used to run some typical conversion tasks.
The reason why we use these tools as a docker image is that they require `conda`, 
which we would like to avoid requiring globally.

An alternative is to use `colomoto/colomoto-docker` image. 
However, this image is rather large when installed (4.4GB), 
whereas our image is comparably smaller ("only" 1.3GB).

## Using `biolqm`

We provide a script which converts `.zginml` files to `.sbml`:

```
./ginsim_to_sbml.sh /path/to/model.zginml
```

The output will be saved with the same name and in the same location as the original model, but using `.sbml` file extension.

## Building the docker image

The docker image is being built and published by the `biolqm_docker.yml` CI workflow whenver a tag starting with `biolqm-` is created. 
Altenratively, you can also build and publish it locally (commands are in the `Makefile`). 
However, you have to be logged in as `daemontus` on Docker Hub.