import subprocess
import sys
import requests
import glob
import argparse

def valid_doi(doi):
    url = f"https://doi.org/{doi}"
    crossref_url = f"https://api.crossref.org/works/{doi}"
    try:
        response = requests.get(crossref_url, allow_redirects=True, timeout=5)
        data = response.json()
        title = data["message"]["title"][0]
        return response.status_code == 200 and title
    except requests.RequestException:
        return False


def valid_bbm_id(bbm_id):
    if glob.glob(f"./sources/{int(bbm_id):03}_*"):
        return True
    return False


def convert_doi(doi, bbm_id):
    dest_folder = glob.glob(f"./sources/{int(bbm_id):03}_*")[0]
    try:
        subprocess.run(f"doi2bib {doi} > {dest_folder}/citation.bib", shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Converting DOI: {doi} to bib has failed")



def main():
    parser = argparse.ArgumentParser(
        description="Convert valid DOI to bib and save citation.bib to the appropriate directory for the specified BBM ID"
    )

    parser.add_argument("doi", help="DOI (e.g., 10.1000/xyz123)")
    parser.add_argument("bbm_id", help="Model identifier")

    args = parser.parse_args()

    doi = args.doi
    bbm_id = args.bbm_id

    if not valid_doi(doi):
        print(f"Invalid DOI format: {doi}")
        return

    if not valid_bbm_id(bbm_id):
        print(f"Invalid BBM ID: {bbm_id}")
        return

    print(f"DOI: {args.doi}")
    print(f"Model ID: {args.bbm_id}")
    
    convert_doi(doi, bbm_id)
if __name__ == "__main__":
    main()
