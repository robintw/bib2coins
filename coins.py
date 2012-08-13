from bibtex import bibparse
import urllib

def parse_authors(authors_string):
	authors = authors_string.split("and")
	authors = map(lambda x: x.strip(), authors)

	lastname, temp, initials = authors[0].partition(",")

	other_authors = []
	for i in range(0, len(authors)):
		other_lastname, temp, other_initials = authors[i].partition(",")
		other_authors.append(other_initials.strip() + " " + other_lastname.strip())

	return (lastname.strip(), initials.strip(), other_authors)

entries = bibparse.parse_bib("/Users/robin/Documents/University/MyPublications/AcademicPortfolio/RobinWilson.bib")

for i in range(len(entries)):
	author1_last, author1_initials, authors = parse_authors(entries[i].data['author'])

	data = {'rft.date'  : entries[i].data['year'],
			'rft.aulast': author1_last,
			'rft.auinit': author1_initials,
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

	# Do the authors bit as there can be many rft.au tags, which a dict can't cope with
	for author in authors:
		s += "&" + 'rft.au' + "=" + author

	s = urllib.quote(s)
	s = s.replace(r"%26", "&amp;")
	s = s.replace(r"%3D", "=")

	print start + s + end