---
title: "Camera Ready Instructions"
---
# Camera Ready Instructions for Full Papers (short paper instructions coming soon)

Dear authors, congratulations again for your accepted papers at MIDL 2023.

Please read the items below carefully and follow the instructions, as they are required for the publication of your paper in the conference proceedings.

Once your final material is prepared according to the detailed instructions below, please **upload and update on OpenReview by April 30th** (by clicking the `Revision` button) the following fields:

<center>

| Item | Field |
|:------|-------|
| LaTeX sources | `LaTeX Source` (in a single .zip) |
| PMLR copyright form | `LaTeX Source` (in a single .zip) |
| Camera ready PDF | `PDF` |
| Title | `Title` |
| Authors | `Authors` |
| Keywords | `Keywords` |
| Abstract | `Abstract` |

</center>


## Detailed Instructions

Three different items need to be prepared for upload in OpenReview:

1. your LaTeX file;

1. the PMLR copyright form;

1. PDF of the camera ready version.


### LaTeX submission
Prepare your camera ready using the **latest** version of the LaTeX MIDL template (`midl-fullpaper`):  [https://github.com/MIDL-Conference/MIDLLatexTemplate](https://github.com/MIDL-Conference/MIDLLatexTemplate)

Please make sure your are **not:**

- overriding the options of the `hyperref` package (loaded automatically);
- using the `times` package (if that was the case, please [contact the program chairs](mailto:pc@2023.midl.io) as soon as possible);
- overriding the bibligraphystyle (defined in `midl.cls`).

After making sure that your project compiles correctly with the standard `pdflatex` compiler, please include all the following items in a single zip folder LaTeX project:

1. The main LaTex file, which should be named `midl23_NNN.tex`, where `NNN` represents the submission OpenReview ID (e.g. 638).

1. The bibliography should be in a single `.bib` file and named `midl23_NNN.bib` with the same convention as above.

1. Within the `midl23_NNN.tex` tex file, the document class should be: `\documentclass{midl}` (without the `anon` option), and make sure that all authors and co-authors are listed correctly.

1. You should also set the following variables before the `\title` command: `\jmlryear{2023}\jmlrworkshop{Full Paper -- MIDL 2023}\jmlrvolume{-- nnn}\editors{Accepted for publication at MIDL 2023}`

1. The bibliography should be included in the paper using the following command: `\bibliography{midl23_NNN}`

1. Please do NOT use the `\begin{thebibliography}` environment.

1. For the camera ready, the page limit is increased from 8 pages to 9 pages, mostly to provide enough space to list all authors. Acknowledgements, references and appendix do not count toward that limit, and can appear on pages 10+.

1. Please be sure to check the author/institution list on the title page is de-anonymized, as well as any previously anonymized citations, github repos, data sources, acknowledgements, and other places.

1. If you used formatting changes (different colored font, etc.) during the rebuttal phase, please remove these formatting changes in the final version of your paper.

1. Please include the appendix and supplementary material in the camera-ready version.

1. Include all the necessary figures and files in the zip folder.


### PMLR copyright form
MIDL papers are published in the [PMLR proceedings](https://proceedings.mlr.press/). As such, it is required to **fill out and sign the PMLR Publication Agreement** ([http://proceedings.mlr.press/pmlr-license-agreement.pdf](http://proceedings.mlr.press/pmlr-license-agreement.pdf)) and add it in PDF format to the zip folder as part of your LaTeX project.


### Camera ready PDF for OpenReview

You also need to submit the final paper in PDF format in OpenReview using the `Revision` button and the `PDF` field by April 30th.
