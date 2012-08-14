bib2coins
=========

bib2coins is a simple tool which will convert BibTeX files to COINS metadata (see http://ocoins.info/) ready for inclusion in a webpage. You may want to use this is you have a BibTeX file of your own publications and you display a list of these publications on a webpage. bib2coins can be used to convert the BibTeX files to a set of `<span>` elements which can be included in your HTML file to allow bibliographic software (such as Mendeley and Zotero) to automatically pick up the metadata from the page and allow the papers on the page to be easily added to the software's database.

Usage
-----
Simply run `bib2coins <bibtextfilename>` and it will print the COINS metadata to the standard output, ready to be piped into a HTML file.

Current status
--------------
This is beta software, and is not yet finished. At the moment it will create COINS metadata for journal articles and conference proceedings, and the entries will be mostly (if not entirely) complete. It may work for other item types such as books, but I haven't done any testing of those yet.