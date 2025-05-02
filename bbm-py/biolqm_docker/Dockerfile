# Use Miniconda as the base image
FROM continuumio/miniconda3

# Set working directory
WORKDIR /app

# Add necessary channels for conda
RUN conda config --add channels colomoto && \
    conda config --add channels conda-forge && \
    conda config --add channels potassco

# Install ginsim and ginsim-python (should also install bioLQM and nusmv)
RUN conda install -y ginsim ginsim-python && \
    conda clean -afy

# Set default command
CMD ["bash"]