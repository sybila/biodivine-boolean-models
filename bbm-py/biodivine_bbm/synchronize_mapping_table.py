import requests
import json
import csv
import os
import glob
import zipfile
import xml.etree.ElementTree as ET

from git import Repo

# 4942
# https://research.cellcollective.org/web/api/model/295579/export/version/1?type=SBML&modeltype=boolean

def github_ginsim_pul():
    repo = Repo('GINsim.github.io')
    origin = repo.remotes.origin
    origin.pull()


def parse_json():
    url = "https://research.cellcollective.org/web/api/model/cards/research?modelTypes=boolean&orderBy=recent&category=published&cards=5"
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data


def missing_models_ginsim(existing_models):
    models = set()
    path = "./GINsim.github.io/content/models"
    dirs = os.listdir(path)
    for model_dir in dirs:
        if model_dir.startswith('_'):
            continue
        sbmls = [file for file in os.listdir(f"{path}/{model_dir}") if file.endswith('.sbml')]
        zginmls = [file for file in os.listdir(f"{path}/{model_dir}") if file.endswith('.zginml')]
        for sbml in sbmls:
            models.add(f"{model_dir}/{sbml}")

        for zginml in zginmls:
            with zipfile.ZipFile(f"{path}/{model_dir}/{zginml}", 'r') as zip_ref:
                for file in zip_ref.namelist():
                    if file.endswith('.ginml'):
                        models.add(f"{model_dir}/{zginml}/{file}")

    missing = models.difference(existing_models)
    print_missing_ginsim(missing)
    return missing

def print_missing_ginsim(missing):
    print("Missing models from GINsim:")
    for model in missing:
        print(model)


def missing_models_cellcolletive(json_data, existing_models):
    models = set()
    model_names = {}
    for model in json_data:
        model_id = model['model']['id']
        model_version_map = model['model']['modelVersionMap']
        for key in model_version_map.keys():
            if "version"  in model_version_map[key].keys():
                model_version = model_version_map[key]["version"]
                identifier = (str(model_id), str(model_version))
                models.add(identifier)
                model_names[identifier] = model['model']['name']

    missing = models.difference(existing_models)
    print_missing_cellcollective(missing, model_names)
    return missing


def models_in_mapping_table(mapping_table):
    ids_in_table = set()
    for line in mapping_table:
        # reading the header
        if line[0] == 'bbm_id':
            continue

        if line[1] == 'cellcollective':
            ids_in_table.add((line[2], line[3]))
        elif line[1] == 'ginsim':
            ids_in_table.add((line[2], line[3]))
    return ids_in_table


def print_missing_cellcollective(missing_models, model_names):
    print('Missing models from CellCollective:')
    for model in missing_models:
        print(model_names[model] + ', version: ' + model[1])
        
    print()


def synchronize_mapping_table():
    #github_ginsim_pull()
    with open("mapping_table.csv", "r") as mapping_table:
        csv_file = csv.reader(mapping_table)
        in_mapping_table = models_in_mapping_table(csv_file)
        json_data = parse_json()
        missing_cellcollective = missing_models_cellcolletive(json_data, in_mapping_table)
        missing_ginsim = missing_models_ginsim(in_mapping_table)


if __name__ == '__main__':
    synchronize_mapping_table()
