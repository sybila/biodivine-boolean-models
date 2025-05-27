import requests
import json
import csv
import os
import glob
import subprocess

from MissingId import MissingIdException

# 4942
# https://research.cellcollective.org/web/api/model/295579/export/version/1?type=SBML&modeltype=boolean

def check_source_file(bbm_id):
    matches = glob.glob(f'../../sources/{int(bbm_id):03}_*') #finds matching model directories
    files = os.listdir(matches[0])
    for file in files:
        if file.startswith('source') and 'cellcollective' in file:
            return None
    return matches[0]


def download_model(ccid, version, dest):
    url = f"https://research.cellcollective.org/web/api/model/{ccid}/export/version/{version}?type=SBML&modeltype=boolean"
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(f"{dest}/source.cellcollective.sbml", "wb") as sbml_file:
            sbml_file.write(response.content)
            print("Download complete")
    except requests.exceptions.RequestException as e:
            print(f"Download failed: {e}")


def check_ginsim_files(bbm_id):
    matches = glob.glob(f'../../sources/{int(bbm_id):03}_*') #finds matching model directories
    files = os.listdir(matches[0])
    for file in files:
        if file.startswith('source') and 'ginsim' in file:
            return None
    return matches[0]


def download_ginsim_model(ginsim_id, version, dest):
    ginsim_id = './GINsim.github.io/content/models/' + ginsim_id 
    if ginsim_id.endswith('sbml'):
        try:
            subprocess.run(['cp', ginsim_id, dest])
        except:
            print(f'File {ginsim_id} could not be copied to {des}')
    elif ginsim_id.endswith('zginml'):
        ginsim_sbml_file = ginsim_id.replace('.zginml', '.sbml')
        #sbml_file = ginsim_sbml_file.split('/')[-1]
        try:
            subprocess.run(['sudo', '../biolqm_docker/ginsim_to_sbml.sh', ginsim_id])
            subprocess.run(['mv', ginsim_sbml_file, dest + '/source.ginsim.sbml'])
        except:
            print(f'File {ginsim_id} could not be converted into sbml file format')


def download_new_models_in_mapping_table(mapping_table):
    for line in mapping_table:
        if line[0] == 'bbm_id':
            continue
        
        if line[0] == '':
            continue
        if line[2] == '' and line[4] == '':
            raise MissingIdException(line[0])

        if line[1] == 'cellcollective':
            new_folder = check_source_file(line[0])
            if new_folder:
                download_model(line[2], line[3],  new_folder)
        elif line[1].lower() == 'ginsim':
            new_source = check_ginsim_files(line[0])
            if new_source:
                download_ginsim_model(line[4], line[5], new_source)


def download_new_in_mapping_table():
    with open("mapping_table.csv", "r") as mapping_table:
        csv_file = csv.reader(mapping_table)
        download_new_models_in_mapping_table(csv_file)


if __name__ == "__main__":
    download_new_in_mapping_table()
