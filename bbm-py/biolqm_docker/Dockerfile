# Use Miniconda as the base image
FROM continuumio/miniconda3

# Set working directory
WORKDIR /app

# Add necessary channels for conda
RUN conda config --add channels colomoto && \
    conda config --add channels conda-forge && \
    conda config --add channels potassco

# Add the colomoto channel and install ginsim and ginsim-python
RUN conda install -y ginsim ginsim-python && \
    conda clean -afy

# Set default command
CMD ["bash"]