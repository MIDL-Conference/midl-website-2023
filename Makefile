CC = python3
CFLAGS = -m mwb

.PHONY: all pages/papers

DEBUG =

TARGET = /usr/share/nginx/midl2023

$(TARGET): FORCE
	rm -rf $@
	$(CC) $(CFLAGS) . $@ $(DEBUG)
# 	chmod -R +x $@

all: papers.json pages/papers pages/program.md pages/virtual_event.md $(TARGET)

papers.json: full_papers.csv short_papers.csv midl_oral_sessions.csv
	$(CC) csv2json.py

pages/papers: pages/papers/paper.template papers.json
	$(CC) generate_papers.py $^ $(@D)

pages/program.md: pages/program.txt papers.json
	$(CC) gen_scientific_program.py $^ $@

pages/virtual_event.md: pages/virtual_event.txt papers.json
	$(CC) gen_virtual_program.py $^ $@


FORCE: