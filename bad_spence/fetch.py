import requests

def fetch_citation(link):
    headers = {
        'Accept': 'text/x-bibliography',
        'style': 'modern-language-association-8th-edition'
    }

    resp = requests.get(link, headers=headers)
    html = resp.text
