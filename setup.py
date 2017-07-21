from setuptools import setup

setup(name='mzdb_wrapper',
    version='0.5',
    description='An extremely simple interface for databases. ',
    url='https://github.com/mznco/mzdb_wrapper',
    author='mznco',
    author_email='admin@mznco.net',
    license='GPL-3.0',
    packages=['mzdb_wrapper'],
    install_requires=[
        'MySQL-python',
        'psycopg2',
        'logging'
    ],
    zip_safe=False)
