import requests


def fetch_citation(link):
    data = {
        'doi': link,
        'style': 'modern-language-association-8th-edition',
        'lang': 'en-US'
    }

    resp = requests.get('https://citation.crosscite.org/format', params=data)
    if resp.status_code != 200:
        raise ValueError(
            f'bad request when handling {link}: code {resp.status_code}'
        )

    return (link, resp.text.strip())
