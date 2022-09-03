import argparse
from pqdm.threads import pqdm

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

        links.append(link)

    htmls = pqdm(links, fetch_citation, n_jobs=4)

    if sort == 'none':
        htmls = sorted(htmls, key=lambda x, l=links: l.index(x[0]))
    else:
        htmls = sorted(htmls, key=lambda x: x[1])

    print('\n\n'.join(i[1] for i in htmls))
