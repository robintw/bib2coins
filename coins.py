from bibtex import bibparse
import urllib

def parse_authors(authors_string):
	authors = authors_string.split("and")
	authors = map(lambda x: x.strip(), authors)
	print authors


	lastname, temp, initials = authors[0].partition(",")

	return (lastname.strip(), initials.strip())

entries = bibparse.parse_bib("/Users/robin/Documents/University/MyPublications/AcademicPortfolio/RobinWilson.bib")

i = 0

print entries[i]






author1_last, author1_initials = parse_authors(entries[i].data['author'])

data = {'rft.date'  : entries[i].data['year'],
		'rft.aulast': author1_last,
		'rft.auinit': author1_initials,
		'rft.au'	: author1_initials + " " + author1_last
}

end = "'></span>"


if entries[i].btype == "article":
	# Do a journal article
	start = "<span class='Z3988' title='url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal"
	data['rft.genre'] = "article"
	data['rft.atitle'] = entries[i].data['title']
	data['rft.jtitle'] = entries[i].data['journal']
else:
	start = "<span class='Z3988' title='url_ver=Z39.88-2004&amp;ctx_ver=Z39.88-2004&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook"
	data['rft.genre'] = "proceeding"
	data['rft.atitle'] =  entries[i].data['title']
	data['rft.btitle'] = entries[i].data['booktitle']


s = ""

for key, value in data.iteritems():
	s += "&" + key + "=" + value

s = urllib.quote(s)
s = s.replace(r"%26", "&amp;")
s = s.replace(r"%3D", "=")

print start + s + end