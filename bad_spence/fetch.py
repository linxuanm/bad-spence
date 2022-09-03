import requests

def fetch_citation(link):
    headers = {
        'Accept': 'text/x-bibliography',
        'style': 'modern-language-association-8th-edition'
    }

    resp = requests.get(link, headers=headers)
    if resp.status_code != 200:
        raise ValueError(
            f'bad request when handling {link}: code {resp.status_code}'
        )

    return resp.text

fetch_citation('https://doi.org/10.48550/arXiv.1910.00935')
