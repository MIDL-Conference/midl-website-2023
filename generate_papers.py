#!/usr/bin/env python3.11

import json
from sys import argv
from pathlib import Path
from operator import attrgetter

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

    papers: dict[str, Paper] = {k: Paper(**v) for (k, v) in raw_papers.items()}

    with open(template_path, 'r') as f:
        empty_template: str = f.read()

    root_slides: Path = Path("static")

    paper: Paper
    for paper in papers.values():
        result: str = empty_template[:]

        result = result.replace("CONF_ID", paper.conf_id)
        result = result.replace("SMALLID", paper.conf_id.casefold())
        result = result.replace("TITLE", paper.title)
        result = result.replace("AUTHORS", ", ".join(paper.authors))
        result = result.replace("ORID", paper.or_id)
        result = result.replace("ABSTRACT", paper.sanitized_abstract)
        result = result.replace("SCHEDULE", "<br>".join(paper.schedule))
        result = result.replace("__POSTERLOC__", paper.poster_loc)

        if paper.award:
            result = result.replace("AWARD", f"## {paper.award}")
        else:
            result = result.replace("AWARD", "")

        # slides_path: Path = Path(paper.slides)

        yt_link = paper.yt_full

        if yt_link and (root_slides / paper.slides[1:]).exists():
            result = result.replace("PRESENTATION", f"{{{{ presentation('{yt_link.split('/')[-1]}', '{paper.slides}', 720, 450) }}}}")
        if yt_link:
            result = result.replace("PRESENTATION", f"{{{{ youtube('{yt_link.split('/')[-1]}') }}}}")
        else:
            result = result.replace("PRESENTATION", "")

        oral_text: str
        if paper.oral:
            oral_text = "Oral presentation"
        elif paper.poster:
            oral_text = "Poster presentation"
        elif paper.short:
            oral_text = "Short paper"

        result = result.replace("ORAL", oral_text)

        with open((dest_path / Path(paper.url)).with_suffix(".md"), 'w') as sink:
            sink.write(result)
