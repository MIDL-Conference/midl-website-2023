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

    papers: list[Paper] = [Paper(**v) for (k, v) in raw_papers.items()]

    title_lookup: dict[str, Paper] = {p.title.lower().strip(): p for p in papers}

    # for p in ["P015", "S016", "S023", "S027", "O029", "S030", "P032", "S044", "S045", "P046", "S055", "S067", "P070", "P076", "S082", "P082", "S087", "S098", "S101", "S112", "S114", "S120", "S121", "S123", "P129", "P138", "P139", "P166", "O179", "P187", "P189", "P199", "P200", "P201", "P215", "S050", "P009", "S110", "S117", "P090", "S073", "S093", "P218"]:
    #     print(f"* {p=} {raw_papers[p]['title']}")

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
        match_title: str = m[1].lower().strip()
        content: str

        if match_title.lower().strip() in title_lookup:
            content = str(title_lookup[match_title.lower().strip()])
        else:
            print(f"NOT FOUND: {match_title}")
            content = match_title

        filled = filled.replace(m[0], content)

    with open(dest_path, 'w') as sink:
        sink.write(filled)
