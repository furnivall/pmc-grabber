from full_text_requests import get_full_text_json, get_raw_text_from_json
from id_handler import get_pm_id

with open('data.txt', 'r') as f:
    doi_list = f.read().split('\n')
    print(doi_list)

def write_to_file(text, pm_id):
    with open(f'full_texts/{pm_id}.txt', 'w+') as f:
        f.write(text)


for doi in doi_list:
    pm_id = get_pm_id(doi)
    if 'Invalid DOI' not in pm_id:
        full_text_json = get_full_text_json(pm_id)
        full_text_doc = get_raw_text_from_json(full_text_json)
        write_to_file(full_text_doc, pm_id)
