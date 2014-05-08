LATEX = latex
DVIPS = dvips


top.dvi: top.tex 
	latex --src-specials  top
	latex --src-specials top
	latex --src-specials top
	#latex  --src-specials -interaction=nonstopmode top
	makeindex top
	latex  --src-specials top
	cp top.dvi thinkCSpy.dvi

puj: puj.tex
	latex --src-specials puj
	latex --src-specials puj
	latex --srs-specials puj
	makeindex puj
	latex --src-specials puj
	cp puj.dvi introprog-py.dvi
	dvips -o introprog-py.ps introprog-py.dvi  
	ps2pdf introprog-py.ps

final:
	latex  puj
	latex  puj
	latex  puj
	makeindex puj
	latex  puj
	cp puj.dvi introprog-py.dvi
	dvips -o introprog-py.ps introprog-py.dvi  
	ps2pdf introprog-py.ps

ps: top.dvi
	dvips -Ppdf  -o thinkCSpy.ps top.dvi
	#dvips -T 6.75in,9.25in -Ppdf -o thinkCSpy.ps top

pdf: ps
	ps2pdf thinkCSpy.ps

dvi: top.dvi

bookhtml:
	sh transform.sh
	lore -pN -b thinkCSpy.book
	mv *.html html

dist: 
	cp Makefile *.tex thinkCSpy
	cp -r illustrations thinkCSpy
	rm thinkCSpy/illustrations/*.bak
	cd thinkCSpy; make clean
	tar -czf thinkCSpy.tar.gz thinkCSpy

clean:
	rm -f *~ *.aux *.log *.idx *.ilg *.ind *.toc *.lore *.ps



