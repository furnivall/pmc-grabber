import requests

def get_full_text_json(pm_id):
    base_url_full_text = f'https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{pm_id}/unicode'

    r = requests.get(base_url_full_text).json()
    return r['documents'][0]

def get_raw_text_from_json(json):
    section_types_counter = {}
    document = ""
    for i in json['passages']:
        section_type = i['infons']['section_type']
        if section_type == "REF":
            continue
        if section_type not in section_types_counter:
            section_types_counter[section_type] = 1
            document += "\n\n"
        else:
            section_types_counter[section_type] += 1
        document += "\n" + i['text']

    print(f'Section types in this document: {section_types_counter}')
    return document
