import argparse

from .fetch import fetch_citation


def main():

    parser = argparse.ArgumentParser(
        description='a DOI-based citation generator'
    )

    parser.add_argument('path', type=str, help='path to the DOI list file')
    parser.add_argument(
        '-s', '--sort',
        default='none',
        const='none',
        nargs='?',
        choices=['none', 'name'],
        help='how to sort the output'
    )

    args = parser.parse_args()

    file = args.path
    sort = args.sort

    with open(file, 'r') as f:
        srcs = f.readlines()

    links = []
    for src in srcs:
        link = src.strip()
        if not link: continue

        if not link.startswith('10'):
            raise ValueError(
                f'{link} does not begin with "10" (format not yet supported)'
            )

        links.append(f'https://doi.org/{link}')
