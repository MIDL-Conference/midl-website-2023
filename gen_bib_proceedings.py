#!/usr/bin/env python3.11

import json
from sys import argv
from pathlib import Path
from operator import attrgetter

from pybtex.database import BibliographyData, Entry

from paper import Paper


if __name__ == "__main__":
        assert len(argv) == 3

        papers_path: Path = Path(argv[1])

        dest_path: Path = Path(argv[2])

        raw_papers: dict[str, dict]
        with open(papers_path, 'r') as pf:
                raw_papers = json.load(pf)

        papers: dict[str, Paper] = {k: Paper(**v) for (k, v) in raw_papers.items()}

        entries: dict[str, Entry] = {}
        paper: Paper
        for paper in papers.values():
                if paper.short or paper.melba:
                        continue
                
                # entry_id: str = f"{paper.first_author}2023{paper.title,.split(' ')[0]}".lower()
                old_id: str = f"midl23_{paper.id:03d}".lower()
                new_id_root: str = f"{paper.first_author}2023".lower()
                new_id: str

                for chr_code in range(ord('a'), ord('z')):
                        letter: str = chr(chr_code)
                        new_id = new_id_root + letter

                        if new_id not in entries:
                                break

                # print(f"git mv {old_id} {new_id}")
                print(f"git mv {new_id}/{old_id}.bib {new_id}/{new_id}.bib")
                # print(f"rm {new_id}/{old_id}.pdf")
                # print(new_id)

                entries[new_id] = Entry('InProceedings',
                                        [('author', ' and '.join(paper.authors)),
                                         ('title', paper.title),
                                         ('abstract', paper.sanitized_abstract)])

        bibdata = BibliographyData(entries)
        bibdata.to_file(dest_path)
