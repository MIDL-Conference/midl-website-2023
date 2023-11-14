---
 title: "Awards"
---
 
{% from "_macros.html" import paper %}

# Awards

## Best poster award

[% .papers %]
{{ paper('Local and global feature aggregation for accurate epithelial cell classification using graph attention mechanisms in histopathology images',
         'Ana Leni Frei, Amjad Khan, Linda Studer, Philipp Zens, Alessandro Lugli, Andreas Fischer, Inti Zlobec',
         openreview='https://openreview.net/forum?id=HlkroJOY-J',
         pdf='https://openreview.net/pdf?id=HlkroJOY-J',
         id='S036',
         paper='papers/S036.html',
         abstract="In digital pathology, cell-level tissue analyses are widely used to better understand tissue composition and structure. Publicly available datasets and models for cell detection and classification in colorectal cancer exist but lack the differentiation of normal and malignant epithelial cells that are important to perform prior to any downstream cell-based analysis. This classification task is particularly difficult due to the high intra-class variability of neoplastic cells. To tackle this, we present here a new method that uses graph-based node classification to take advantage of both local cell features and global tissue architecture to perform accurate epithelial cell classification. The proposed method  demonstrated excellent performance on F1 score (PanNuke: 1.0, TCGA: 0.98) and performed significantly better than conventional computer vision methods (PanNuke: 0. 99, TCGA: 0.92).")
}}
[% / %]

## Runner-up for best poster award


[% .papers %]
{{ paper('Calibration techniques for node classification using graph neural networks on medical image data',
         'Iris Vos, Ishaan Bhat, Birgitta Velthuis, Ynte Ruigrok, Hugo Kuijf',
         openreview='https://openreview.net/forum?id=xY3agyj5Eq',
         pdf='https://openreview.net/pdf?id=xY3agyj5Eq',
         id='P126',
         paper='papers/P126.html',
         abstract="Miscalibration of deep neural networks (DNNs) can lead to unreliable predictions and hinder their use in clinical decision-making. This miscalibration is  often caused by overconfident probability estimates. Calibration techniques such as   model ensembles, regularization terms, and post-hoc scaling of the predictions can be employed to improve the calibration performance of DNNs. In contrast to DNNs, graph neural networks (GNNs) tend to exhibit underconfidence. In this study, we investigate the efficacy of calibration techniques developed for DNNs when applied to GNNs trained on medical image data, and compare the calibration performance of binary and multiclass node classification on a benchmark dataset and a medical image dataset. We find that post-hoc methods using Platt scaling or Temperature scaling, or methods that add a regularization term to the loss function during training are most effective to improve calibration. Our results further indicate that these calibration techniques are more effective for multiclass classification tasks compared to binary classification tasks.")
}}
[% / %]

## Best oral award


[% .papers %]
{{ paper('Data Consistent Deep Rigid MRI Motion Correction',
         'Nalini M Singh, Neel Dey, Malte Hoffmann, Bruce Fischl, Elfar Adalsteinsson, Robert Frost, Adrian V Dalca, Polina Golland',
         openreview='https://openreview.net/forum?id=KolMbwNBNGv',
         pdf='https://openreview.net/pdf?id=KolMbwNBNGv',
         id='O177',
         paper='papers/O177.html',
         abstract="Motion artifacts are a pervasive problem in MRI, leading to misdiagnosis or mischaracterization in population-level imaging studies. Current retrospective rigid intra-slice motion correction techniques jointly optimize estimates of the image and the motion parameters. In this paper, we use a deep network to reduce the joint image-motion parameter search to a search over rigid motion parameters alone. Our network produces a reconstruction as a function of two inputs: corrupted k-space data and motion parameters. We train the network using simulated, motion-corrupted k-space data generated from known motion parameters. At test-time, we estimate unknown motion parameters by minimizing a data consistency loss between the motion parameters, the network-based image reconstruction given those parameters, and the acquired measurements. Intra-slice motion correction experiments on simulated and realistic 2D fast spin echo brain MRI achieve high reconstruction fidelity while retaining the benefits of explicit data consistency-based optimization.")
}}
[% / %]


## Runner-up for best oral award


[% .papers %]
{{ paper('Decoding natural image stimuli from fMRI data with a surface-based convolutional network',
         'Zijin Gu, Keith Jamison, Amy Kuceyeski, Mert R. Sabuncu',
         openreview='https://openreview.net/forum?id=V5vvti2Y9PA',
         pdf='https://openreview.net/pdf?id=V5vvti2Y9PA',
         id='O037',
         paper='papers/O037.html',
         abstract="Due to the low signal-to-noise ratio and limited resolution of functional MRI data, and the high complexity of natural images, reconstructing a visual stimulus from human brain fMRI measurements is a challenging task. In this work, we propose a novel approach for this task, which we call Cortex2Image, to decode visual stimuli with high semantic fidelity and rich fine-grained detail. In particular, we train a surface-based convolutional network model that maps from brain response to semantic image features first (Cortex2Semantic). We then combine this model with a high-quality image generator (Instance-Conditioned GAN) to train another mapping from brain response to fine-grained image features using a variational approach (Cortex2Detail). Image reconstructions obtained by our proposed method achieve state-of-the-art semantic fidelity, while yielding good fine-grained similarity with the ground-truth stimulus. Our code is available on url{https://github.com/zijin-gu/meshconv-decoding.git} .") 
}}
[% / %]


---


### Best reviewer

* Hoel Kervadec - 11 papers total(6 full + 5 short)

### Best area chair

* Yuankai Huo - 9 papers(2 full + 7 short)

