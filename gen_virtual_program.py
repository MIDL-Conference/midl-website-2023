#!/usr/bin/env python3.8

import json
import re
from pprint import pprint
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

    dest_path: Path = Path(argv[3])

    raw_papers: dict[str, dict]
    with open(papers_path, 'r') as pf:
        raw_papers = json.load(pf)

    # for key in ["P010", "P031", "P075", "P115", "P217", "P218", "P048", "P083", "P165", "P073"]:
    # for key in ["S085", "S110", "S069"]:
    #     print(f"* {raw_papers[key]['title']}")

    papers: list[Paper] = [Paper(**v) for (k, v) in raw_papers.items()]

    title_lookup: dict[str, Paper] = {p.title.lower().strip(): p for p in papers}

    template: str
    with open(template_path, 'r') as f:
        template = f.read()
    filled = template[:]

    regexp: Pattern = re.compile("\* (.*)")
    matches: list[Match] = list(regexp.finditer(template))
    # pprint(matches)

    matched_papers: list[Paper] = [title_lookup[m[1].lower().strip()] for m in matches]
    long_: list[Paper] = [p for p in matched_papers if not p.short]
    short_: list[Paper] = [p for p in matched_papers if p.short]

    # print(">>> Long sorted papers")
    # for p_ in sorted(long_, key=lambda p: p.id):
    #     print(f"* {p_.title}")
    # print(">>> Short sorted papers")
    # for p_ in sorted(short_, key=lambda p: p.id):
    #     print(f"* {p_.title}")

    # print(len(matches))

    default_thumbnail: str = "/assets/logos/logo_gold.png"

    for m1, m2 in zip_longest(matches[::2], matches[1::2]):

        content: str

        p1: Paper = title_lookup[m1[1].lower().strip()]
        p2: Paper | None = title_lookup[m2[1].lower().strip()] if m2 else None

        content = ''

        t1: str = f"/virtual/thumbnail/{p1.conf_id}.jpg"
        if not Path("static/" + t1).exists():
            print(Path("static/" + t1))
            t1 = default_thumbnail[:]

        content += f'| ![{p1.conf_id}]({t1}) |'
        if p2:
            t2: str = f"/virtual/thumbnail/{p2.conf_id}.jpg"
            if not Path("static/" + t2).exists():
                print(Path("static/" + t2))
                t2 = default_thumbnail[:]
            content += f'![{p2.conf_id}]({t2}) |\n'
        else:
            content += '|\n'

        content += f'| [{p1.conf_id} - {p1.title}](papers/{p1.conf_id}.html) |'
        if p2:
            content += f'[{p2.conf_id} - {p2.title}](papers/{p2.conf_id}.html)  |\n'
        else:
            content += '|\n'

        content += '| <hr> | <hr> |\n'

        to_replace: str = f"{m1[0]}\n{m2[0]}\n" if m2 else f"{m1[0]}\n"

        filled = filled.replace(to_replace, content)

    with open(dest_path, 'w') as sink:
        sink.write(filled)
