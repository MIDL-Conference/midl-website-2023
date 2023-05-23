#!/usr/bin/env python3.10

import json
import pandas as pd
from typing import Final
from pprint import pprint

from paper import Paper, PaperEncoder

ORAL_SESSIONS: Final[list[str]] = ["(midl board session)", "Computer-assisted diagnosis", "Graph-based methods",
                                   "Neuroimaging", "Segmentation 1", "Segmentation 2",
                                   "Semi-supervised/self-supervised methods", "Synthesis",
                                   "Unsupervised/Weakly supervised methods"]

if __name__ == "__main__":
        midl_orals_df = pd.read_csv("midl_oral_sessions.csv")

        session_map: dict[str, str] = {}
        for index, row in midl_orals_df.iterrows():
                session_map[row["title"]] = row["session"]

        pprint(session_map)

        assert set(session_map.values()) == set(ORAL_SESSIONS)

        full_papers_df = pd.read_csv("full_papers.csv")

        papers: list[Paper] = []

        for _, full_row in full_papers_df.iterrows():
                title: str = full_row["title"]
                is_oral = title in session_map

                schedule: str = session_map[title] if is_oral else ""

                paper = Paper(id=full_row["number"], title=title, authors=full_row["authors"],
                              or_id=full_row["forum"].split('=')[1], oral=str(is_oral),
                              short="False", abstract=full_row["abstract"], ignore_schedule=True)
                papers.append(paper)

        with open("papers.json", 'w') as sink:
                json.dump({p.id: p for p in papers}, sink, cls=PaperEncoder, indent=4, sort_keys=True)

        # print(full_papers_csv)
