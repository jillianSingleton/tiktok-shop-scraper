thonimport csv
import json
from extractors.utils import save_to_file

def export_to_csv(data):
    keys = data[0].keys() if data else []
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print("Data has been exported to output.csv")

def export_to_json(data):
    save_to_file(data, 'output.json')
    print("Data has been exported to output.json")