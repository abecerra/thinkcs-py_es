#!/usr/bin/env python
#
#	transform .tex chapter to lore html
#
import string, sys

heading = """\
<html>
<head>
  <title>%s</title>
</head>
<body>
<h1>%s</h1>
"""

nextline = " "

def getline () :
	global nextline
	lin = nextline
	if nextline != None :
		nextline = sys.stdin.readline()
		if not nextline : nextline = None
		else            : nextline = string.strip(nextline)
	return lin

def find (l, what) :
	return string.find(l, what) >= 0

def replace (l, what, till, with) :
	did = 0
	while 1 :
		i = string.find(l, what)
		if i < 0 : return l, did
		j = string.find(l[i:],till)
		if j < 0 : return l, did
		dict = {'inner': l[i+len(what):i+j]}
		l = l[:i]+with%dict +l[i+j+len(till):]
		did = 1

def main () :
	getline()      # prime the pump
	inpara = inpre = 0; parasep = "p"
	while 1 :
		lin = getline()
		if lin == None : break

		chap = find(lin,"\\chapter{")
		if chap :
			chap = lin[9:-1]
			print heading % (chap,chap)
			continue

		if lin[0:1] == "%" : continue
		if find(lin, "\\adjustpage") : continue
		if find(lin, "\\beforeverb") : continue
		if find(lin, "\\afterverb")  : continue
		if find(lin, "\\beforefig")  : continue
		if find(lin, "\\afterfig")   : continue
                if find(lin, "\\vspace") : continue
                if find(lin, "\\begin{flushleft}"): continue
                if find(lin, "\\end{flushleft}"): continue
                if find(lin, "\\end{itemize}"): continue
                if find(lin,"\\\\"):
                    continue
		if find(lin, "\\begin{verbatim}") :
			print '<pre class="python">'
			inpre = 1 ; continue
		if find(lin, "\\end{verbatim}") :
			print '</pre>\n'
			inpre = 0 ; continue
		if find(lin, "\\begin{description}") :
			print '<dl>'
			parasep = "dd" ; continue
		if find(lin, "\\end{description}") :
			print '</dl>\n'
			parasep = "p" ; continue

		lin,did = replace(lin,"\\section{",'}', '<h2>%(inner)s</h2>')
		if  did : print lin; continue
		lin,did = replace(lin,"\\index{",'}', '<span class="index" value="%(inner)s"/>')
		if  did : print lin; continue
		lin,did = replace(lin,"\\item[",']', '<dt>%(inner)s</dt>\n<dd>')
		if  did :
			if nextline == "" : lin = lin+"</dd>"
			else              : inpara = 1
			print lin; continue

		lin,did = replace(lin,"{\\bf ",'}',    '<strong>%(inner)s</strong>')
		lin,did = replace(lin,"{\\tt ",'}',    '<code>%(inner)s</code>')
		lin,did = replace(lin,"{\\em ",'}',    '<em>%(inner)s</em>')
		if inpre : lin = "   " + lin
		if not inpre and not inpara and lin :
			lin = "<%s>"%parasep + lin
			inpara = 1
		if not inpre and inpara and nextline == "" :
			lin = lin + "</%s>"%parasep
			inpara = 0
		print lin
	print "</body>"
	print "</html>"

if __name__ == "__main__" : main()

