CC = python3
CFLAGS = -m mwb

.PHONY: pages/papers

DEBUG =

TARGET = /usr/share/nginx/midl2023

$(TARGET): FORCE
	rm -rf $@
	$(CC) $(CFLAGS) . $@ $(DEBUG)
# 	chmod -R +x $@

papers.json: full_papers.csv short_papers.csv midl_oral_sessions.csv
	$(CC) csv2json.py

pages/papers: pages/papers/paper.template papers.json
	$(CC) generate_papers.py $^ $(@D)

pages/scientific-program.md: pages/program.md papers.json
	$(CC) gen_scientific_program.py $^ $@


FORCE: