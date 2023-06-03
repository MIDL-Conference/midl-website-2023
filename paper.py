#!/usr/bin/env python3.11

import json
from typing import List


class Paper():
    def __init__(self, id: str, title: str, authors: str, or_id: str, oral: str, short: str,
                 abstract: str, schedule: str = "", ignore_schedule: bool = False,
                 award: str = "", pmlr_url=""):
        self.id: int = int(id)
        self.title: str = title
        self.authors: List[str] = authors.split('|')
        self.or_id: str = or_id
        self.oral: bool = oral == "True"
        self.short: bool = short == "True"
        self.poster: bool = (not self.short) and (not self.oral)
        self.abstract: str = abstract
        # self.slides: str = slides
        # self.yt_teaser: str = yt_teaser
        # self.yt_full: str = yt_full
        self.award: str = award

        self.pmlr_url: str = pmlr_url
        assert not (self.short and self.pmlr_url)

        self.pdf_url: str
        if self.short:
            self.pdf_url = f'https://openreview.net/pdf?id={self.or_id}'
        else:
            pmlr_id: str = self.pmlr_url.split('/')[-1].replace(".html", "")
            self.pdf_url = f"http://proceedings.mlr.press/v121/{pmlr_id}/{pmlr_id}.pdf"

        self.schedule: List[str]
        if not schedule:
            self.schedule = []
        else:
            self.schedule = schedule.split('\n')

        assert not (self.oral and self.short)
        if self.short:
            assert not self.oral

        if not ignore_schedule:
            try:
                if not self.oral:
                    assert len(self.schedule) == 1
                else:
                    assert len(self.schedule) == 2
            except AssertionError:
                print(self.id, self.schedule)

        sanitized_abstract: str = self.abstract.replace("'", "\\'")
        sanitized_abstract = sanitized_abstract.replace('"', '\\"')
        sanitized_abstract = sanitized_abstract.replace('\n', '')
        sanitized_abstract = sanitized_abstract.replace('`', '')
        self.sanitized_abstract = sanitized_abstract

        self.conf_sign: str = "O" if self.oral else ("S" if self.short else "P")

        self.conf_id: str = f"{self.conf_sign}{self.id:03d}"
        self.url: str = f"papers/{self.conf_id}"

        # self.__class__.__name__: str = "Paper"

    def __str__(self) -> str:
        sanitized_abstract: str = self.abstract.replace("'", "\\'")
        sanitized_abstract = sanitized_abstract.replace('"', '\\"')
        sanitized_abstract = sanitized_abstract.replace('\n', '')
        sanitized_abstract = sanitized_abstract.replace('`', '')
        sanitized_abstract = repr(sanitized_abstract)
        # sanitized_abstract: str = repr(self.abstract)

        sanitized_authors: list[str] = [a.replace("'", "\\'") for a in self.authors]
        sanitized_title: str = self.title.replace("'", "\\'")

        return f'''{{{{ paper(\'{sanitized_title}\',
        \'{f'{", ".join(sanitized_authors)}'}\',
        openreview=\'{f'https://openreview.net/forum?id={self.or_id}'}\',
        pdf=\'{self.pdf_url}\',
        id='{self.conf_id}',
        paper='{self.url}',
        proceedings='{self.pmlr_url}',
        abstract={sanitized_abstract})
}}}}'''


class PaperEncoder(json.JSONEncoder):
    def default(self, paper):
        if isinstance(paper, Paper):
            return {"id": str(paper.id),
                    "title": paper.title,
                    "authors": ", ".join(paper.authors),
                    "or_id": paper.or_id,
                    "oral": str(paper.oral),
                    "short": str(paper.short),
                    "abstract": paper.abstract,
                    "schedule": "\n".join(paper.schedule),
                    "award": paper.award,
                    "pmlr_url": paper.pmlr_url}

        return json.JSONEncoder.default(self, paper)
