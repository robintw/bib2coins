import os
from setuptools import setup


setup(
    name = "bib2coins",
    packages = ['bibtex'],
    py_modules = ['bib2coins'],
    scripts = ['bib2coins'],
    version = "0.1",
    author = "Robin Wilson",
    author_email = "robin@rtwilson.com",
    description = ("""Module to parse human-style date ranges (eg. 15th-19th March 2011) to datetimes"""),
    license = "BSD",
    url = "https://github.com/robintw/bib2coins",
    long_description="""bib2coins is a simple tool which will convert BibTeX files to COINS metadata (see http://ocoins.info/) ready for inclusion in a webpage. You may want to use this is you have a BibTeX file of your own publications and you display a list of these publications on a webpage. bib2coins can be used to convert the BibTeX files to a set of <span> elements which can be included in your HTML file to allow bibliographic software (such as Mendeley and Zotero) to automatically pick up the metadata from the page and allow the papers on the page to be easily added to the software's database.""",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        "Programming Language :: Python"
        
    ],
)