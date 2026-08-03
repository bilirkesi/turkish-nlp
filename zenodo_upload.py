import requests
import json
import sys

URL = 'https://zenodo.org/api/deposit/depositions'
TOKEN = 'Ns5Mq8BGU0oWmgcr5NGm6nkPzrHcJkbsFhzQSej0Aon63311kzR7r6zKWKeR'

headers = {'Content-Type': 'application/json'}
data = {
    'metadata': {
        'title': 'Osmanlica-Bench-v1: Benchmark Dataset for Ottoman Turkish Transliteration',
        'upload_type': 'dataset',
        'description': 'Benchmark dataset for evaluating Ottoman Turkish transliteration systems. Contains 6,500 paired Ottoman Turkish (Arabic script) and Modern Turkish (Latin script) text samples from historical sources spanning the 15th-20th centuries.',
        'creators': [{'name': 'Bilirkesi AI Team'}],
        'keywords': ['ottoman-turkish', 'transliteration', 'nlp', 'digital-humanities', 'turkish'],
        'license': 'mit'
    }
}

print("Creating deposition...")
response = requests.post(URL, headers=headers, json=data, params={'access_token': TOKEN})
print(f"Status: {response.status_code}")

if response.status_code == 201:
    deposition = response.json()
    deposition_id = deposition['id']
    print(f"Deposition ID: {deposition_id}")
    
    # Get files upload URL
    files_url = f"https://zenodo.org/api/deposit/depositions/{deposition_id}/files"
    
    # Upload file
    with open('osmanlica-bench-v1.tar.gz', 'rb') as f:
        files = {'file': ('osmanlica-bench-v1.tar.gz', f, 'application/gzip')}
        file_response = requests.post(files_url, params={'access_token': TOKEN}, files=files)
        print(f"Upload status: {file_response.status_code}")
        
        if file_response.status_code == 201:
            file_data = file_response.json()
            print(f"File ID: {file_data['id']}")
            print(f"Filename: {file_data['filename']}")
            
            # Publish deposition
            publish_url = f"https://zenodo.org/api/deposit/depositions/{deposition_id}/actions/publish"
            publish_response = requests.post(publish_url, params={'access_token': TOKEN})
            print(f"Publish status: {publish_response.status_code}")
            
            if publish_response.status_code == 202:
                print(f"\nSUCCESS!")
                print(f"DOI: https://doi.org/10.5281/zenodo.{deposition_id}")
                print(f"URL: https://zenodo.org/record/{deposition_id}")
            else:
                print(f"Publish error: {publish_response.text}")
        else:
            print(f"Upload error: {file_response.text}")
else:
    print(f"Error: {response.text}")
    sys.exit(1)
