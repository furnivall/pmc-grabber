import requests


def get_pm_id(doi):
    root_url = f'https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids={doi}&format=json&versions=no'
    r = requests.get(root_url).json()
    try:
        return r['records'][0]['pmid']
    except KeyError:
        if r['status'] == 'error':
            return r
        elif r['records'][0]['status'] == 'error':
            return "Invalid DOI - looks like this file isn't available within PMC"
        else:
            print(f"Problem with your DOI, here's the output of the request: {r}")
