import pathlib
from setuptools import setup, find_packages


PATH = pathlib.Path(__file__).parent
README = (PATH / 'README.md').read_text()

setup(
    name='bad-spence',
    version='0.1.0',
    description='A DOI-based citation generator.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/davidmaamoaix/bad-spence',
    author='David Ma',
    author_email='davidma@davidma.cn',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['spence=bad_spence.generator:main']
    },
    install_requires=[
        'requests', 'pqdm'
    ]
)