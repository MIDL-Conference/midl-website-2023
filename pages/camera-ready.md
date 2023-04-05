---
title: "Camera Ready Instructions"
---
# Camera Ready Instructions

Dear authors, congratulations again for your accepted papers at MIDL 2023.

Please read the items below carefully and follow the instructions, as they are required for the publication of your paper in the conference proceedings.

Once your final material is prepared according to the detailed instructions below, please **upload and update on OpenReview by April 30th** (by clicking the `Camera ready revision` button) the following fields:

<center>

| Item | Field |
|:------|-------|
| Latex sources | `Supplementary material` (in a single .zip) |
| PMLR copyright form | `Supplementary material` (in a single .zip) |
| Camera ready PDF | `PDF` |
| Title | `Title` |
| Authors | `Authors` |
| Keywords | `Keywords` |
| Abstract | `Abstract` |

</center>


## Detailed Instructions

Three different items need to be prepared for upload in OpenReview:

1. your LaTex file;

1. the PMLR copyright form;

1. pdf of the camera ready version.


### LaTex submission
Prepare your camera ready using the **latest** version of the LaTex MIDL template (`midl-fullpaper`):  [https://github.com/MIDL-Conference/MIDLLatexTemplate](https://github.com/MIDL-Conference/MIDLLatexTemplate)

**Please make sure your are not:**

- overriding the options of the `hyperref` package (loaded automatically);
- using the `times` package (if that was the case, please contact the program chairs as soon as possible);
- overriding the bibligraphystyle (defined in `midl.cls`).

After making sure that your project compiles correctly with the standard `pdflatex` compiler, please include all the following items in a single zip folder latex project:

1. The main LaTex file, which should be named `midl23_NNN.tex`, where `NNN` represents the submission OpenReview ID (e.g. 638).

1. The bibliography should be in a single `.bib` file and named `midl23_NNN.bib` with the same convention as above.

1. Within the `midl23_NNN.tex` tex file, the document class should be: `\documentclass{midl}`

1. You should also set the following variables before the `\title` command: `\jmlryear{2023}\jmlrworkshop{Full Paper -- MIDL 2023}\jmlrvolume{-- nnn}\editors{Accepted for publication at MIDL 2023}`

1. The bibliography should be included in the paper using the following command: `\bibliography{midl23_NNN}`

1. Please do NOT use the `\begin{thebibliography}` environment.

1. Please ensure that your paper does not exceed the 8 page limit.

1. Please include the appendix and supplementary material in the camera-ready version.

1. Include all the necessary figures and files in the zip folder.


### PMLR copyright form
MIDL papers are published in the [PMLR proceedings](https://proceedings.mlr.press/). As such, it is required to **fill out and sign the PMLR Publication Agreement** ([http://proceedings.mlr.press/pmlr-license-agreement.pdf](http://proceedings.mlr.press/pmlr-license-agreement.pdf)) and add it in PDF format to the zip folder as part of your LaTeX project.


### Camera ready PDF for OpenReview

You also need to submit the final paper in PDF format in OpenReview using the `Camera Ready Revision` button and the `PDF` field by March 30th.
