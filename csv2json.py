#!/usr/bin/env python3.10

import json
import pandas as pd
from pathlib import Path
from typing import Final
from pprint import pprint

from paper import Paper, PaperEncoder

ORAL_SESSIONS: Final[list[str]] = ["(midl board session)", "Computer-assisted diagnosis", "Graph-based methods",
                                   "Neuroimaging", "Segmentation 1", "Segmentation 2",
                                   "Semi-supervised/self-supervised methods", "Synthesis",
                                   "Unsupervised/Weakly supervised methods"]

if __name__ == "__main__":
        papers: list[Paper] = []

        midl_orals_df = pd.read_csv("midl_oral_sessions.csv")

        session_map: dict[str, str] = {}
        for index, row in midl_orals_df.iterrows():
                session_map[row["title"]] = row["session"]

        # pprint(session_map)
        assert set(session_map.values()) == set(ORAL_SESSIONS)
        print(f">>> Loaded {len(set(session_map.values()))} sessions")

        full_papers_df = pd.read_csv("full_papers.csv")

        title: str
        for _, full_row in full_papers_df.iterrows():
                title = full_row["title"]
                is_oral = title in session_map

                paper = Paper(id=full_row["number"], title=title, authors=full_row["authors"],
                              or_id=full_row["forum"].split('=')[1], oral=str(is_oral),
                              short="False", abstract=full_row["abstract"], ignore_schedule=True)
                papers.append(paper)

        print(f">>> Loaded {len(full_papers_df)} full papers")

        short_papers_df = pd.read_csv("short_papers.csv")
        for _, short_row in short_papers_df.iterrows():
                title = short_row["title"]
                # print(short_row)

                paper = Paper(id=short_row["number"], title=title, authors=short_row["authors"],
                              or_id=short_row["forum"].split('=')[1], oral="False",
                              short="True", abstract=short_row["abstract"], ignore_schedule=True)
                papers.append(paper)

        print(f">>> Loaded {len(short_papers_df)} short papers")

        paper_dict: dict[str, Paper] = {p.conf_id: p for p in papers}
        json_dict: dict = json.loads(json.dumps(paper_dict, cls=PaperEncoder, indent=4, sort_keys=True))
        print(">>> First conversion to json")

        patch_file: str = "patch.json"
        with open(patch_file, 'r') as pf:
                patch: dict = json.load(pf)

        print(">>> Patching")
        pprint(patch)

        for p in patch:
                json_dict[p] |= patch[p]
        # Go back and forth, because some conf_id might have changed due to the patch, bit messy
        # (for instance, orals that are downgrade to posters)
        json_dict = json.loads(json.dumps({p.conf_id: p for p in [Paper(**v, ignore_schedule=True)
                                                                  for v in json_dict.values()]},
                                          cls=PaperEncoder,
                                          indent=4,
                                          sort_keys=True))

        print(f">> Patched json with {patch_file}")

        with open("melba.json", 'r') as melba:
                melba_json = json.load(melba)

        for mp in melba_json:
                id_: int = int(mp['melba_id'].split(':')[1])
                authors_: str = ", ".join(a.split('#')[0] for a in mp['authors'])
                json_dict[f"M{id_:03d}"] = {'abstract': mp['abstract'],
                                            'authors': authors_,
                                            'award': None,
                                            'id': id_,
                                            'or_id': "",
                                            'oral': "False",
                                            'pmlr_url': "",
                                            'schedule': "",
                                            'short': "False",
                                            'melba': "True",
                                            'title': mp['title']}
        print(f">>> Loaded {len(melba_json)} for melba to journal to conf")

        title_dict: dict[str, str] = {json_dict[pid]["title"].strip().lower(): pid for pid in json_dict}
        with open("pages/program.txt", 'r') as program:
                current_day: str = ""
                current_time: str = ""
                cur_title: str
                for line in program:
                        if line.startswith("## "):
                                current_day = line[3:-1]
                        elif line.startswith("### "):
                                current_time = line[4:]
                        elif line.startswith("* "):
                                cur_title = line[2:].strip().lower()
                                json_dict[title_dict[cur_title]]["schedule"] += f"{current_day}: {current_time}"

        print(">>> Adding virtual information")
        midl_virtual_df = pd.read_csv("virtual_papers.csv")
        for _, row in midl_virtual_df.iterrows():
                # print(row["Paper #"], row["Video link"])
                if str(row["Video link"]) != "nan":
                        json_dict[row["Paper #"]]["yt_full"] = row["Video link"]
        for pdf_ in Path("static/virtual/poster").glob("*.pdf"):
                json_dict[pdf_.stem]["slides"] = str(pdf_).replace("static", "")

        print(f">>> Writing {len(papers)} to papers.json...")
        with open("papers.json", 'w') as sink:
                json.dump(json_dict, sink, indent=4, sort_keys=True)

        # print(full_papers_csv)
