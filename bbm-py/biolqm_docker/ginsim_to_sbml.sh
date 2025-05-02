#!/usr/bin/env bash

# --- Configuration ---
# Name of the colomoto docker image
DOCKER_IMAGE="daemontus/biolqm-minimal"
# Alternatively, the colomoto docker image should also work...
# DOCKER_IMAGE="colomoto/colomoto-docker:2025-03-01"
# Tool inside the docker image to use for conversion
CONVERSION_TOOL="bioLQM"

# --- Script Setup ---
# Exit immediately if a command exits with a non-zero status.
set -e
# Treat unset variables as an error when substituting.
set -u
# Pipeline fails if any command fails, not just the last one.
set -o pipefail

# --- Functions ---
usage() {
  echo "Usage: $0 <input_file.zginml>"
  echo "  Converts the input .zginml file to an .sbml file with the same base name."
  echo "  Requires Docker and the '${DOCKER_IMAGE}' image to be pulled locally."
  echo "  Example: $0 my_model.zginml"
  exit 1
}

# --- Argument Parsing ---
# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
  echo "Error: Invalid number of arguments."
  usage
fi

INPUT_FILE="$1"

# Check if the input file exists
if [ ! -f "$INPUT_FILE" ]; then
  echo "Error: Input file '${INPUT_FILE}' not found."
  exit 1
fi

# Check if the input file has the .zginml extension (case-insensitive)
if [[ ! "$INPUT_FILE" =~ \.[zZ][gG][iI][nN][mM][lL]$ ]]; then
  echo "Error: Input file '${INPUT_FILE}' does not seem to be a .zginml file."
  usage
fi

# --- Determine Output Filename ---
# Get the directory part of the input file
INPUT_DIR=$(dirname "$INPUT_FILE")
# Get the filename part of the input file
INPUT_FILENAME=$(basename "$INPUT_FILE")
# Get the base name (filename without extension)
# Using parameter expansion: ${VARIABLE%PATTERN} removes shortest matching suffix
BASE_NAME="${INPUT_FILENAME%.*}"
# Construct the output filename
OUTPUT_FILENAME="${BASE_NAME}.sbml"
OUTPUT_FILE="${INPUT_DIR}/${OUTPUT_FILENAME}" # Keep output in the same dir as input

# --- Check Docker ---
if ! command -v docker &> /dev/null; then
    echo "Error: Docker command not found. Please install Docker."
    exit 1
fi
# Optional: Check if the image exists locally, though docker run will pull if needed
if ! docker image inspect "$DOCKER_IMAGE" &> /dev/null; then
   echo "Warning: Docker image '${DOCKER_IMAGE}' not found locally. Docker will attempt to pull it."
fi


# --- Perform Conversion ---
echo "Input file:  '${INPUT_FILE}'"
echo "Output file: '${OUTPUT_FILE}'"

# Get the absolute path of the input directory for volume mounting
# Use 'pwd -P' if the path might contain symlinks and you want the physical path
# Or just 'pwd' if logical path is fine. Use realpath for robustness if available.
if command -v realpath &> /dev/null; then
    HOST_WORKDIR=$(realpath "$(dirname "$INPUT_FILE")")
else
    # Fallback using pwd, might have issues with relative paths containing '..'
    # or complex symlinks
    HOST_WORKDIR=$(cd "$(dirname "$INPUT_FILE")" && pwd)
fi

CONTAINER_WORKDIR="/workspace"

echo "Attempting conversion using Docker image '${DOCKER_IMAGE}'..."

# Run the conversion command inside the docker container
# --rm : Remove the container automatically when it exits
# -v   : Mount the host directory containing the file(s) into the container
# -w   : Set the working directory inside the container
docker run --rm \
  -v "${HOST_WORKDIR}:${CONTAINER_WORKDIR}" \
  -w "${CONTAINER_WORKDIR}" \
  "${DOCKER_IMAGE}" \
  "${CONVERSION_TOOL}" "${INPUT_FILENAME}" "${OUTPUT_FILENAME}"

# --- Verification ---
# Check if the docker command succeeded (exit code 0) and if the output file was created
if [ $? -eq 0 ] && [ -f "$OUTPUT_FILE" ]; then
  echo "Conversion successful!"
  echo "Output saved to: '${OUTPUT_FILE}'"
  exit 0
else
  echo "Error: Conversion failed. Please check Docker output for details."
  # Clean up potentially empty/partial output file if it exists but conversion failed
  if [ -f "$OUTPUT_FILE" ]; then
      rm "$OUTPUT_FILE"
  fi
  exit 1
fi