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
                if paper.short:
                        continue
                
                entry_id: str = f"{paper.first_author}2023{paper.title.split(' ')[0]}".lower()

                entries[entry_id] = Entry('InProceedings',
                                          [('title', paper.title),
                                           ('author', ' and '.join(paper.authors)),
                                           ('abstract', paper.sanitized_abstract)])

        bibdata = BibliographyData(entries)
        bibdata.to_file(dest_path)
