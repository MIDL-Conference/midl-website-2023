#!/usr/bin/env python3.8

import json
import re
from sys import argv
from pathlib import Path
from typing import Match, Pattern

from paper import Paper


if __name__ == "__main__":
    assert len(argv) == 4

    template_path: Path = Path(argv[1])
    assert template_path.exists()

    papers_path: Path = Path(argv[2])
    assert papers_path.exists()

    # mode: str = argv[3]
    # assert mode in ["short", "full"]

    dest_path: Path = Path(argv[3])

    raw_papers: dict[str, dict]
    with open(papers_path, 'r') as pf:
        raw_papers = json.load(pf)

    papers: list[Paper] = [Paper(ignore_schedule=True, **v) for (k, v) in raw_papers.items()]

    title_lookup: dict[str, Paper] = {p.title.lower(): p for p in papers}

    template: str
    with open(template_path, 'r') as f:
        template = f.read()
    filled = template[:]

    regexp: Pattern = re.compile("\* (.*)")
    matches: list[Match] = list(regexp.finditer(template))

    print(len(matches))
    # print(matches)
    for m in matches:
        # id = m[1][2:-2]
        # int_id: int = int(m[1])
        # print(m[0], int_id)
        # print(papers[int_id])
        match_title: str = m[1]
        content: str

        if match_title.lower() in title_lookup:
            content = str(title_lookup[match_title.lower()])
        else:
            print(f"NOT FOUND: {match_title}")
            content = match_title

        filled = filled.replace(m[0], content)

    with open(dest_path, 'w') as sink:
        sink.write(filled)
