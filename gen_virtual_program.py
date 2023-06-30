#!/usr/bin/env python3.8

import json
import re
from sys import argv
from pathlib import Path
from typing import Match, Pattern
from itertools import zip_longest

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

    matched_papers: list[Paper] = [title_lookup[m[1].lower().strip()] for m in matches]
    long_: list[Paper] = [p for p in matched_papers if not p.short]
    short_: list[Paper] = [p for p in matched_papers if p.short]

    print(">>> Long sorted papers")
    for p_ in sorted(long_, key=lambda p: p.id):
        print(f"* {p_.title}")
    print(">>> Short sorted papers")
    for p_ in sorted(short_, key=lambda p: p.id):
        print(f"* {p_.title}")

    # print(sorted(short_, key=lambda p: p.id))

    print(len(matches))
    # print(matches)
    first = True
    header: str = "|:-:|:-:|\n"
    for m1, m2 in zip_longest(matches[::2], matches[1::2]):
        # id = m[1][2:-2]
        # int_id: int = int(m[1])
        # print(m[0], int_id)
        # print(papers[int_id])

        content: str

        p1: Paper = title_lookup[m1[1].lower().strip()]
        p2: Paper = title_lookup[m2[1].lower().strip()] if m2 else p1

        content = f'''| ![{p1.conf_id}](/virtual/thumbnail/{p1.conf_id}.jpg) | ![{p2.conf_id}](/virtual/thumbnail/{p2.conf_id}.jpg) |
{header if first else ""}| [{p1.conf_id} - {p1.title}](papers/{p1.conf_id}.html) | [{p2.conf_id} - {p2.title}](papers/{p2.conf_id}.html)  |
| <hr> | <hr> |
'''
        first = False
        filled = filled.replace(f"{m1[0]}\n{m2[0]}\n", content)

    with open(dest_path, 'w') as sink:
        sink.write(filled)
