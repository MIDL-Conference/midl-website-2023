---
title: "Detailed program - coming soon!"
---

{% from "_macros.html" import button, paper %}

Please note the program is tentative. Please note the assignment of short papers to the poster sessions is coming soon; the below program only has papers from the full paper track.

# Monday, July 10

## Oral session 1 - Segmentation 1 - 9:30 - 10:30am

[% .papers %]
{{ paper('MS-Former: Multi-Scale Self-Guided Transformer for Medical Image Segmentation',
        'Sanaz Karimijafarbigloo, Reza Azad, Amirhossein Kazerouni, Dorit Merhof',
        openreview='https://openreview.net/forum?id=pp2raGSU3Wx',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O031',
        paper='papers/O031',
        proceedings='',
        abstract='Multi-scale representations have proven to be a powerful tool since they can take into account both the fine-grained details of objects in an image as well as the broader context. Inspired by this, we propose a novel dual-branch transformer network that operates on two different scales to encode global contextual dependencies while preserving local information. To learn in a self-supervised fashion, our approach considers the semantic dependency that exists between different scales to generate a supervisory signal for inter-scale consistency and also imposes a spatial stability loss within the scale for self-supervised content clustering. While intra-scale and inter-scale consistency losses aim to increase features similarly within the cluster, we propose to include a cross-entropy loss function on top of the clustering score map to effectively model each cluster distribution and increase the decision boundary between clusters. Iteratively our algorithm learns to assign each pixel to a semantically related cluster to produce the segmentation map. Extensive experiments on skin lesion and lung segmentation datasets show the superiority of our method compared to the state-of-the-art (SOTA) approaches. ')
}}
{{ paper('SuperMask: Generating High-resolution object masks from multi-view, unaligned low-resolution MRIs',
        'Hanxue Gu, Hongyu He, Roy Colglazier, Jordan Axelrod, Robert French, Maciej A Mazurowski',
        openreview='https://openreview.net/forum?id=oi5psB9R_l',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O039',
        paper='papers/O039',
        proceedings='',
        abstract='Three-dimensional segmentation in magnetic resonance images (MRI), which reflects the true shape of the objects, is challenging since high-resolution isotropic MRIs are rare and typical MRIs are anisotropic, with the out-of-plane dimension having a much lower resolution. A potential remedy to this issue lies in the fact that often multiple sequences are acquired on different planes. However, in practice, these sequences are not orthogonal to each other, limiting the applicability of many previous solutions to reconstruct higher-resolution images from multiple lower-resolution ones. We propose a novel deep learning-based solution to generating high-resolution masks from multiple low-resolution images. Our method combines segmentation and unsupervised registration networks by introducing two new regularizations to make registration and segmentation reinforce each other. Finally, we introduce a multi-view fusion method to generate high-resolution target object masks. The experimental results on two datasets show the superiority of our methods. Importantly, the advantage of not using high-resolution images in the training process makes our method applicable to a wide variety of MRI segmentation tasks.')
}}
{{ paper('Model Adaptive Tooth Segmentation',
        'Ruizhe Chen, Jianfei Yang, YANG FENG, Jin Hao, Zuozhu Liu',
        openreview='https://openreview.net/forum?id=O2DerS5oQ1',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O048',
        paper='papers/O048',
        proceedings='',
        abstract='Automatic 3-dimensional tooth segmentation on intraoral scans (IOS) plays a pivotal role in computer-aided orthodontic treatments. In practice, deploying existing well-trained models to different medical centers suffers from two main problems: (1) the data distribution shifts between existing and new centers, (2) the data in the existing center is usually not allowed to share while annotating additional data in the new center is time-consuming and expensive. In this paper, we propose a Model Adaptive Tooth Segmentation (MATS) framework to alleviate these issues. Taking the trained model from a source center as input, MATS adapts it to different target centers without data transmission or additional annotations, as inspired by the source data-free domain adaptation (SFDA) paradigm. The model adaptation in MATS is realized by a tooth-level feature prototype learning module, a progressive pseudo-labeling module and a tooth-prior regularized information maximization loss. Experiments on a dataset with tooth abnormalities and a real-world cross-center dataset show that MATS can consistently surpass existing baselines. The effectiveness is further verified with extensive ablation studies and statistical analysis, demonstrating its applicability for privacy-preserving tooth segmentation in real-world digital dentistry. ')
}}
{{ paper('Learning Clinically Acceptable Segmentation of Organs at Risk in Cervical Cancer Radiation Treatment from Clinically Available Annotations',
        'Monika Grewal, Dustin van Weersel, Henrike Westerveld, Peter Bosman, Tanja Alderliesten',
        openreview='https://openreview.net/forum?id=uPRFWdz03_',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O100',
        paper='papers/O100',
        proceedings='',
        abstract='Deep learning models benefit from training with a large dataset (labeled or unlabeled). Following this motivation, we present an approach to learn a deep learning model for the automatic segmentation of Organs at Risk (OARs) in cervical cancer radiation treatment from a large clinically available dataset of Computed Tomography (CT) scans containing data inhomogeneity, label noise, and missing annotations. We employ simple heuristics for automatic data cleaning to minimize data inhomogeneity and label noise. Further, we develop a semi-supervised learning approach utilizing a teacher-student setup, annotation imputation, and uncertainty-guided training to learn in presence of missing annotations. Our experimental results show that learning from a large dataset with our approach yields a significant improvement in the test performance despite missing annotations in the data. Further, the contours generated from the segmentation masks predicted by our model are found to be equally clinically acceptable as manually generated contours.')
}}

## Oral session 2 - Unsupervised/weakly supervised methods - 2:00 - 3:00pm
[% .papers %]
{{ paper('Joint Breast Neoplasm Detection and Subtyping using Multi-Resolution Network Trained on Large-Scale H&E Whole Slide Images with Weak Labels',
        'Adam Casson, Siqi Liu, Ran A Godrich, Hamed Aghdam, Brandon Rothrock, Kasper Malfroid, Christopher Kanan, Thomas Fuchs',
        openreview='https://openreview.net/forum?id=rXVtHHFLRIz',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O007',
        paper='papers/O007',
        proceedings='',
        abstract='Breast cancer is the most commonly diagnosed cancer and the use of artificial intelligence (AI) to help diagnose the disease from digital pathology images has the potential to greatly improve patient outcomes. However, current methods for detecting, segmenting, and sub-typing breast neoplasms and other proliferative lesions often rely on costly and time-consuming manual annotation efforts, which can be impractical for large-scale datasets. In this work, we propose an annotation-free learning framework to jointly detect, segment, and subtype breast neoplasms. Our approach leverages top-k multiple instance learning to train an initial neoplasm detection backbone network from weakly-labeled whole slide images, which is then used to automatically generate pixel-level pseudo-labels for whole slides with only one subtype. A second network is trained using these pseudo-labels, and slide-level classification is performed by training an aggregator network that fuses the embeddings from both backbone networks. We trained and validated our framework on large-scale datasets with more than 100k whole slide images and demonstrate its effectiveness on tasks including breast neoplasms detection, segmentation, and subtyping.')
}}
{{ paper('Generalizing Unsupervised Anomaly Detection: Towards Unbiased Pathology Screening',
        'Cosmin I. Bercea, Benedikt Wiestler, Daniel Rueckert, Julia A Schnabel',
        openreview='https://openreview.net/forum?id=8ojx-Ld3yjR',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O021',
        paper='papers/O021',
        proceedings='',
        abstract='The main benefit of unsupervised anomaly detection is the ability to identify arbitrary, rare data instances of pathologies even in the absence of training labels or sufficient examples of the rare class(es). In the clinical workflow, such methods have the potential to assist in screening and pre-filtering exams for potential pathologies and thus meaningfully support radiologists. Even though much work has been done on using auto-encoders (AE) for anomaly detection, there are still two critical challenges to overcome: First, learning compact and detailed representations of the healthy distribution is cumbersome. Recent work shows that AEs can reconstruct some types of anomalies even better than actual samples from the training distribution. Second, while the majority of unsupervised algorithms are tailored to detect hyperintense lesions on FLAIR brain MR scans, recent improvements in basic intensity thresholding techniques have outperformed them.  Moreover, we found that even state-of-the-art (SOTA) AEs fail to detect several classes of non-hyperintense anomalies on T1w brain MRIs, such as brain atrophy, edema, or resections. In this work, we propose reversed AEs (RA) to generate pseudo-healthy reconstructions and localize various brain pathologies. We extensively evaluate our method on T1w brain scans and increase the detection of global pathology and artefacts from 73.1 to 89.4 AUROC and the amount of detected local pathologies from 52.6% to 86.0% compared to SOTA methods.')
}}
{{ paper('Unsupervised Stain Decomposition via Inversion Regulation for Multiplex Immunohistochemistry Images',
        'Shahira Abousamra, Danielle Fassler, Jiachen Yao, Rajarsi R. Gupta, Tahsin Kurc, Luisa Escobar-Hoyos, Dimitris Samaras, Kenneth Shroyer, Joel Saltz, Chao Chen',
        openreview='https://openreview.net/forum?id=J0VD-I2IOOg',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O026',
        paper='papers/O026',
        proceedings='',
        abstract='Multiplex Immunohistochemistry (mIHC) is a cost-effective and accessible method for in situ labeling of multiple protein biomarkers in a tissue sample. By assigning a different stain to each biomarker, it allows the visualization of different types of cells within the tumor vicinity for downstream analysis. However, to detect different types of stains in a given mIHC image is a challenging problem, especially when the number of stains is high. Previous deep-learning-based methods mostly assume full supervision; yet the annotation can be costly. In this paper, we propose a novel unsupervised stain decomposition method to detect different stains simultaneously. Our method does not require any supervision, except for color samples of different stains. A main technical challenge is that the problem is underdetermined and can have multiple solutions. To conquer this issue, we propose a novel inversion regulation technique, which eliminates most undesirable solutions. On a 7-plexed IHC image dataset, the proposed method achieves high quality stain decomposition results without human annotation.')
}}
{{ paper('DRIMET: Deep Registration-based 3D Incompressible Motion Estimation in Tagged-MRI with Application to the Tongue',
        'Zhangxing Bian, Fangxu Xing, Jinglun Yu, Muhan Shao, Yihao Liu, Aaron Carass, Jonghye Woo, Jerry L Prince',
        openreview='https://openreview.net/forum?id=jkSC4UHHVzy',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O047',
        paper='papers/O047',
        proceedings='',
        abstract='Tagged magnetic resonance imaging (MRI) has been used for decades to observe and quantify the detailed motion of deforming tissue. However, this technique faces several challenges such as tag fading, large motion, long computation times, and difficulties in obtaining diffeomorphic incompressible flow fields. To address these issues, this paper presents a novel unsupervised phase-based 3D motion estimation technique for tagged MRI. We introduce two key innovations. First, we apply a sinusoidal transformation to the harmonic phase input, which enables end-to-end training and avoids the need for phase interpolation. Second, we propose a Jacobian determinant-based learning objective to encourage incompressible flow fields for deforming biological tissues.  Our method efficiently estimates 3D motion fields that are accurate, dense, and approximately diffeomorphic and incompressible. The efficacy of the method is assessed using human tongue motion during speech, and includes both healthy controls and patients that have undergone glossectomy. We show that the method outperforms existing approaches, and also exhibits improvements in speed, robustness to tag fading, and large tongue motion. The code is available.')
}}

## Oral session 3 - Graph-based methods - 4:00 - 5:00pm
[% .papers %]
{{ paper('DBGDGM: Dynamic Brain Graph Deep Generative Model',
        'Alexander Campbell, Simeon Emilov Spasov, Nicola Toschi, Pietro Lio',
        openreview='https://openreview.net/forum?id=WHS3Zv9pxz',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O139',
        paper='papers/O139',
        proceedings='',
        abstract='Graphs are a natural representation of brain activity derived from functional magnetic imaging (fMRI) data. It is well known that clusters of anatomical brain regions, known as functional connectivity networks (FCNs), encode temporal relationships which can serve as useful biomarkers for understanding brain function and dysfunction. Previous works, however, ignore the temporal dynamics of the brain and focus on static graphs. In this paper, we propose a dynamic brain graph deep generative model (DBGDGM) which simultaneously clusters brain regions into temporally evolving communities and learns dynamic unsupervised node embeddings. Specifically, DBGDGM represents brain graph nodes as embeddings sampled from a distribution over communities that evolve over time. We parameterise this community distribution using neural networks that learn from subject and node embeddings as well as past community assignments. Experiments demonstrate DBGDGM outperforms baselines in graph generation, dynamic link prediction, and is comparable for graph classification. Finally, an analysis of the learnt community distributions reveals overlap with known FCNs reported in neuroscience literature.')
}}
{{ paper('Tumor Budding T-cell Graphs: Assessing the Need for Resection in pT1 Colorectal Cancer Patients',
        'Linda Studer, JM Bokhorst, I Nagtegaal, Inti Zlobec, Heather Dawson, Andreas Fischer',
        openreview='https://openreview.net/forum?id=ruaXPgZCk6i',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O088',
        paper='papers/O088',
        proceedings='',
        abstract='Colon resection is often the treatment of choice for colorectal cancer (CRC) patients. However, especially for minimally invasive cancer, such as pT1, simply removing the polyps may be enough to stop cancer progression. Different histopathological risk factors such as tumor grade and invasion depth currently found the basis for the need for colon resection in pT1 CRC patients. Here, we investigate two additional risk factors, tumor budding and lymphocyte infiltration at the invasive front, which are known to be clinically relevant. We capture the spatial layout of tumor buds and T-cells and use graph-based deep learning to investigate them as potential risk predictors. Our pT1 Hotspot Tumor Budding T-cell Graph (pT1-HBTG) dataset consists of 626 tumor budding hotspots from 575 patients. We propose and compare three different graph structures, as well as combinations of the node labels. The best-performing Graph Neural Network architecture is able to increase specificity by 20% compared to the currently recommended risk stratification based on histopathological risk factors, without losing any sensitivity. We believe that using a graph-based analysis can help to assist pathologists in making risk assessments for pT1 CRC patients, and thus decrease the number of patients undergoing potentially unnecessary surgery. Both the code and dataset are made publicly available.')
}}
{{ paper('A Geometric Deep Learning Framework for Generation of Virtual Left Ventricles as Graphs',
        'Soodeh Kalaie, Andrew J. Bulpitt, Alejandro F. Frangi, Ali Gooya',
        openreview='https://openreview.net/forum?id=Ao0D2HMB8P',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O216',
        paper='papers/O216',
        proceedings='',
        abstract='Generative statistical models have a wide range of applications in the modelling of anatomies. In-silico clinical trials of medical devices, for instance, require the development of virtual populations of anatomy that capture enough variability while remaining plausible. Model construction and use are heavily influenced by the correspondence problem and establishing shape matching over a large number of training data.This study focuses on generating virtual cohorts of left ventricle geometries resembling different-sized shape populations, suitable for in-silico experiments. We present an unsupervised data-driven probabilistic generative model for shapes. This framework incorporates an attention-based shape matching procedure using graph neural networks, coupled with a $\\beta-$VAE generation model, eliminating the need for initial shape correspondence. Left ventricle shapes derived from cardiac magnetic resonance images available in the UK Biobank are utilized for training and validating the framework. We investigate our method’s generative capabilities in terms of generalisation and specificity and show that it is able to synthesise virtual populations of realistic shapes with volumetric measurements in line with actual clinical indices. Moreover, results show our method outperforms joint registration-PCA-based models.')
}}
{{ paper('Vesselformer: Towards Complete 3D Vessel Graph Generation from Images',
        'Chinmay Prabhakar, Suprosanna Shit, Johannes C. Paetzold, Ivan Ezhov, Rajat Koner, Hongwei Li, Florian Sebastian Kofler, bjoern menze',
        openreview='https://openreview.net/forum?id=X_AJqHfE1H',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O140',
        paper='papers/O140',
        proceedings='',
        abstract='The reconstruction of graph representations from Images (Image-to-graph) is a frequent task, especially vessel graph extraction from biomedical images. Traditionally, this problem is tackled by a two-stage process: segmentation followed by skeletonization. However, the ambiguity in the heuristic-based pruning of the centerline graph from the skeleta makes it hard to achieve a compact yet faithful graph representation. Recently, \\textit{Relationformer} proposed an end-to-end solution to extract graphs directly from images. However, it does not consider edge features, particularly radius information, which is crucial in many applications such as flow simulation. Further, Relationformer predicts only patch-based graphs. In this work, we address these two shortcomings. We propose a task-specific token, namely radius-token, which explicitly focuses on capturing radius information between two nodes. Second, we propose an efficient algorithm to infer a large 3D graph from patch inference. Finally, we show experimental results on a synthetic vessel dataset and achieve the first 3D complete graph prediction. Code is available at \\url{https://github.com/****}. ')
}}

## Posters - 11:00am - 12:00pm & 3:00pm - 4:00pm

[% .papers %]
{{ paper('A Geometric Deep Learning Framework for Generation of Virtual Left Ventricles as Graphs',
        'Soodeh Kalaie, Andrew J. Bulpitt, Alejandro F. Frangi, Ali Gooya',
        openreview='https://openreview.net/forum?id=Ao0D2HMB8P',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O216',
        paper='papers/O216',
        proceedings='',
        abstract='Generative statistical models have a wide range of applications in the modelling of anatomies. In-silico clinical trials of medical devices, for instance, require the development of virtual populations of anatomy that capture enough variability while remaining plausible. Model construction and use are heavily influenced by the correspondence problem and establishing shape matching over a large number of training data.This study focuses on generating virtual cohorts of left ventricle geometries resembling different-sized shape populations, suitable for in-silico experiments. We present an unsupervised data-driven probabilistic generative model for shapes. This framework incorporates an attention-based shape matching procedure using graph neural networks, coupled with a $\\beta-$VAE generation model, eliminating the need for initial shape correspondence. Left ventricle shapes derived from cardiac magnetic resonance images available in the UK Biobank are utilized for training and validating the framework. We investigate our method’s generative capabilities in terms of generalisation and specificity and show that it is able to synthesise virtual populations of realistic shapes with volumetric measurements in line with actual clinical indices. Moreover, results show our method outperforms joint registration-PCA-based models.')
}}
{{ paper('DBGDGM: Dynamic Brain Graph Deep Generative Model',
        'Alexander Campbell, Simeon Emilov Spasov, Nicola Toschi, Pietro Lio',
        openreview='https://openreview.net/forum?id=WHS3Zv9pxz',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O139',
        paper='papers/O139',
        proceedings='',
        abstract='Graphs are a natural representation of brain activity derived from functional magnetic imaging (fMRI) data. It is well known that clusters of anatomical brain regions, known as functional connectivity networks (FCNs), encode temporal relationships which can serve as useful biomarkers for understanding brain function and dysfunction. Previous works, however, ignore the temporal dynamics of the brain and focus on static graphs. In this paper, we propose a dynamic brain graph deep generative model (DBGDGM) which simultaneously clusters brain regions into temporally evolving communities and learns dynamic unsupervised node embeddings. Specifically, DBGDGM represents brain graph nodes as embeddings sampled from a distribution over communities that evolve over time. We parameterise this community distribution using neural networks that learn from subject and node embeddings as well as past community assignments. Experiments demonstrate DBGDGM outperforms baselines in graph generation, dynamic link prediction, and is comparable for graph classification. Finally, an analysis of the learnt community distributions reveals overlap with known FCNs reported in neuroscience literature.')
}}
{{ paper('DRIMET: Deep Registration-based 3D Incompressible Motion Estimation in Tagged-MRI with Application to the Tongue',
        'Zhangxing Bian, Fangxu Xing, Jinglun Yu, Muhan Shao, Yihao Liu, Aaron Carass, Jonghye Woo, Jerry L Prince',
        openreview='https://openreview.net/forum?id=jkSC4UHHVzy',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O047',
        paper='papers/O047',
        proceedings='',
        abstract='Tagged magnetic resonance imaging (MRI) has been used for decades to observe and quantify the detailed motion of deforming tissue. However, this technique faces several challenges such as tag fading, large motion, long computation times, and difficulties in obtaining diffeomorphic incompressible flow fields. To address these issues, this paper presents a novel unsupervised phase-based 3D motion estimation technique for tagged MRI. We introduce two key innovations. First, we apply a sinusoidal transformation to the harmonic phase input, which enables end-to-end training and avoids the need for phase interpolation. Second, we propose a Jacobian determinant-based learning objective to encourage incompressible flow fields for deforming biological tissues.  Our method efficiently estimates 3D motion fields that are accurate, dense, and approximately diffeomorphic and incompressible. The efficacy of the method is assessed using human tongue motion during speech, and includes both healthy controls and patients that have undergone glossectomy. We show that the method outperforms existing approaches, and also exhibits improvements in speed, robustness to tag fading, and large tongue motion. The code is available.')
}}
{{ paper('Generalizing Unsupervised Anomaly Detection: Towards Unbiased Pathology Screening',
        'Cosmin I. Bercea, Benedikt Wiestler, Daniel Rueckert, Julia A Schnabel',
        openreview='https://openreview.net/forum?id=8ojx-Ld3yjR',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O021',
        paper='papers/O021',
        proceedings='',
        abstract='The main benefit of unsupervised anomaly detection is the ability to identify arbitrary, rare data instances of pathologies even in the absence of training labels or sufficient examples of the rare class(es). In the clinical workflow, such methods have the potential to assist in screening and pre-filtering exams for potential pathologies and thus meaningfully support radiologists. Even though much work has been done on using auto-encoders (AE) for anomaly detection, there are still two critical challenges to overcome: First, learning compact and detailed representations of the healthy distribution is cumbersome. Recent work shows that AEs can reconstruct some types of anomalies even better than actual samples from the training distribution. Second, while the majority of unsupervised algorithms are tailored to detect hyperintense lesions on FLAIR brain MR scans, recent improvements in basic intensity thresholding techniques have outperformed them.  Moreover, we found that even state-of-the-art (SOTA) AEs fail to detect several classes of non-hyperintense anomalies on T1w brain MRIs, such as brain atrophy, edema, or resections. In this work, we propose reversed AEs (RA) to generate pseudo-healthy reconstructions and localize various brain pathologies. We extensively evaluate our method on T1w brain scans and increase the detection of global pathology and artefacts from 73.1 to 89.4 AUROC and the amount of detected local pathologies from 52.6% to 86.0% compared to SOTA methods.')
}}
{{ paper('Joint Breast Neoplasm Detection and Subtyping using Multi-Resolution Network Trained on Large-Scale H&E Whole Slide Images with Weak Labels',
        'Adam Casson, Siqi Liu, Ran A Godrich, Hamed Aghdam, Brandon Rothrock, Kasper Malfroid, Christopher Kanan, Thomas Fuchs',
        openreview='https://openreview.net/forum?id=rXVtHHFLRIz',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O007',
        paper='papers/O007',
        proceedings='',
        abstract='Breast cancer is the most commonly diagnosed cancer and the use of artificial intelligence (AI) to help diagnose the disease from digital pathology images has the potential to greatly improve patient outcomes. However, current methods for detecting, segmenting, and sub-typing breast neoplasms and other proliferative lesions often rely on costly and time-consuming manual annotation efforts, which can be impractical for large-scale datasets. In this work, we propose an annotation-free learning framework to jointly detect, segment, and subtype breast neoplasms. Our approach leverages top-k multiple instance learning to train an initial neoplasm detection backbone network from weakly-labeled whole slide images, which is then used to automatically generate pixel-level pseudo-labels for whole slides with only one subtype. A second network is trained using these pseudo-labels, and slide-level classification is performed by training an aggregator network that fuses the embeddings from both backbone networks. We trained and validated our framework on large-scale datasets with more than 100k whole slide images and demonstrate its effectiveness on tasks including breast neoplasms detection, segmentation, and subtyping.')
}}
{{ paper('Learning Clinically Acceptable Segmentation of Organs at Risk in Cervical Cancer Radiation Treatment from Clinically Available Annotations',
        'Monika Grewal, Dustin van Weersel, Henrike Westerveld, Peter Bosman, Tanja Alderliesten',
        openreview='https://openreview.net/forum?id=uPRFWdz03_',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O100',
        paper='papers/O100',
        proceedings='',
        abstract='Deep learning models benefit from training with a large dataset (labeled or unlabeled). Following this motivation, we present an approach to learn a deep learning model for the automatic segmentation of Organs at Risk (OARs) in cervical cancer radiation treatment from a large clinically available dataset of Computed Tomography (CT) scans containing data inhomogeneity, label noise, and missing annotations. We employ simple heuristics for automatic data cleaning to minimize data inhomogeneity and label noise. Further, we develop a semi-supervised learning approach utilizing a teacher-student setup, annotation imputation, and uncertainty-guided training to learn in presence of missing annotations. Our experimental results show that learning from a large dataset with our approach yields a significant improvement in the test performance despite missing annotations in the data. Further, the contours generated from the segmentation masks predicted by our model are found to be equally clinically acceptable as manually generated contours.')
}}
{{ paper('Model Adaptive Tooth Segmentation',
        'Ruizhe Chen, Jianfei Yang, YANG FENG, Jin Hao, Zuozhu Liu',
        openreview='https://openreview.net/forum?id=O2DerS5oQ1',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O048',
        paper='papers/O048',
        proceedings='',
        abstract='Automatic 3-dimensional tooth segmentation on intraoral scans (IOS) plays a pivotal role in computer-aided orthodontic treatments. In practice, deploying existing well-trained models to different medical centers suffers from two main problems: (1) the data distribution shifts between existing and new centers, (2) the data in the existing center is usually not allowed to share while annotating additional data in the new center is time-consuming and expensive. In this paper, we propose a Model Adaptive Tooth Segmentation (MATS) framework to alleviate these issues. Taking the trained model from a source center as input, MATS adapts it to different target centers without data transmission or additional annotations, as inspired by the source data-free domain adaptation (SFDA) paradigm. The model adaptation in MATS is realized by a tooth-level feature prototype learning module, a progressive pseudo-labeling module and a tooth-prior regularized information maximization loss. Experiments on a dataset with tooth abnormalities and a real-world cross-center dataset show that MATS can consistently surpass existing baselines. The effectiveness is further verified with extensive ablation studies and statistical analysis, demonstrating its applicability for privacy-preserving tooth segmentation in real-world digital dentistry. ')
}}
{{ paper('MS-Former: Multi-Scale Self-Guided Transformer for Medical Image Segmentation',
        'Sanaz Karimijafarbigloo, Reza Azad, Amirhossein Kazerouni, Dorit Merhof',
        openreview='https://openreview.net/forum?id=pp2raGSU3Wx',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O031',
        paper='papers/O031',
        proceedings='',
        abstract='Multi-scale representations have proven to be a powerful tool since they can take into account both the fine-grained details of objects in an image as well as the broader context. Inspired by this, we propose a novel dual-branch transformer network that operates on two different scales to encode global contextual dependencies while preserving local information. To learn in a self-supervised fashion, our approach considers the semantic dependency that exists between different scales to generate a supervisory signal for inter-scale consistency and also imposes a spatial stability loss within the scale for self-supervised content clustering. While intra-scale and inter-scale consistency losses aim to increase features similarly within the cluster, we propose to include a cross-entropy loss function on top of the clustering score map to effectively model each cluster distribution and increase the decision boundary between clusters. Iteratively our algorithm learns to assign each pixel to a semantically related cluster to produce the segmentation map. Extensive experiments on skin lesion and lung segmentation datasets show the superiority of our method compared to the state-of-the-art (SOTA) approaches. ')
}}
{{ paper('Reproducibility of the Methods in Medical Imaging with Deep Learning.',
        'Attila Simkó, Anders Garpebring, Joakim Jonsson, Tufve Nyholm, Tommy Löfstedt',
        openreview='https://openreview.net/forum?id=_P59zCfXOt',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O029',
        paper='papers/O029',
        proceedings='',
        abstract='Concerns about the reproducibility of deep learning research are more prominent than ever, with no clear solution in sight. The Medical Imaging with Deep Learning (MIDL) conference has made advancements in employing empirical rigor with regards to reproducibility by advocating open access, and recently also recommending authors to make their code public---both aspects being adopted by the majority of the conference submissions.  We have evaluated all accepted full paper submissions to MIDL between 2018 and 2022 using established, but adjusted guidelines addressing the reproducibility and quality of the public repositories.  The evaluations show that publishing repositories and using public datasets are becoming more popular, which helps traceability, but the quality of the repositories shows room for improvement in every aspect. Merely 22% of all submissions contain a repository that was deemed repeatable using our evaluations.  From the commonly encountered issues during the evaluations, we propose a set of guidelines for machine learning-related research for medical imaging applications, adjusted specifically for future submissions to MIDL. We presented our results to future MIDL authors who were eager to continue an open discussion on the topic of code reproducibility.')
}}
{{ paper('SuperMask: Generating High-resolution object masks from multi-view, unaligned low-resolution MRIs',
        'Hanxue Gu, Hongyu He, Roy Colglazier, Jordan Axelrod, Robert French, Maciej A Mazurowski',
        openreview='https://openreview.net/forum?id=oi5psB9R_l',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O039',
        paper='papers/O039',
        proceedings='',
        abstract='Three-dimensional segmentation in magnetic resonance images (MRI), which reflects the true shape of the objects, is challenging since high-resolution isotropic MRIs are rare and typical MRIs are anisotropic, with the out-of-plane dimension having a much lower resolution. A potential remedy to this issue lies in the fact that often multiple sequences are acquired on different planes. However, in practice, these sequences are not orthogonal to each other, limiting the applicability of many previous solutions to reconstruct higher-resolution images from multiple lower-resolution ones. We propose a novel deep learning-based solution to generating high-resolution masks from multiple low-resolution images. Our method combines segmentation and unsupervised registration networks by introducing two new regularizations to make registration and segmentation reinforce each other. Finally, we introduce a multi-view fusion method to generate high-resolution target object masks. The experimental results on two datasets show the superiority of our methods. Importantly, the advantage of not using high-resolution images in the training process makes our method applicable to a wide variety of MRI segmentation tasks.')
}}
{{ paper('Tumor Budding T-cell Graphs: Assessing the Need for Resection in pT1 Colorectal Cancer Patients',
        'Linda Studer, JM Bokhorst, I Nagtegaal, Inti Zlobec, Heather Dawson, Andreas Fischer',
        openreview='https://openreview.net/forum?id=ruaXPgZCk6i',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O088',
        paper='papers/O088',
        proceedings='',
        abstract='Colon resection is often the treatment of choice for colorectal cancer (CRC) patients. However, especially for minimally invasive cancer, such as pT1, simply removing the polyps may be enough to stop cancer progression. Different histopathological risk factors such as tumor grade and invasion depth currently found the basis for the need for colon resection in pT1 CRC patients. Here, we investigate two additional risk factors, tumor budding and lymphocyte infiltration at the invasive front, which are known to be clinically relevant. We capture the spatial layout of tumor buds and T-cells and use graph-based deep learning to investigate them as potential risk predictors. Our pT1 Hotspot Tumor Budding T-cell Graph (pT1-HBTG) dataset consists of 626 tumor budding hotspots from 575 patients. We propose and compare three different graph structures, as well as combinations of the node labels. The best-performing Graph Neural Network architecture is able to increase specificity by 20% compared to the currently recommended risk stratification based on histopathological risk factors, without losing any sensitivity. We believe that using a graph-based analysis can help to assist pathologists in making risk assessments for pT1 CRC patients, and thus decrease the number of patients undergoing potentially unnecessary surgery. Both the code and dataset are made publicly available.')
}}
{{ paper('Unsupervised Stain Decomposition via Inversion Regulation for Multiplex Immunohistochemistry Images',
        'Shahira Abousamra, Danielle Fassler, Jiachen Yao, Rajarsi R. Gupta, Tahsin Kurc, Luisa Escobar-Hoyos, Dimitris Samaras, Kenneth Shroyer, Joel Saltz, Chao Chen',
        openreview='https://openreview.net/forum?id=J0VD-I2IOOg',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O026',
        paper='papers/O026',
        proceedings='',
        abstract='Multiplex Immunohistochemistry (mIHC) is a cost-effective and accessible method for in situ labeling of multiple protein biomarkers in a tissue sample. By assigning a different stain to each biomarker, it allows the visualization of different types of cells within the tumor vicinity for downstream analysis. However, to detect different types of stains in a given mIHC image is a challenging problem, especially when the number of stains is high. Previous deep-learning-based methods mostly assume full supervision; yet the annotation can be costly. In this paper, we propose a novel unsupervised stain decomposition method to detect different stains simultaneously. Our method does not require any supervision, except for color samples of different stains. A main technical challenge is that the problem is underdetermined and can have multiple solutions. To conquer this issue, we propose a novel inversion regulation technique, which eliminates most undesirable solutions. On a 7-plexed IHC image dataset, the proposed method achieves high quality stain decomposition results without human annotation.')
}}
{{ paper('Vesselformer: Towards Complete 3D Vessel Graph Generation from Images',
        'Chinmay Prabhakar, Suprosanna Shit, Johannes C. Paetzold, Ivan Ezhov, Rajat Koner, Hongwei Li, Florian Sebastian Kofler, bjoern menze',
        openreview='https://openreview.net/forum?id=X_AJqHfE1H',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O140',
        paper='papers/O140',
        proceedings='',
        abstract='The reconstruction of graph representations from Images (Image-to-graph) is a frequent task, especially vessel graph extraction from biomedical images. Traditionally, this problem is tackled by a two-stage process: segmentation followed by skeletonization. However, the ambiguity in the heuristic-based pruning of the centerline graph from the skeleta makes it hard to achieve a compact yet faithful graph representation. Recently, \\textit{Relationformer} proposed an end-to-end solution to extract graphs directly from images. However, it does not consider edge features, particularly radius information, which is crucial in many applications such as flow simulation. Further, Relationformer predicts only patch-based graphs. In this work, we address these two shortcomings. We propose a task-specific token, namely radius-token, which explicitly focuses on capturing radius information between two nodes. Second, we propose an efficient algorithm to infer a large 3D graph from patch inference. Finally, we show experimental results on a synthetic vessel dataset and achieve the first 3D complete graph prediction. Code is available at \\url{https://github.com/****}. ')
}}
{{ paper('Interpretable histopathology-based prediction of disease relevant features in Inflammatory Bowel Disease biopsies using weakly-supervised deep learning',
        'Ricardo Mokhtari, Azam Hamidinekoo, Daniel James Sutton, Arthur Lewis, Bastian Angermann, Ulf Gehrmann, Pål Lundin, Hibret Adissu, Junmei Cairns, Jessica Neisen, Emon Khan, Daniel Marks, Nia Khachapuridze, Talha Qaiser, Nikolay Burlutskiy',
        openreview='https://openreview.net/forum?id=m-f1SNDhde',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P002',
        paper='papers/P002',
        proceedings='',
        abstract='Crohn’s Disease (CD) and Ulcerative Colitis (UC) are the two main Inflammatory Bowel Disease (IBD) types. We developed interpretable deep learning models to identify histolog- ical disease features for both CD and UC using only endoscopic labels. We explored fine- tuning and end-to-end training of two state-of-the-art self-supervised models for predicting three different endoscopic categories (i) CD vs UC (AUC=0.87), (ii) normal vs lesional (AUC=0.81), (iii) low vs high disease severity score (AUC=0.80). With the support of a pathologist, we explored the relationship between endoscopic labels, model predictions and histological evaluations qualitatively and quantitatively and identified cases where the pathologist’s descriptions of inflammation were consistent with regions of high attention. In parallel, we used a model trained on the Colon Nuclei Identification and Counting (CoNIC) dataset to predict and explore 6 cell populations. We observed consistency between areas enriched with the predicted immune cells in biopsies and the pathologist’s feedback on the attention maps. Finally, we identified several cell level features indicative of disease severity in CD and UC. These models can enhance our understanding about the pathology behind IBD and can shape our strategies for patient stratification in clinical trials.')
}}
{{ paper('Denoising Diffusion Models for Memory-efficient Processing of 3D Medical Images',
        'Florentin Bieder, Julia Wolleb, Alicia Durrer, Robin Sandkuehler, Philippe C. Cattin',
        openreview='https://openreview.net/forum?id=neXqIGpO-tn',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P009',
        paper='papers/P009',
        proceedings='',
        abstract='Denoising diffusion models have recently achieved state-of-the-art performance in many image-generation tasks. They do, however, require a large amount of computational resources. This limits their application to medical tasks, where we often deal with large 3D volumes, like high-resolution three-dimensional data. In this work, we present a number of different ways to reduce the resource consumption for 3D diffusion models and apply them to a dataset of 3D images. The main contribution of this paper is the memory-efficient patch-based diffusion model PatchDDM, which can be applied to the total volume during inference while the training is performed only on patches. Without limiting the application of the proposed diffusion model for image generation, we evaluate the method on the tumor segmentation task of the BraTS2020 dataset and demonstrate that we can generate meaningful three-dimensional segmentations.')
}}
{{ paper('Reference-based MRI Reconstruction Using Texture Transformer',
        'Pengfei Guo, Vishal M. Patel',
        openreview='https://openreview.net/forum?id=EoEWcHFHJ1W',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P012',
        paper='papers/P012',
        proceedings='',
        abstract='Deep Learning (DL) based methods for magnetic resonance (MR) image reconstruction have been shown to produce superior performance. However, previous methods either only leverage under-sampled data or require a paired fully-sampled auxiliary MR sequence to perform guidance-based reconstruction. Consequently, existing approaches neglect to explore attention mechanisms that can transfer texture from reference data to under-sampled data within a single MR sequence, which either limits the performance of these approaches or increases the difficulty of data acquisition. In this paper, we propose a novel $\\textbf{T}$exture $\\textbf{T}$ransformer $\\textbf{M}$odule ($\\textbf{TTM}$) for the reference-based MR image reconstruction. The TTM facilitates joint feature learning across under-sampled and reference data, so feature correspondences can be discovered by attention and accurate texture features can be leveraged during reconstruction. Notably, TTM can be stacked on prior MRI reconstruction methods to improve their performance. In addition, a $\\textbf{R}$ecurrent $\\textbf{T}$ransformer $\\textbf{R}$econstruction backbone ($\\textbf{RTR}$) is proposed to further improve the performance in a unified framework. Extensive experiments demonstrate the effectiveness of TTM and show that RTR can achieve the state-of-the-art results on multiple datasets. Implementation code and pre-trained weights will be made public after the review process.  ')
}}
{{ paper('Domain Adaptation using Silver Standard Labels for Ki-67 Scoring in Digital Pathology A Step Closer to Widescale Deployment',
        'Amanda Dy, Ngoc-Nhu Jennifer Nguyen, Seyed Hossein Mirjahanmardir, Dimitrios Androutsos, Melanie Dawe, Anthony Fyles, Wei Shi, Fei-Fei Liu, Susan Done, April Khademi',
        openreview='https://openreview.net/forum?id=-ahfrpMo9ui',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P016',
        paper='papers/P016',
        proceedings='',
        abstract='Deep learning systems have been proposed to improve the objectivity and efficiency of Ki-67 PI scoring. The challenge is that deep learning techniques, while very accurate, suffer from reduced performance when applied to out-of-domain data. This is a critical challenge for clinical translation, as models are typically trained using data available to the vendor, which is not from the target domain. To address this challenge, this study proposes a domain adaptation pipeline that employs an unsupervised framework to generate silver standard (pseudo) labels in the target domain, which is used to augment the gold standard (GS) source domain data. Five training regimes were tested on two validated Ki-67 scoring architectures (UV-Net and piNET), (1) SS Only: trained on target silver standard (SS) labels, (2) GS Only: trained on source GS labels, (3) Mixed: trained on target SS and source GS labels, (4) GS+SS: trained on source GS labels and fine-tuned on target SS labels, and our proposed method (5) SS+GS: trained on source SS labels and fine-tuned on source GS labels. The SS+GS method yielded significantly ($p<0.05$) higher PI accuracy ($95.9\\%$) and more consistent results compared to the GS Only model on target data.  Analysis of t-SNE plots showed features learned by the SS+GS models are more aligned for source and target data which results in improved generalization. The proposed pipeline provides an efficient method for learning the target distribution  without the need for manual annotations, which are time-consuming and costly to generate for medical images. This framework can be applied to any target site as a per-laboratory calibration method, for widescale deployment.')
}}
{{ paper('DeepBrainPrint: A Novel Contrastive Framework for Brain MRI Re-Identification',
        'Lemuel Puglisi, Arman Eshaghi, Geoff Parker, Frederik Barkhof, Daniel C. Alexander, Daniele Ravi',
        openreview='https://openreview.net/forum?id=i5khDI1te1M',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P033',
        paper='papers/P033',
        proceedings='',
        abstract="Recent advances in MRI have led to the creation of large datasets. With the increase in data volume, it has become difficult to locate previous scans of the same patient within these datasets (a process known as re-identification). To address this issue, we propose an AI-powered medical imaging retrieval framework called DeepBrainPrint, which is designed to retrieve brain MRI scans of the same patient. Our framework is a semi-self-supervised contrastive deep learning approach with three main innovations. First, we use a combination of self-supervised and supervised paradigms to create an effective brain fingerprint from MRI scans that can be used for real-time image retrieval. Second, we use a special weighting function to guide the training and improve model convergence. Third, we introduce new imaging transformations to improve retrieval robustness in the presence of intensity variations (i.e. different scan contrasts), and to account for age and disease progression in patients. We tested DeepBrainPrint on a large dataset of T1-weighted brain MRIs from the Alzheimer\\'s Disease Neuroimaging Initiative (ADNI) and on a synthetic dataset designed to evaluate retrieval performance with different image modalities. Our results show that DeepBrainPrint outperforms previous methods, including simple similarity metrics and more advanced contrastive deep learning frameworks.")
}}
{{ paper('Video pretraining advances 3D deep learning on chest CT tasks',
        'Alexander Ke, Shih-Cheng Huang, Chloe P OConnell, Michal Klimont, Serena Yeung, Pranav Rajpurkar',
        openreview='https://openreview.net/forum?id=zhpP7zluLBk',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P046',
        paper='papers/P046',
        proceedings='',
        abstract='Pretraining on large natural image classification datasets such as ImageNet has aided model development on data-scarce 2D medical tasks. 3D medical tasks often have much less data than 2D medical tasks, prompting practitioners to rely on pretrained 2D models to featurize slices. However, these 2D models have been surpassed by 3D models on 3D computer vision benchmarks since they do not natively leverage cross-sectional or temporal information. In this study, we explore whether natural video pretraining for 3D models can enable higher performance on smaller datasets for 3D medical tasks. We demonstrate video pretraining improves the average performance of seven 3D models on two chest CT datasets, regardless of finetuning dataset size, and that video pretraining allows 3D models to outperform 2D baselines. Lastly, we observe that pretraining on the large-scale out-of-domain Kinetics dataset improves performance more than pretraining on a typically-sized in-domain CT dataset. Our results show consistent benefits of video pretraining across a wide array of architectures, tasks, and training dataset sizes, supporting a shift from small-scale in-domain pretraining to large-scale out-of-domain pretraining for 3D medical tasks.')
}}
{{ paper('MEDIMP: 3D Medical Images and clinical Prompts for renal transplant representation learning',
        'Leo Milecki, Vicky Kalogeiton, Sylvain Bodard, Dany Anglicheau, Jean-Michel Correas, Marc-Olivier Timsit, Maria Vakalopoulou',
        openreview='https://openreview.net/forum?id=jt-ochRhqG',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P055',
        paper='papers/P055',
        proceedings='',
        abstract='Renal transplantation emerges as the most effective solution for end-stage renal disease. Occurring from complex causes, a substantial risk of transplant chronic dysfunction persists and may lead to graft loss. Medical imaging plays a substantial role in renal transplant monitoring in clinical practice. However, graft supervision is multi-disciplinary, notably joining nephrology, urology, and radiology, while identifying robust biomarkers from such high-dimensional and complex data for prognosis is challenging. In this work, taking inspiration from the recent success of Large Language Models (LLMs), we propose MEDIMP -- Medical Images and clinical Prompts -- a model to learn meaningful multi-modal representations of renal transplant Dynamic Contrast-Enhanced Magnetic Resonance Imaging (DCE MRI) by incorporating structural clinicobiological data after translating them into text prompts. MEDIMP is based on contrastive learning from joint text-image paired embeddings to perform this challenging task. Moreover, we propose a framework that generates medical prompts using automatic textual data augmentations from LLMs. Our goal is to learn meaningful manifolds of renal transplant DCE MRI, interesting for the prognosis of the transplant or patient status (2, 3, and 4 years after the transplant), fully exploiting the limited available multi-modal data most efficiently. Extensive experiments and comparisons with other renal transplant representation learning methods with limited data prove the effectiveness of MEDIMP in a relevant clinical setting, giving new directions toward medical prompts. Our code is available at https://github.com/leomlck/MEDIMP.')
}}
{{ paper('Stage Detection of Mild Cognitive Impairment: Region-dependent Graph Representation Learning on Brain Morphable Meshes',
        'Jiaqi Guo, Emanuel Azcona, Santiago Lopez-Tapia, Aggelos Katsaggelos',
        openreview='https://openreview.net/forum?id=J4JWTCq14u',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P068',
        paper='papers/P068',
        proceedings='',
        abstract="Mild cognitive impairment (MCI), as a transitional state between normal cognition and Alzheimer\\'s disease (AD), is crucial for taking preventive interventions in order to slow down AD progression. Given the high relevance of brain atrophy and the neurodegeneration process of AD, we propose a novel mesh-based pooling module, RegionPool, to investigate the morphological changes in brain shape regionally. We then present a geometric deep learning framework with the RegionPool and graph attention convolutions to perform binary classification on MCI subtypes (EMCI/LMCI). Our model does not require feature engineering and relies only on the relevant geometric information of T1-weighted magnetic resonance imaging (MRI) signals. Our evaluation reveals the state-of-the-art classification capabilities of our network and shows that current empirically derived MCI subtypes cannot identify heterogeneous patterns of cortical atrophy at the MCI stage. The class activation maps (CAMs) generated from the correct predictions provide additional visual evidence for our model\\'s decisions and are consistent with the atrophy patterns reported by the relevant literature.")
}}
{{ paper('Inherently Interpretable Multi-Label Classification Using Class-Specific Counterfactuals',
        'Susu Sun, Stefano Woerner, Andreas Maier, Lisa M. Koch, Christian F. Baumgartner',
        openreview='https://openreview.net/forum?id=OpmQOkfizzM',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P073',
        paper='papers/P073',
        proceedings='',
        abstract='Interpretability is essential for machine learning algorithms in high-stakes application fields such as medical image analysis. However, high-performing black-box neural networks do not provide explanations for their predictions, which can lead to mistrust and suboptimal human-ML collaboration. Post-hoc explanation techniques, which are widely used in practice, have been shown to suffer from severe conceptual problems. Furthermore, as we show in this paper, current explanation techniques do not perform adequately in the multi-label scenario, in which multiple medical findings may co-occur in a single image. We propose Attri-Net, an inherently interpretable model for multi-label classification. Attri-Net is a powerful classifier that provides transparent, trustworthy, and human-understandable explanations. The model first generates class-specific attribution maps based on counterfactuals to identify which image regions correspond to certain medical findings. Then a simple logistic regression classifier is used to make predictions based solely on these attribution maps. We compare Attri-Net to five post-hoc explanation techniques and one inherently interpretable classifier on three chest X-ray datasets. We find that Attri-Net produces high-quality multi-label explanations consistent with clinical knowledge and has comparable classification performance to state-of-the-art classification models.')
}}
{{ paper('MultiTask Learning for accelerated-MRI Reconstruction and Segmentation of Brain Lesions in Multiple Sclerosis',
        'Dimitrios Karkalousos, Ivana Isgum, Henk Marquering, Matthan W. A. Caan',
        openreview='https://openreview.net/forum?id=ci2Fg31H0T',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P078',
        paper='papers/P078',
        proceedings='',
        abstract='This work proposes MultiTask Learning for accelerated-MRI Reconstruction and Segmentation (MTLRS). Unlike the common single-task approaches, MultiTask Learning identifies relations between multiple tasks to improve the performance of all tasks. The proposed MTLRS consists of a unique cascading architecture, where a recurrent reconstruction network and a segmentation network inform each other through hidden states. The features of the two networks are shared and implicitly enforced as inductive bias. To evaluate the benefit of MTLRS, we compare performing the two tasks of accelerated-MRI reconstruction and MRI segmentation with pre-trained, sequential, end-to-end, and joint approaches. A synthetic multicoil dataset is used to train, validate, and test all approaches with five-fold cross-validation. The dataset consists of 3D FLAIR brain data of relapsing-remitting Multiple Sclerosis patients with known white matter lesions. The acquisition is prospectively undersampled by approximately 7.5 times compared to clinical standards. Reconstruction performance is evaluated by Structural Similarity Index Measure (SSIM) and Peak Signal-to-Noise Ratio (PSNR). Segmentation performance is evaluated by Dice score for combined brain tissue and white matter lesion segmentation and by per lesion Dice score. Results show that MTLRS outperforms other evaluated approaches, providing high-quality reconstructions and accurate white matter lesion segmentation. A significant correlation was found between the performance of both tasks (SSIM and per lesion Dice score, $\\rho=0.92$, $p=0.0005$). Our proposed MTLRS demonstrates that accelerated-MRI reconstruction and MRI segmentation can be effectively combined to improve performance on both tasks, potentially benefiting clinical settings.')
}}
{{ paper('Multi PILOT: Feasible Learned Multiple Acquisition Trajectories For Dynamic MRI',
        'Tamir Shor',
        openreview='https://openreview.net/forum?id=NXPLq6w___',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P085',
        paper='papers/P085',
        proceedings='',
        abstract='Dynamic Magnetic Resonance Imaging (MRI) is known to be a powerful and reliable technique for the dynamic imaging of internal organs and tissues, making it a leading diagnostic tool. A major difficulty in using MRI in this setting is the relatively long acquisition time (and, hence, increased cost) required for imaging in high spatio-temporal resolution, leading to the appearance of related motion artifacts and decrease in resolution. Compressed Sensing (CS) techniques have become a common tool to reduce MRI acquisition time by subsampling images in the $k$-space according to some acquisition trajectory. Several studies have particularly focused on applying deep learning techniques to learn these acquisition trajectories in order to attain better image reconstruction, rather than using some predefined set of trajectories. To the best of our knowledge, learning acquisition trajectories has been only explored in the context of static MRI. In this study, we consider acquisition trajectory learning in the dynamic imaging setting. We design an end-to-end pipeline for the joint optimization of multiple per-frame acquisition trajectories along with a reconstruction neural network, and demonstrate improved image reconstruction quality in shorter acquisition times. The code for reproducing all experiments will accompany the paper.')
}}
{{ paper('Few Shot Hematopoietic Cell Classification',
        'Vu Nguyen, Prantik Howlader, Le Hou, Dimitris Samaras, Rajarsi R. Gupta, Joel Saltz',
        openreview='https://openreview.net/forum?id=9yTSJIb5t_Z',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P101',
        paper='papers/P101',
        proceedings='',
        abstract='We propose a few shot learning approach for the problem of hematopoietic cell classification in digital pathology. In hematopoiesis cell classification, the classes correspond to the different stages of the cellular maturation process. Two  consecutive stage categories are considered to have a neighborhood relationship, which implies a visual similarity between the two categories. We propose RelationVAE which incorporates these relationships between hematopoietic cell classes to robustly generate more data for the classes with limited training data. Specifically, we first model these relationships using a graphical model, and propose RelationVAE, a deep generative model which implements the graphical model. RelationVAE is trained to optimize the lower bound of the pairwise data likelihood of the graphical model. In this way, it can identify class level features of a specific class from a small number of input images together with the knowledge transferred from visually similar classes, leading to more robust sample synthesis. The experiments on our collected hematopoietic dataset show the improved results of our proposed RelationVAE over a baseline VAE model and other few shot learning methods.')
}}
{{ paper('Prior Guided 3D Medical Image Landmark Localization',
        'yijie pang, Pujin Cheng, Junyan Lyu, FAN lin, Xiaoying Tang',
        openreview='https://openreview.net/forum?id=Ae1KAltzEd',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P117',
        paper='papers/P117',
        proceedings='',
        abstract='Accurate detection of 3D landmarks is critical for evaluating and characterizing anatomical features and performing preoperative diagnostic screening. However, detecting 3D landmarks can be challenging due to the local structural homogeneity of medical images. To address this issue, physicians often annotate multiple landmarks in a single slice, particularly when estimating 3D distance or volume. In this study, we present a prior guided coarse-to-fine framework for efficient and accurate 3D medical landmark detection; we make use of the prior information that in specific settings physicians annotate multiple landmarks on a same slice. The coarse stage uses coordinate regression on downsampled 3D images to maintain the structural relationships across different landmarks. The fine stage categorizes landmarks as correlated and independent landmarks based on their annotation prior. For independent landmarks, we train multiple models to capture local features and ensure reliable local predictions. For correlated landmarks, we mimic the manual annotation process and propose a correlated landmark detection model that merges information from various patches to query key slices and identify correlated landmarks. Our method is extensively evaluated on two datasets, exhibiting superior performance with an average detection error of respective 3.29 mm and 2.13 mm.')
}}
{{ paper('Calibration techniques for node classification using graph neural networks on medical image data',
        'Iris Vos, Ishaan Bhat, Birgitta Velthuis, Ynte Ruigrok, Hugo Kuijf',
        openreview='https://openreview.net/forum?id=xY3agyj5Eq',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P126',
        paper='papers/P126',
        proceedings='',
        abstract='Miscalibration of deep neural networks (DNNs) can lead to unreliable predictions and hinder their use in clinical decision-making. This miscalibration is often caused by overconfident probability estimates. Calibration techniques such as model ensembles, regularization terms, and post-hoc scaling of the predictions can be employed to improve the calibration performance of DNNs. In contrast to DNNs, graph neural networks (GNNs) tend to exhibit underconfidence. In this study, we investigate the efficacy of calibration techniques developed for DNNs when applied to GNNs trained on medical image data, and compare the calibration performance of binary and multiclass node classification on a benchmark dataset and a medical image dataset. We find that post-hoc methods using Platt scaling or Temperature scaling, or methods that add a regularization term to the loss function during training are most effective to improve calibration. Our results further indicate that these calibration techniques are more effective for multiclass classification tasks compared to binary classification tasks.')
}}
{{ paper('ST(OR)$^2$: Spatio-Temporal Object Level Reasoning for Activity Recognition in the Operating Room',
        'Idris Hamoud, Muhammad Abdullah Jamal, Vinkle Srivastav, Didier MUTTER, Nicolas Padoy, Omid Mohareri',
        openreview='https://openreview.net/forum?id=C6EJi0SS7j',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P132',
        paper='papers/P132',
        proceedings='',
        abstract='Surgical robotics holds much promise for improving patient safety and clinician experience in the Operating Room (OR). However, it also comes with new challenges, requiring strong team coordination and effective OR management. Automatic detection of surgical activities is a key requirement for developing AI-based intelligent tools to tackle these challenges. The current state-of-the-art surgical activity recognition methods however operate on image-based representations and depend on large-scale labeled datasets whose collection is time-consuming and resource-expensive. This work proposes a new sample-efficient and object-based approach for surgical activity recognition in the OR. Our method focuses on the geometric arrangements between clinicians and surgical devices, thus utilizing the significant object interaction dynamics in the OR. We conduct experiments in a low-data regime study for long video activity recognition. We also benchmark our method against other object-centric approaches on clip-level action classification and show superior performance.')
}}
{{ paper('Improved multi-site Parkinsons disease classification using neuroimaging data with counterfactual inference',
        'Vibujithan Vigneshwaran, Matthias Wilms, Milton Ivan Camacho Camacho, Raissa Souza, Nils Forkert',
        openreview='https://openreview.net/forum?id=l4LDtGb8zL',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P137',
        paper='papers/P137',
        proceedings='',
        abstract='Deep learning has led to many advances in medical image analysis for various clinical problems. However, most deep learning models are known to be sensitive to differences in the training and test data distributions, which can lead to a decrease in accuracy when applied in real-life scenarios. Thus far, various techniques have been developed to tackle this problem, primarily focusing on harmonizing feature representations from different datasets. Due to the recent increased interest in causal approaches in deep learning, explainable harmonization techniques have gained momentum lately but have not been applied broadly yet. Our study proposes a causal flow-based technique to overcome the problem of different feature distributions in multi-site data used for Parkinson\\\'s disease (PD) classification. Feature distributions from six different sites, with a total of 415 subjects (PD: 263, healthy controls: 152), were used for the experiments. A counterfactual approach to answer the question, How would brain MRI features appear if they were obtained at a different site?\\" was developed using a causal normalizing flow. When tested on features from a previously unseen site, the counterfactual-based classifier demonstrated superior performance (weighted f1 = 0.68) compared to a classifier trained on purely observational data (weighted f1 = 0.36) and improved accuracy compared to a harmonization technique typically used in neurological settings (weighted f1 = 0.5). These results show that the proposed technique can effectively correct differences in multi-site feature distributions to facilitate generalizable deep-learning models.')
}}
{{ paper('Radiology Reports Improve Visual Representations Learned from Radiographs',
        'Haoxu Huang, Samyak Rawlekar, Sumit Chopra, Cem M Deniz',
        openreview='https://openreview.net/forum?id=S9EfOVFJIxQh',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P145',
        paper='papers/P145',
        proceedings='',
        abstract='Although human’s ability to visually understand the structure of the World plays a crucial role in perceiving the World and making appropriate decisions, human perception does not solely rely on vision but amalgamates the information from acoustic, verbal, and visual stimuli. An active area of research has been revolving around designing an efficient framework that adapts to multiple modalities and ideally improves the performance of existing tasks. While numerous frameworks have proved effective on natural datasets like ImageNet, a limited number of studies have been carried out in the biomedical domain. In this work, we extend the available frameworks for natural data to biomedical data by leveraging the abundant, unstructured multi-modal data available as radiology images and reports. We attempt to answer the question, ”For multi-modal learning, self-supervised learning and joint learning using both learning strategies, which one improves the visual representation for downstream chest radiographs classification tasks the most?”. Our experiments indicated that in limited labeled data settings with 1% and 10% labeled data, the joint learning with multi-modal and self-supervised models outperforms self-supervised learning and is at par with multi-modal learning. Additionally, we found that multi-modal learning is generally more robust on out-of-distribution datasets. ')
}}
{{ paper('Federated Cross Learning for Medical Image Segmentation',
        'Xuanang Xu, Hannah H. Deng, Tianyi Chen, Tianshu Kuang, Joshua C. Barber, Daeseung Kim, Jaime Gateno, James J. Xia, Pingkun Yan',
        openreview='https://openreview.net/forum?id=DrZbwobH_zo',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P153',
        paper='papers/P153',
        proceedings='',
        abstract='Federated learning (FL) can collaboratively train deep learning models using isolated patient data owned by different hospitals for various clinical applications, including medical image segmentation. However, a major problem of FL is its performance degradation when dealing with data that are not independently and identically distributed (non-iid), which is often the case in medical images. In this paper, we first conduct a theoretical analysis on the FL algorithm to reveal the problem of model aggregation during training on non-iid data. With the insights gained through the analysis, we propose a simple yet effective method, federated cross learning (FedCross), to tackle this challenging problem. Unlike the conventional FL methods that combine multiple individually trained local models on a server node, our FedCross sequentially trains the global model across different clients in a round-robin manner, and thus the entire training procedure does not involve any model aggregation steps. To further improve its performance to be comparable with the centralized learning method, we combine the FedCross with an ensemble learning mechanism to compose a federated cross ensemble learning (FedCrossEns) method. Finally, we conduct extensive experiments using a set of public datasets. The experimental results show that the proposed FedCross training strategy outperforms the mainstream FL methods on non-iid data. In addition to improving the segmentation performance, our FedCrossEns can further provide a quantitative estimation of the model uncertainty, demonstrating the effectiveness and clinical significance of our designs. Source code is publicly available at https://github.com/DIAL-RPI/FedCross.')
}}
{{ paper('A comparative evaluation of image-to-image translation methods for stain transfer in histopathology',
        'Igor Zingman, Sergio Frayle, Ivan Tankoyeu, Sergey Sukhanov, Fabian Heinemann',
        openreview='https://openreview.net/forum?id=leVAXRDthXI',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P164',
        paper='papers/P164',
        proceedings='',
        abstract="Image-to-image translation (I2I) methods allow the generation of artificial images that share the content of the original image but have a different style. With the advances in Generative Adversarial Networks (GANs)-based methods, I2I methods enabled the generation of artificial images that are indistinguishable from natural images. Recently, I2I methods were also employed in histopathology for generating artificial images of in silico stained tissues from a different type of staining. We refer to this process as stain transfer. The number of I2I variants is constantly increasing, which makes a well justified choice of the most suitable I2I methods for stain transfer challenging. In our work, we compare twelve stain transfer approaches, three of which are based on traditional and nine on GAN-based image processing methods. The analysis relies on complementary quantitative measures for the quality of image translation, the assessment of the suitability for deep learning-based tissue grading, and the visual evaluation by pathologists. Our study highlights the strengths and weaknesses of the stain transfer approaches, thereby allowing a rational choice of the underlying I2I algorithms. Code, data, and trained models for stain transfer between H&E and Masson\\'s Trichrome staining will be made available online.")
}}
{{ paper('OFDVDnet: A Sensor Fusion Approach for Video Denoising in Fluorescence-Guided Surgery',
        'Trevor Seets, Wei Lin, Yizhou Lu, Christie Lin, Adam Uselmann, Andreas Velten',
        openreview='https://openreview.net/forum?id=TcUtCXRcK8',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P178',
        paper='papers/P178',
        proceedings='',
        abstract='Many applications in machine vision and medical imaging require the capture of images from a scene with very low radiance, which may result in very noisy images and videos. An important example of such an application is the imaging of fluorescently-labeled tissue in fluorescence-guided surgery. Medical imaging systems, especially when intended to be used in surgery, are designed to operate in well-lit environments and use optical filters, time division, or other strategies that allow the simultaneous capture of low radiance fluorescence video and a well-lit visible light video of the scene. This work demonstrates video denoising can be dramatically improved by utilizing deep learning together with motion and textural cues from the noise-free video.')
}}
{{ paper('TransRP: Transformer-based PET/CT feature extraction incorporating clinical data for recurrence-free survival prediction in oropharyngeal cancer',
        'Baoqiang Ma, Jiapan Guo, Lisanne Van Dijk, P.M.A. van Ooijen, Stefan Both, Nanna Maria Sijtsema',
        openreview='https://openreview.net/forum?id=eF_6td_piu-',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P187',
        paper='papers/P187',
        proceedings='',
        abstract='The growing number of subtypes and treatment options for oropharyngeal squamous cell carcinoma (OPSCC), a common type of head and neck cancer (HNC), highlights the need for personalized therapies. Prognostic outcome prediction models can identify different risk groups for investigation of intensified or de-escalated treatment strategies. Convolution neural networks (CNNs) have been shown to have improved predictive performance compared to traditional clinical and radiomics models by extracting comprehensive and representative features. However, CNNs are limited in their ability to learn global features within an entire volume. In this study, we propose a Transformer-based model for predicting recurrence-free survival (RFS) in OPSCC patients, called TransRP. TransRP consists of a CNN encoder to extract rich PET/CT image features, a Transformer encoder to learn global context features, and a fully connected network to incorporate clinical data for RFS prediction. We investigated three different methods for combining clinical features into TransRP. The experiments were conducted using the public HECKTOR 2022 challenge dataset, which includes pretreatment PET/CT scans, Gross Tumor Volume masks, clinical data, and RFS for OPSCC patients. The dataset was split into a test set (n = 120) and a training set (n = 362) for five-fold cross-validation. The results show that TransRP achieved the highest test concordance index of 0.698 (an improvement > 2%) in RFS prediction compared to several state-of-the-art clinical and CNN-based methods. In addition, we found that incorporating clinical features with image features obtained from the Transformer encoder performed better than using the Transformer encoder to extract features from both clinical and image features. The code for this study is available at (anonymized temporarily for review).')
}}
{{ paper('SegPrompt: Using Segmentation Map as a Better Prompt to Finetune Deep Models for Kidney Stone Classification',
        'Wei Zhu, Runtao Zhou, Yuan Yao, Timothy Douglas Campbell, Rajat Kumar Jain, Jiebo Luo',
        openreview='https://openreview.net/forum?id=QXjGotk45lb',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P200',
        paper='papers/P200',
        proceedings='',
        abstract='Recently, deep learning has produced encouraging results for kidney stone classification using endoscope images. However, the shortage of annotated training data poses a severe problem in improving the performance and generalization ability of the trained model. It is thus crucial to fully exploit the limited data at hand. In this paper, we propose SegPrompt to alleviate the data shortage problems by exploiting segmentation maps from two aspects. First, SegPrompt integrates segmentation maps to facilitate classification training so that the classification model is aware of the regions of interest. The proposed method allows the image and segmentation tokens to interact with each other to fully utilize the segmentation map information. Second, we use the segmentation maps as prompts to tune the pretrained deep model, resulting in much fewer trainable parameters than vanilla finetuning. We perform extensive experiments on the collected kidney stone dataset. The results show that SegPrompt can achieve an advantageous balance between the model fitting ability and the generalization ability, eventually leading to an effective model with limited training data.')
}}
{{ paper('On Sensitivity and Robustness of Normalization Schemes to Input Distribution Shifts in Automatic MR Image Diagnosis',
        'Divyam Madaan, Daniel Sodickson, Kyunghyun Cho, Sumit Chopra',
        openreview='https://openreview.net/forum?id=iA0XwM0IU08',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P212',
        paper='papers/P212',
        proceedings='',
        abstract='Magnetic Resonance Imaging (MRI) is considered the gold standard of medical imaging because of the excellent soft-tissue contrast exhibited in the images reconstructed by the MR pipeline, which enables the human radiologist to discern many pathologies easily. More recently, Deep Learning (DL) models have also achieved state-of-the-art performance in diagnosing multiple diseases using these reconstructed images as input. However, the image reconstruction process within the MR pipeline, which requires the use of complex hardware and adjustment of a large number of scanner parameters, is highly susceptible to the noise of various forms resulting in arbitrary artifacts within the images. Furthermore, the noise distribution is not stationary and varies within a machine, across machines, and patients, leading to varying artifacts within the images. Unfortunately, DL models are quite sensitive to these varying artifacts as it leads to changes in the input data distribution between the training and testing phases. The lack of robustness of these models against varying artifacts impedes their use in medical applications where safety is critical. In this work, we focus on improving the generalization performance of these models in the presence of multiple varying artifacts that manifest due to the complexity of the MR data acquisition. In our experiments, we observe that Batch Normalization (BN), a widely used technique during the training of DL models for medical image analysis, is a significant cause of performance degradation in these changing environments. As a solution, we propose to use other normalization techniques, such as Group Normalization (GN) and Layer Normalization (LN), to inject robustness into model performance against varying image artifacts. Through a systematic set of experiments, we show that GN and LN provide better accuracy for various MR artifacts and distribution shifts.')
}}
{{ paper('One-Class SVM on siamese neural network latent space for Unsupervised Anomaly Detection on brain MRI White Matter Hyperintensities',
        'Nicolas Pinon, Robin Trombetta, Carole Lartizien',
        openreview='https://openreview.net/forum?id=_c9r6-HCEaN',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P217',
        paper='papers/P217',
        proceedings='',
        abstract='Anomaly detection remains a challenging task in neuroimaging when little to no supervision is available and when lesions can be very small or with subtle contrast. Patch-based representation learning has shown powerful representation capacities when applied to industrial or medical imaging and outlier detection methods have been applied successfully to these images. In this work, we propose an unsupervised anomaly detection (UAD) method based on a latent space constructed by a siamese patch-based auto-encoder and perform the outlier detection with a One-Class SVM training paradigm tailored to the lesion detection task in multi-modality neuroimaging. We evaluate performances of this model on a public database, the White Matter Hyperintensities (WMH) challenge and show in par performance with the two best performing state-of-the-art methods reported so far. ')
}}
{{ paper('nnUNet meets pathology: Bridging the gap for application to whole slide images and computational biomarkers',
        'Joey Spronck, Thijs Gelton, Leander van Eekelen, Joep Bogaerts, Leslie Tessier, Mart van Rijthoven, Lieke van der Woude, Michel van den Heuvel, Willemijn Theelen, Jeroen van der Laak, Francesco Ciompi',
        openreview='https://openreview.net/forum?id=aHuwlUu_QR',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P229',
        paper='papers/P229',
        proceedings='',
        abstract="Image segmentation is at the core of many tasks in medical imaging, including the engineering of computational biomarkers. While the self-configuring nnUNet framework for image segmentation tasks completely shifted the state-of-the-art in the radiology field, it has never been adapted to overcome its limitations for application on the pathology domain. Our study showcases the potential of nnUNet in computational pathology and bridges the gap that currently exists in utilizing nnUNet for pathology applications. Our proposed nnUNet for pathology framework has demonstrated its significance and potential to shift the state-of-the-art in the computational pathology field, as seen from the exceptional first-place segmentation ranking on the TIGER challenge\\'s experimental leaderboard 1. Our framework includes critical hyperparameter adjustments and pathology-specific color augmentations, as well as an essential WSI inference pipeline and a novel inference uncertainty approach that proves helpful for biomarker development. We release the code of our accurate and workflow-friendly segmentation tool to promote and foster growth within the computational pathology community.")
}}
{{ paper('Image2SSM: Localization-aware Deep Learning Framework for Statistical Shape Modeling Directly from Images',
        'Janmesh Ukey, Shireen Elhabian',
        openreview='https://openreview.net/forum?id=oRA8BPiduI',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P238',
        paper='papers/P238',
        proceedings='',
        abstract='Statistical Shape Modelling (SSM) is an effective tool for quantitatively analyzing anatom- ical populations. SSM has benefitted largely from advances in deep learning where statis- tical representations of anatomies (e.g., point distribution models or PDMs) are inferred directly from images, alleviating the need for a time-consuming and expensive workflow of anatomy segmentation, shape registration, and model optimization. Nonetheless, to date, existing deep learning methods do not consider the rigid pose transformation of shapes or anatomy of interest. They also require a tight bounding box to be defined over the image of anatomy-of-interest before feeding the image to the deep network for network training and inference. In this paper, we propose a deep learning framework that simultaneously detects and segments the anatomy of interest, estimate the rigid transformation with respect to the population mean (average) using a spatial transformer, and estimates the corresponding statistical representation of that anatomy, all directly from unsegmented 3D image without the need for any additional supervision. Furthermore, we leverage the segmentation task to provide an attention model for the sub-network that estimates shape representation, giving more accurate shape statistics for shape analysis.')
}}

# Tuesday, July 11

## Oral session 4 - Neuroimaging - 9:00 - 10:30am

[% .papers %]
{{ paper('MProtoNet: A Case-Based Interpretable Model for Brain Tumor Classification with 3D Multi-parametric Magnetic Resonance Imaging',
        'Yuanyuan Wei, Roger Tam, Xiaoying Tang',
        openreview='https://openreview.net/forum?id=6Wbj3QCo4U4',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O218',
        paper='papers/O218',
        proceedings='',
        abstract='Recent applications of deep convolutional neural networks in medical imaging raise concerns about their interpretability. While most explainable deep learning applications use post hoc methods (such as GradCAM) to generate feature attribution maps, there is a new type of case-based reasoning models, namely ProtoPNet and its variants, which identify prototypes during training and compare input image patches with those prototypes. We propose the first medical prototype network (MProtoNet) to extend ProtoPNet to brain tumor classification with 3D multi-parametric magnetic resonance imaging (mpMRI) data. To address different requirements between 2D natural images and 3D mpMRIs especially in terms of localizing attention regions, a new attention module with soft masking and online-CAM loss is introduced. Soft masking helps sharpen attention maps, while online-CAM loss directly utilizes image-level labels when training the attention module. MProtoNet achieves statistically significant improvements in interpretability metrics of both correctness and localization coherence (with a best activation precision of $0.713\\pm0.058$) without human-annotated labels during training, when compared with GradCAM and several ProtoPNet variants. The source code is available at https://github.com/aywi/mprotonet.')
}}
{{ paper('Decoding natural image stimuli from fMRI data with a surface-based convolutional network',
        'Zijin Gu, Keith Jamison, Amy Kuceyeski, Mert R. Sabuncu',
        openreview='https://openreview.net/forum?id=V5vvti2Y9PA',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O037',
        paper='papers/O037',
        proceedings='',
        abstract='Due to the low signal-to-noise ratio and limited resolution of functional MRI data, and the high complexity of natural images, reconstructing a visual stimulus from human brain fMRI measurements is a challenging task. In this work, we propose a novel approach for this task, which we call Cortex2Image, to decode visual stimuli with high semantic fidelity and rich fine-grained detail. In particular, we train a surface-based convolutional network model that maps from brain response to semantic image features first (Cortex2Semantic).  We then combine this model with a high-quality image generator (Instance-Conditioned GAN) to train another mapping from brain response to fine-grained image features using a variational approach (Cortex2Detail). Image reconstructions obtained by our proposed method achieve state-of-the-art semantic fidelity, while yielding good fine-grained similarity with the ground-truth stimulus. Our code is available on \\url{https://github.com/zijin-gu/meshconv-decoding.git}.')
}}
{{ paper('Pre-Training Transformers for Fingerprinting to Improve Stress Prediction in fMRI',
        'Gony Rosenman, Itzik Malkiel, Ayam Greental, Talma Hendler, Lior Wolf',
        openreview='https://openreview.net/forum?id=W9qI8DwoUFF',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O077',
        paper='papers/O077',
        proceedings='',
        abstract='We harness a Transformer-based model and a pre-training procedure for fingerprinting on fMRI data, to enhance the accuracy of stress predictions. Our model, called MetricFMRI, first optimizes a pixel-based reconstruction loss. In a second unsupervised training phase, a triplet loss is used to encourage fMRI sequences of the same subject to have closer representations, while sequences from different subjects are pushed away from each other. Finally, supervised learning is used for the target task, based on the learned representation. We evaluate the performance of our model and other alternatives and conclude that the triplet training for the fingerprinting task is key to the improved accuracy of our method for the task of stress prediction. To obtain insights regarding the learned model, gradient-based explainability techniques are used, indicating that sub-cortical brain regions that are known to play a central role in stress-related processes are highlighted by the model. ')
}}
{{ paper('E(3) x SO(3)-Equivariant Networks for Spherical Deconvolution in Diffusion MRI',
        'Axel Elaldi, Guido Gerig, Neel Dey',
        openreview='https://openreview.net/forum?id=lri_iAbpn_r',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O134',
        paper='papers/O134',
        proceedings='',
        abstract='We present Roto-Translation Equivariant Spherical Deconvolution (RT-ESD), an $E(3)\\times SO(3)$ equivariant framework for sparse deconvolution of volumes where each voxel contains a spherical signal. Such 6D data naturally arises in diffusion MRI (dMRI), a medical imaging modality widely used to measure microstructure and structural connectivity. As each dMRI voxel is typically a mixture of various overlapping structures, there is a need for blind deconvolution to recover crossing anatomical structures such as white matter tracts. Existing dMRI work takes either an iterative or deep learning approach to sparse spherical deconvolution, yet it typically does not account for relationships between neighboring measurements. This work constructs equivariant deep learning layers which respect to symmetries of spatial rotations, reflections, and translations, alongside the symmetries of voxelwise spherical rotations. As a result, RT-ESD improves on previous work across several tasks including fiber recovery on the DiSCo dataset, deconvolution-derived partial volume estimation on real-world in vivo human brain dMRI, and improved downstream reconstruction of fiber tractograms on the Tractometer dataset. The code will be released.')
}}
{{ paper('Amortized Normalizing Flows for Transcranial Ultrasound with Uncertainty Quantification',
        'Rafael Orozco, Mathias Louboutin, Ali Siahkoohi, Gabrio Rizzuti, Tristan van Leeuwen, Felix Johan Herrmann',
        openreview='https://openreview.net/forum?id=LoJG-lUIlk',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O159',
        paper='papers/O159',
        proceedings='',
        abstract='We present a novel approach to transcranial ultrasound computed tomography that utilizes normalizing flows to improve the speed of imaging and provide Bayesian uncertainty quantification. Our method combines physics-informed methods and data-driven methods to accelerate the reconstruction of the final image. We make use of a physics-informed summary statistic to incorporate the known ultrasound physics with the goal of compressing large incoming observations. This compression enables efficient training of the normalizing flow and standardizes the size of the data regardless of imaging configurations. The combinations of these methods results in fast uncertainty-aware image reconstruction that generalizes to a variety of transducer configurations. We evaluate our approach with in silico experiments and demonstrate that it can significantly improve the imaging speed while quantifying uncertainty. We validate the quality of our image reconstructions by comparing against the traditional physics-only method and also verify that our provided uncertainty is calibrated with the error. ')
}}
{{ paper('Data Consistent Deep Rigid MRI Motion Correction',
        'Nalini M Singh, Neel Dey, Malte Hoffmann, Bruce Fischl, Elfar Adalsteinsson, Robert Frost, Adrian V Dalca, Polina Golland',
        openreview='https://openreview.net/forum?id=KolMbwNBNGv',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O177',
        paper='papers/O177',
        proceedings='',
        abstract='Motion artifacts are a pervasive problem in MRI, leading to misdiagnosis or mischaracterization in population-level imaging studies. Current retrospective rigid intra-slice motion correction techniques jointly optimize estimates of the image and the motion parameters. In this paper, we use a deep network to reduce the joint image-motion parameter search to a search over rigid motion parameters alone. Our network produces a reconstruction as a function of two inputs: corrupted k-space data and motion parameters. We train the network using simulated, motion-corrupted k-space data generated from known motion parameters. At test-time, we estimate unknown motion parameters by minimizing a data consistency loss between the motion parameters, the network-based image reconstruction given those parameters, and the acquired measurements. Intra-slice motion correction experiments on simulated and realistic 2D fast spin echo brain MRI achieve high reconstruction fidelity while retaining the benefits of explicit data consistency-based optimization.')
}}
[% / %]

## Oral session 5 - Semi-supervised/self-supervised methods - 2:00 - 3:00pm

[% .papers %]
{{ paper('Vision-Language Modelling For Radiological Imaging and Reports In The Low Data Regime',
        'Rhydian Windsor, Amir Jamaludin, Timor Kadir, Andrew Zisserman',
        openreview='https://openreview.net/forum?id=2XVITHcQCfj',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O024',
        paper='papers/O024',
        proceedings='',
        abstract='This paper explores training medical vision-language models (VLMs) -- where the visual and language inputs are embedded into a common space -- with a particular focus on scenarios where training data is limited, as is often the case in clinical datasets. We explore several candidate methods to improve low-data performance, including: (i) adapting generic pre-trained models to novel image and text domains (i.e.\\ medical imaging and reports) via unimodal self-supervision; (ii) using local (e.g.\\ GLoRIA) \\& global (e.g. InfoNCE) contrastive loss functions as well as a combination of the two; (iii) extra supervision during VLM training, via: (a) image- and text-only self-supervision, and (b) creating additional positive image-text pairs for training through augmentation and nearest-neighbour search.  Using text-to-image retrieval as a benchmark, we evaluate the performance of these methods with variable sized training datasets of paired chest X-rays and radiological reports.  Combined, they significantly improve retrieval compared to fine-tuning CLIP, roughly equivalent to training with $10\\times$ the data. A similar pattern is found in the downstream task classification of CXR-related conditions with our method outperforming CLIP and also BioVIL, a strong CXR VLM benchmark, in the zero-shot and linear probing settings. We conclude with a set of recommendations for researchers aiming to train vision-language models on other medical imaging modalities when training data is scarce. To facilitate further research, we will make our code and models publicly available.  ')
}}
{{ paper('Learning to Compare Longitudinal Images',
        'Heejong Kim, Mert R. Sabuncu',
        openreview='https://openreview.net/forum?id=l17YFzXLP53',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O160',
        paper='papers/O160',
        proceedings='',
        abstract='Longitudinal studies, where a series of images from the same set of individuals are acquired at different time-points, represent a popular technique for studying and characterizing temporal dynamics in biomedical applications. The classical approach for longitudinal comparison involves normalizing for nuisance variations, such as image orientation or contrast differences, via pre-processing. Statistical analysis is, in turn, conducted to detect changes of interest, either at the individual or population level. This classical approach can suffer from pre-processing issues and limitations of the statistical modeling. For example, normalizing for nuisance variation might be hard in settings where there are a lot of idiosyncratic changes. In this paper, we present a simple machine learning-based approach that can alleviate these issues. In our approach, we train a deep learning model (called PaIRNet, for Pairwise Image Ranking Network) to compare pairs of longitudinal images, with or without supervision. In the self-supervised setup, for instance, the model is trained to temporally order the images, which requires learning to recognize time-irreversible changes. Our results from four datasets demonstrate that PaIRNet can be very effective in localizing and quantifying meaningful longitudinal changes while discounting nuisance variation. Our code is available at \\url{https://github.com/heejong-kim/learning-to-compare-longitudinal-images}')
}}
{{ paper('Exploring Image Augmentations for Siamese Representation Learning with Chest X-Rays',
        'Rogier Van der Sluijs, Nandita Bhaskhar, Daniel Rubin, Curtis Langlotz, Akshay S Chaudhari',
        openreview='https://openreview.net/forum?id=xkmhsBITaCw',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O221',
        paper='papers/O221',
        proceedings='',
        abstract='Image augmentations are quintessential for effective visual representation learning across self-supervised learning techniques. While augmentation strategies for natural imaging have been studied extensively, medical images are vastly different from their natural counterparts. Thus, it is unknown whether common augmentation strategies employed in Siamese representation learning generalize to medical images and to what extent. To address this challenge, in this study, we systematically assess the effect of various augmentations on the quality and robustness of the learned representations. We train and evaluate Siamese Networks for abnormality detection on chest X-Rays across three large datasets (MIMIC-CXR, CheXpert and VinDr-CXR). We investigate the efficacy of the learned representations through experiments involving linear probing, fine-tuning, zero-shot transfer, and data efficiency. Finally, we identify a set of augmentations that yield robust representations that generalize well to both out-of-distribution data and diseases, while outperforming supervised baselines using just zero-shot transfer and linear probes by up to 20%.')
}}
{{ paper('Self-Supervised CSF Inpainting for Improved Accuracy Validation of Cortical Surface Analyses ',
        'Jiacheng Wang, Kathleen Larson, Ipek Oguz',
        openreview='https://openreview.net/forum?id=HR1GtDQnuw',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O063',
        paper='papers/O063',
        proceedings='',
        abstract='Accuracy validation of cortical thickness measurement is a difficult problem due to the lack of ground truth data. To address this need, many methods have been developed to synthetically induce gray matter (GM) atrophy in an MRI via deformable registration, creating a set of images with known changes in cortical thickness. However, these methods often cause blurring in atrophied regions, and cannot simulate realistic atrophy within deep sulci where cerebrospinal fluid (CSF) is obscured or absent. In this paper, we present a solution using a self-supervised inpainting model to generate CSF in these regions and create images with more plausible GM/CSF boundaries. Specifically, we introduce a novel, 3D GAN model that incorporates patch-based dropout training, edge map priors, and sinusoidal positional encoding, all of which are established methods previously limited to 2D domains. We show that our framework significantly improves the quality of the resulting synthetic images and is adaptable to unseen data with fine-tuning. We also demonstrate that our resulting dataset can be employed for accuracy validation of cortical segmentation and thickness measurement.')
}}
[% / %]

## Oral session 6 - Synthesis - 4:00 - 5:00pm

[% .papers %]
{{ paper('CP2Image: Generating high-quality single-cell images using CellProfiler representations',
        'Yanni Ji, Marie Cutiongco, Bjørn Sand Jensen, Ke Yuan',
        openreview='https://openreview.net/forum?id=4LqtcKZoKeB',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O125',
        paper='papers/O125',
        proceedings='',
        abstract='Single-cell high-throughput microscopy images contain key biological information underlying normal and pathological cellular processes. Image-based analysis and profiling are powerful and promising for extracting this information but are made difficult due to substantial complexity and heterogeneity in cellular phenotype. Hand-crafted methods and machine learning models are popular ways to extract cell image information. Representations extracted via machine learning models, which often exhibit good reconstruction performance, lack biological interpretability. Hand-crafted representations, on the contrary, have clear biological meanings and thus are interpretable. Whether these hand-crafted representations can also generate realistic images is not clear. In this paper, we propose a CellProfiler to image (CP2Image) model that can directly generate realistic cell images from CellProfiler representations. We also demonstrate most biological information encoded in the CellProfiler representations is well-preserved in the generating process. This is the first time hand-crafted representations be shown to have generative ability and provide researchers with an intuitive way for their further analysis.')
}}
{{ paper('Ultra-NeRF: Neural Radiance Fields for Ultrasound Imaging',
        'Magdalena Wysocki, Mohammad Farid Azampour, Christine Eilers, Benjamin Busam, Mehrdad Salehi, Nassir Navab',
        openreview='https://openreview.net/forum?id=x4McMBwVyi',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O190',
        paper='papers/O190',
        proceedings='',
        abstract='We present a physics-enhanced implicit neural representation (INR) for ultrasound (US) imaging that learns tissue properties from overlapping US sweeps. Our proposed method leverages a ray-tracing-based neural rendering for novel view US synthesis. Recent publications demonstrated that INR models could encode a representation of a three-dimensional scene from a set of two-dimensional US frames. However, these models fail to consider the view-dependent changes in appearance and geometry intrinsic to US imaging. In our work, we discuss direction-dependent changes in the scene and show that a physics-inspired rendering improves the fidelity of US image synthesis. In particular, we demonstrate experimentally that our proposed method generates geometrically accurate B-mode images for regions with ambiguous representation owing to view-dependent differences of the US images. We conduct our experiments using simulated B-mode US sweeps of the liver and acquired US sweeps of a spine phantom tracked with a robotic arm. The experiments corroborate that our method generates US frames that enable consistent volume compounding from previously unseen views. To the best of our knowledge, the presented work is the first to address view-dependent US image synthesis using INR.')
}}
{{ paper('Bi-parametric prostate MR image synthesis using pathology and sequence-conditioned stable diffusion',
        'Shaheer U. Saeed, Tom Syer, Wen Yan, Qianye Yang, Mark Emberton, Shonit Punwani, Matthew John Clarkson, Dean Barratt, Yipeng Hu',
        openreview='https://openreview.net/forum?id=3QnxUSzR7iu',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O053',
        paper='papers/O053',
        proceedings='',
        abstract='We propose an image synthesis mechanism for multi-sequence prostate MR images conditioned on text, to control lesion presence and sequence, as well as to generate paired bi-parametric images conditioned on images e.g. for generating diffusion-weighted MR from T2-weighted MR for paired data, which are two challenging tasks in pathological image synthesis. Our proposed mechanism utilises and builds upon the recent stable diffusion model by proposing image-based conditioning for paired data generation. We validate our method using 2D image slices from real suspected prostate cancer patients. The realism of the synthesised images is validated by means of a blind expert evaluation for identifying real versus fake images, where a radiologist with 4 years experience reading urological MR only achieves 59.4\\% accuracy across all tested sequences (where chance is 50\\%). For the first time, we evaluate the realism of the generated pathology by blind expert identification of the presence of suspected lesions, where we find that the clinician performs similarly for both real and synthesised images, with a 2.9 percentage point difference in lesion identification accuracy between real and synthesised images, demonstrating the potentials in radiological training purposes. Furthermore, we also show that a machine learning model, trained for lesion identification, shows better performance (76.2\\% vs 70.4\\%, statistically significant improvement) when trained with real data augmented by synthesised data as opposed to training with only real images, demonstrating usefulness for model training.')
}}
{{ paper('Know Your Space: Inlier and Outlier Construction for Calibrating Medical OOD Detectors',
        'Vivek Narayanaswamy, Yamen Mubarka, Rushil Anirudh, Deepta Rajan, Andreas Spanias, Jayaraman J. Thiagarajan',
        openreview='https://openreview.net/forum?id=RU7fr0-M8N',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O069',
        paper='papers/O069',
        proceedings='',
        abstract='We focus on the problem of producing well-calibrated out-of-distribution (OOD) detectors, in order to enable safe deployment of medical image classifiers. Motivated by the difficulty of curating suitable calibration datasets, synthetic augmentations have become highly prevalent for inlier/outlier specification. While there have been rapid advances in data augmentation techniques, this paper makes a striking finding that the space in which the inliers and outliers are synthesized, in addition to the type of augmentation, plays a critical role in calibrating OOD detectors. Using the popular energy-based OOD detection framework, we find that the optimal protocol is to synthesize latent-space inliers along with diverse pixel-space outliers. Based on empirical studies with multiple medical imaging benchmarks, we demonstrate that our approach consistently leads to superior OOD detection ($15\\% - 35\\%$ in AUROC) over the state-of-the-art in a variety of open-set recognition settings.')
}}
[% / %]

## Posters - 10:30am - 12:00pm & 3:00pm - 4:00pm

[% .papers %]
{{ paper('Amortized Normalizing Flows for Transcranial Ultrasound with Uncertainty Quantification',
        'Rafael Orozco, Mathias Louboutin, Ali Siahkoohi, Gabrio Rizzuti, Tristan van Leeuwen, Felix Johan Herrmann',
        openreview='https://openreview.net/forum?id=LoJG-lUIlk',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O159',
        paper='papers/O159',
        proceedings='',
        abstract='We present a novel approach to transcranial ultrasound computed tomography that utilizes normalizing flows to improve the speed of imaging and provide Bayesian uncertainty quantification. Our method combines physics-informed methods and data-driven methods to accelerate the reconstruction of the final image. We make use of a physics-informed summary statistic to incorporate the known ultrasound physics with the goal of compressing large incoming observations. This compression enables efficient training of the normalizing flow and standardizes the size of the data regardless of imaging configurations. The combinations of these methods results in fast uncertainty-aware image reconstruction that generalizes to a variety of transducer configurations. We evaluate our approach with in silico experiments and demonstrate that it can significantly improve the imaging speed while quantifying uncertainty. We validate the quality of our image reconstructions by comparing against the traditional physics-only method and also verify that our provided uncertainty is calibrated with the error. ')
}}
{{ paper('Bi-parametric prostate MR image synthesis using pathology and sequence-conditioned stable diffusion',
        'Shaheer U. Saeed, Tom Syer, Wen Yan, Qianye Yang, Mark Emberton, Shonit Punwani, Matthew John Clarkson, Dean Barratt, Yipeng Hu',
        openreview='https://openreview.net/forum?id=3QnxUSzR7iu',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O053',
        paper='papers/O053',
        proceedings='',
        abstract='We propose an image synthesis mechanism for multi-sequence prostate MR images conditioned on text, to control lesion presence and sequence, as well as to generate paired bi-parametric images conditioned on images e.g. for generating diffusion-weighted MR from T2-weighted MR for paired data, which are two challenging tasks in pathological image synthesis. Our proposed mechanism utilises and builds upon the recent stable diffusion model by proposing image-based conditioning for paired data generation. We validate our method using 2D image slices from real suspected prostate cancer patients. The realism of the synthesised images is validated by means of a blind expert evaluation for identifying real versus fake images, where a radiologist with 4 years experience reading urological MR only achieves 59.4\\% accuracy across all tested sequences (where chance is 50\\%). For the first time, we evaluate the realism of the generated pathology by blind expert identification of the presence of suspected lesions, where we find that the clinician performs similarly for both real and synthesised images, with a 2.9 percentage point difference in lesion identification accuracy between real and synthesised images, demonstrating the potentials in radiological training purposes. Furthermore, we also show that a machine learning model, trained for lesion identification, shows better performance (76.2\\% vs 70.4\\%, statistically significant improvement) when trained with real data augmented by synthesised data as opposed to training with only real images, demonstrating usefulness for model training.')
}}
{{ paper('CP2Image: Generating high-quality single-cell images using CellProfiler representations',
        'Yanni Ji, Marie Cutiongco, Bjørn Sand Jensen, Ke Yuan',
        openreview='https://openreview.net/forum?id=4LqtcKZoKeB',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O125',
        paper='papers/O125',
        proceedings='',
        abstract='Single-cell high-throughput microscopy images contain key biological information underlying normal and pathological cellular processes. Image-based analysis and profiling are powerful and promising for extracting this information but are made difficult due to substantial complexity and heterogeneity in cellular phenotype. Hand-crafted methods and machine learning models are popular ways to extract cell image information. Representations extracted via machine learning models, which often exhibit good reconstruction performance, lack biological interpretability. Hand-crafted representations, on the contrary, have clear biological meanings and thus are interpretable. Whether these hand-crafted representations can also generate realistic images is not clear. In this paper, we propose a CellProfiler to image (CP2Image) model that can directly generate realistic cell images from CellProfiler representations. We also demonstrate most biological information encoded in the CellProfiler representations is well-preserved in the generating process. This is the first time hand-crafted representations be shown to have generative ability and provide researchers with an intuitive way for their further analysis.')
}}
{{ paper('Data Consistent Deep Rigid MRI Motion Correction',
        'Nalini M Singh, Neel Dey, Malte Hoffmann, Bruce Fischl, Elfar Adalsteinsson, Robert Frost, Adrian V Dalca, Polina Golland',
        openreview='https://openreview.net/forum?id=KolMbwNBNGv',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O177',
        paper='papers/O177',
        proceedings='',
        abstract='Motion artifacts are a pervasive problem in MRI, leading to misdiagnosis or mischaracterization in population-level imaging studies. Current retrospective rigid intra-slice motion correction techniques jointly optimize estimates of the image and the motion parameters. In this paper, we use a deep network to reduce the joint image-motion parameter search to a search over rigid motion parameters alone. Our network produces a reconstruction as a function of two inputs: corrupted k-space data and motion parameters. We train the network using simulated, motion-corrupted k-space data generated from known motion parameters. At test-time, we estimate unknown motion parameters by minimizing a data consistency loss between the motion parameters, the network-based image reconstruction given those parameters, and the acquired measurements. Intra-slice motion correction experiments on simulated and realistic 2D fast spin echo brain MRI achieve high reconstruction fidelity while retaining the benefits of explicit data consistency-based optimization.')
}}
{{ paper('Decoding natural image stimuli from fMRI data with a surface-based convolutional network',
        'Zijin Gu, Keith Jamison, Amy Kuceyeski, Mert R. Sabuncu',
        openreview='https://openreview.net/forum?id=V5vvti2Y9PA',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O037',
        paper='papers/O037',
        proceedings='',
        abstract='Due to the low signal-to-noise ratio and limited resolution of functional MRI data, and the high complexity of natural images, reconstructing a visual stimulus from human brain fMRI measurements is a challenging task. In this work, we propose a novel approach for this task, which we call Cortex2Image, to decode visual stimuli with high semantic fidelity and rich fine-grained detail. In particular, we train a surface-based convolutional network model that maps from brain response to semantic image features first (Cortex2Semantic).  We then combine this model with a high-quality image generator (Instance-Conditioned GAN) to train another mapping from brain response to fine-grained image features using a variational approach (Cortex2Detail). Image reconstructions obtained by our proposed method achieve state-of-the-art semantic fidelity, while yielding good fine-grained similarity with the ground-truth stimulus. Our code is available on \\url{https://github.com/zijin-gu/meshconv-decoding.git}.')
}}
{{ paper('E(3) x SO(3)-Equivariant Networks for Spherical Deconvolution in Diffusion MRI',
        'Axel Elaldi, Guido Gerig, Neel Dey',
        openreview='https://openreview.net/forum?id=lri_iAbpn_r',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O134',
        paper='papers/O134',
        proceedings='',
        abstract='We present Roto-Translation Equivariant Spherical Deconvolution (RT-ESD), an $E(3)\\times SO(3)$ equivariant framework for sparse deconvolution of volumes where each voxel contains a spherical signal. Such 6D data naturally arises in diffusion MRI (dMRI), a medical imaging modality widely used to measure microstructure and structural connectivity. As each dMRI voxel is typically a mixture of various overlapping structures, there is a need for blind deconvolution to recover crossing anatomical structures such as white matter tracts. Existing dMRI work takes either an iterative or deep learning approach to sparse spherical deconvolution, yet it typically does not account for relationships between neighboring measurements. This work constructs equivariant deep learning layers which respect to symmetries of spatial rotations, reflections, and translations, alongside the symmetries of voxelwise spherical rotations. As a result, RT-ESD improves on previous work across several tasks including fiber recovery on the DiSCo dataset, deconvolution-derived partial volume estimation on real-world in vivo human brain dMRI, and improved downstream reconstruction of fiber tractograms on the Tractometer dataset. The code will be released.')
}}
{{ paper('Exploring Image Augmentations for Siamese Representation Learning with Chest X-Rays',
        'Rogier Van der Sluijs, Nandita Bhaskhar, Daniel Rubin, Curtis Langlotz, Akshay S Chaudhari',
        openreview='https://openreview.net/forum?id=xkmhsBITaCw',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O221',
        paper='papers/O221',
        proceedings='',
        abstract='Image augmentations are quintessential for effective visual representation learning across self-supervised learning techniques. While augmentation strategies for natural imaging have been studied extensively, medical images are vastly different from their natural counterparts. Thus, it is unknown whether common augmentation strategies employed in Siamese representation learning generalize to medical images and to what extent. To address this challenge, in this study, we systematically assess the effect of various augmentations on the quality and robustness of the learned representations. We train and evaluate Siamese Networks for abnormality detection on chest X-Rays across three large datasets (MIMIC-CXR, CheXpert and VinDr-CXR). We investigate the efficacy of the learned representations through experiments involving linear probing, fine-tuning, zero-shot transfer, and data efficiency. Finally, we identify a set of augmentations that yield robust representations that generalize well to both out-of-distribution data and diseases, while outperforming supervised baselines using just zero-shot transfer and linear probes by up to 20%.')
}}
{{ paper('Know Your Space: Inlier and Outlier Construction for Calibrating Medical OOD Detectors',
        'Vivek Narayanaswamy, Yamen Mubarka, Rushil Anirudh, Deepta Rajan, Andreas Spanias, Jayaraman J. Thiagarajan',
        openreview='https://openreview.net/forum?id=RU7fr0-M8N',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O069',
        paper='papers/O069',
        proceedings='',
        abstract='We focus on the problem of producing well-calibrated out-of-distribution (OOD) detectors, in order to enable safe deployment of medical image classifiers. Motivated by the difficulty of curating suitable calibration datasets, synthetic augmentations have become highly prevalent for inlier/outlier specification. While there have been rapid advances in data augmentation techniques, this paper makes a striking finding that the space in which the inliers and outliers are synthesized, in addition to the type of augmentation, plays a critical role in calibrating OOD detectors. Using the popular energy-based OOD detection framework, we find that the optimal protocol is to synthesize latent-space inliers along with diverse pixel-space outliers. Based on empirical studies with multiple medical imaging benchmarks, we demonstrate that our approach consistently leads to superior OOD detection ($15\\% - 35\\%$ in AUROC) over the state-of-the-art in a variety of open-set recognition settings.')
}}
{{ paper('Learning to Compare Longitudinal Images',
        'Heejong Kim, Mert R. Sabuncu',
        openreview='https://openreview.net/forum?id=l17YFzXLP53',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O160',
        paper='papers/O160',
        proceedings='',
        abstract='Longitudinal studies, where a series of images from the same set of individuals are acquired at different time-points, represent a popular technique for studying and characterizing temporal dynamics in biomedical applications. The classical approach for longitudinal comparison involves normalizing for nuisance variations, such as image orientation or contrast differences, via pre-processing. Statistical analysis is, in turn, conducted to detect changes of interest, either at the individual or population level. This classical approach can suffer from pre-processing issues and limitations of the statistical modeling. For example, normalizing for nuisance variation might be hard in settings where there are a lot of idiosyncratic changes. In this paper, we present a simple machine learning-based approach that can alleviate these issues. In our approach, we train a deep learning model (called PaIRNet, for Pairwise Image Ranking Network) to compare pairs of longitudinal images, with or without supervision. In the self-supervised setup, for instance, the model is trained to temporally order the images, which requires learning to recognize time-irreversible changes. Our results from four datasets demonstrate that PaIRNet can be very effective in localizing and quantifying meaningful longitudinal changes while discounting nuisance variation. Our code is available at \\url{https://github.com/heejong-kim/learning-to-compare-longitudinal-images}')
}}
{{ paper('MProtoNet: A Case-Based Interpretable Model for Brain Tumor Classification with 3D Multi-parametric Magnetic Resonance Imaging',
        'Yuanyuan Wei, Roger Tam, Xiaoying Tang',
        openreview='https://openreview.net/forum?id=6Wbj3QCo4U4',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O218',
        paper='papers/O218',
        proceedings='',
        abstract='Recent applications of deep convolutional neural networks in medical imaging raise concerns about their interpretability. While most explainable deep learning applications use post hoc methods (such as GradCAM) to generate feature attribution maps, there is a new type of case-based reasoning models, namely ProtoPNet and its variants, which identify prototypes during training and compare input image patches with those prototypes. We propose the first medical prototype network (MProtoNet) to extend ProtoPNet to brain tumor classification with 3D multi-parametric magnetic resonance imaging (mpMRI) data. To address different requirements between 2D natural images and 3D mpMRIs especially in terms of localizing attention regions, a new attention module with soft masking and online-CAM loss is introduced. Soft masking helps sharpen attention maps, while online-CAM loss directly utilizes image-level labels when training the attention module. MProtoNet achieves statistically significant improvements in interpretability metrics of both correctness and localization coherence (with a best activation precision of $0.713\\pm0.058$) without human-annotated labels during training, when compared with GradCAM and several ProtoPNet variants. The source code is available at https://github.com/aywi/mprotonet.')
}}
{{ paper('Pre-Training Transformers for Fingerprinting to Improve Stress Prediction in fMRI',
        'Gony Rosenman, Itzik Malkiel, Ayam Greental, Talma Hendler, Lior Wolf',
        openreview='https://openreview.net/forum?id=W9qI8DwoUFF',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O077',
        paper='papers/O077',
        proceedings='',
        abstract='We harness a Transformer-based model and a pre-training procedure for fingerprinting on fMRI data, to enhance the accuracy of stress predictions. Our model, called MetricFMRI, first optimizes a pixel-based reconstruction loss. In a second unsupervised training phase, a triplet loss is used to encourage fMRI sequences of the same subject to have closer representations, while sequences from different subjects are pushed away from each other. Finally, supervised learning is used for the target task, based on the learned representation. We evaluate the performance of our model and other alternatives and conclude that the triplet training for the fingerprinting task is key to the improved accuracy of our method for the task of stress prediction. To obtain insights regarding the learned model, gradient-based explainability techniques are used, indicating that sub-cortical brain regions that are known to play a central role in stress-related processes are highlighted by the model. ')
}}
{{ paper('Self-Supervised CSF Inpainting for Improved Accuracy Validation of Cortical Surface Analyses ',
        'Jiacheng Wang, Kathleen Larson, Ipek Oguz',
        openreview='https://openreview.net/forum?id=HR1GtDQnuw',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O063',
        paper='papers/O063',
        proceedings='',
        abstract='Accuracy validation of cortical thickness measurement is a difficult problem due to the lack of ground truth data. To address this need, many methods have been developed to synthetically induce gray matter (GM) atrophy in an MRI via deformable registration, creating a set of images with known changes in cortical thickness. However, these methods often cause blurring in atrophied regions, and cannot simulate realistic atrophy within deep sulci where cerebrospinal fluid (CSF) is obscured or absent. In this paper, we present a solution using a self-supervised inpainting model to generate CSF in these regions and create images with more plausible GM/CSF boundaries. Specifically, we introduce a novel, 3D GAN model that incorporates patch-based dropout training, edge map priors, and sinusoidal positional encoding, all of which are established methods previously limited to 2D domains. We show that our framework significantly improves the quality of the resulting synthetic images and is adaptable to unseen data with fine-tuning. We also demonstrate that our resulting dataset can be employed for accuracy validation of cortical segmentation and thickness measurement.')
}}
{{ paper('Ultra-NeRF: Neural Radiance Fields for Ultrasound Imaging',
        'Magdalena Wysocki, Mohammad Farid Azampour, Christine Eilers, Benjamin Busam, Mehrdad Salehi, Nassir Navab',
        openreview='https://openreview.net/forum?id=x4McMBwVyi',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O190',
        paper='papers/O190',
        proceedings='',
        abstract='We present a physics-enhanced implicit neural representation (INR) for ultrasound (US) imaging that learns tissue properties from overlapping US sweeps. Our proposed method leverages a ray-tracing-based neural rendering for novel view US synthesis. Recent publications demonstrated that INR models could encode a representation of a three-dimensional scene from a set of two-dimensional US frames. However, these models fail to consider the view-dependent changes in appearance and geometry intrinsic to US imaging. In our work, we discuss direction-dependent changes in the scene and show that a physics-inspired rendering improves the fidelity of US image synthesis. In particular, we demonstrate experimentally that our proposed method generates geometrically accurate B-mode images for regions with ambiguous representation owing to view-dependent differences of the US images. We conduct our experiments using simulated B-mode US sweeps of the liver and acquired US sweeps of a spine phantom tracked with a robotic arm. The experiments corroborate that our method generates US frames that enable consistent volume compounding from previously unseen views. To the best of our knowledge, the presented work is the first to address view-dependent US image synthesis using INR.')
}}
{{ paper('Vision-Language Modelling For Radiological Imaging and Reports In The Low Data Regime',
        'Rhydian Windsor, Amir Jamaludin, Timor Kadir, Andrew Zisserman',
        openreview='https://openreview.net/forum?id=2XVITHcQCfj',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O024',
        paper='papers/O024',
        proceedings='',
        abstract='This paper explores training medical vision-language models (VLMs) -- where the visual and language inputs are embedded into a common space -- with a particular focus on scenarios where training data is limited, as is often the case in clinical datasets. We explore several candidate methods to improve low-data performance, including: (i) adapting generic pre-trained models to novel image and text domains (i.e.\\ medical imaging and reports) via unimodal self-supervision; (ii) using local (e.g.\\ GLoRIA) \\& global (e.g. InfoNCE) contrastive loss functions as well as a combination of the two; (iii) extra supervision during VLM training, via: (a) image- and text-only self-supervision, and (b) creating additional positive image-text pairs for training through augmentation and nearest-neighbour search.  Using text-to-image retrieval as a benchmark, we evaluate the performance of these methods with variable sized training datasets of paired chest X-rays and radiological reports.  Combined, they significantly improve retrieval compared to fine-tuning CLIP, roughly equivalent to training with $10\\times$ the data. A similar pattern is found in the downstream task classification of CXR-related conditions with our method outperforming CLIP and also BioVIL, a strong CXR VLM benchmark, in the zero-shot and linear probing settings. We conclude with a set of recommendations for researchers aiming to train vision-language models on other medical imaging modalities when training data is scarce. To facilitate further research, we will make our code and models publicly available.  ')
}}
{{ paper('Making Your First Choice: To Address Cold Start Problem in Medical Active Learning',
        'Liangyu Chen, Yutong Bai, Siyu Huang, Yongyi Lu, Bihan Wen, Alan Yuille, Zongwei Zhou',
        openreview='https://openreview.net/forum?id=5iSBMWm3ln',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P003',
        paper='papers/P003',
        proceedings='',
        abstract='Active learning promises to improve annotation efficiency by iteratively selecting the most important data to be annotated first. However, we uncover a striking contradiction to this promise: at the first few choices, active learning fails to select data as efficiently as random selection. We identify this as the cold start problem in active learning, caused by a biased and outlier initial query. This paper seeks to address the cold start problem and develops a novel active querying strategy, named HaCon, that can exploit the three advantages of contrastive learning: (1) no annotation is required; (2) label diversity is ensured by pseudo-labels to mitigate bias; (3) typical data is determined by contrastive features to reduce outliers. Experiments on three public medical datasets show that HaCon not only significantly outperforms existing active querying strategies but also surpasses random selection by a large margin. Code is available at https://github.com/liangyuch/CSVAL.')
}}
{{ paper('Robust Detection Outcome: A Metric for Pathology Detection in Medical Images',
        'Felix Meissen, Philip Müller, Georgios Kaissis, Daniel Rueckert',
        openreview='https://openreview.net/forum?id=zyiJi4sJ7dZ',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P010',
        paper='papers/P010',
        proceedings='',
        abstract='Detection of pathologies is a fundamental task in medical imaging and the evaluation of algorithms that can perform this task automatically is crucial. However, current object detection metrics for natural images do not reflect the specific clinical requirements in pathology detection sufficiently. To tackle this problem, we propose Robust Detection Outcome (RoDeO); a novel metric for evaluating algorithms for pathology detection in medical images, especially in chest X-rays. RoDeO evaluates different errors directly and individually, and reflects clinical needs better than current metrics. Extensive evaluation on the ChestX-ray8 dataset shows the superiority of our metrics compared to existing ones. We released the code at [https://github.com/FeliMe/RoDeO](https://github.com/FeliMe/RoDeO) and published RoDeO as pip package ($rodeometric$).')
}}
{{ paper('SVD-DIP: Overcoming the Overfitting Problem in DIP-based CT Reconstruction',
        'Marco Nittscher, Michael Falk Lameter, Riccardo Barbano, Johannes Leuschner, Bangti Jin, Peter Maass',
        openreview='https://openreview.net/forum?id=ivC7VP2mof',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P014',
        paper='papers/P014',
        proceedings='',
        abstract='The deep image prior (DIP) is a well-established unsupervised deep learning method for image reconstruction; yet it is far from being flawless. The DIP overfits to noise if not early stopped, or optimized via a regularized objective. We build on the regularized fine-tuning of a pretrained DIP, by adopting a novel strategy that restricts the learning to the adaptation of singular values. The proposed SVD-DIP uses ad hoc convolutional layers whose pretrained parameters are decomposed via the singular value decomposition. Optimizing the DIP then solely consists in the fine-tuning of the singular values, while keeping the left and right singular vectors fixed. We thoroughly validate the proposed method on real-measured μCT data of a lotus root as well as two medical datasets (LoDoPaB and Mayo). We report significantly improved stability of the DIP optimization, by overcoming the overfitting to noise.')
}}
{{ paper('ViT-AE++: Improving Vision Transformer Autoencoder for Self-supervised Medical Image Representations',
        'Chinmay Prabhakar, Hongwei Li, Jiancheng Yang, Suprosanna Shit, Benedikt Wiestler, bjoern menze',
        openreview='https://openreview.net/forum?id=2Aoi0VKPOWT',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P023',
        paper='papers/P023',
        proceedings='',
        abstract='Self-supervised learning has attracted increasing attention as it learns data-driven representation from data without annotations. Vision transformer-based autoencoder (ViT-AE) by He et al. (2021) is a recent self-supervised learning technique that employs a patch-masking strategy to learn a meaningful latent space. In this paper, we focus on improving ViT-AE (nicknamed ViT-AE++) for a more effective representation of both 2D and 3D medical images. We propose two new loss functions to enhance the representation during the training stage. The first loss term aims to improve self-reconstruction by considering the structured dependencies and hence indirectly improving the representation. The second loss term leverages contrastive loss to directly optimize the representation from two randomly masked views. As an independent contribution, we extended ViT-AE++ to a 3D fashion for volumetric medical images.  We extensively evaluate ViT-AE++ on both natural images and medical images, demonstrating consistent improvement over vanilla ViT-AE and its superiority over other contrastive learning approaches.')
}}
{{ paper('Deformable Image Registration with Geometry-informed Implicit Neural Representations',
        'Louis van Harten, Rudolf Leonardus Mirjam Van Herten, Jaap Stoker, Ivana Isgum',
        openreview='https://openreview.net/forum?id=Pj9vtDIzSCE',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P035',
        paper='papers/P035',
        proceedings='',
        abstract='Deformable image registration is a crucial component in the analysis of motion in time series. In medical data, the deformation fields are often predictable to a certain degree: the muscles and other tissues causing the motion-of-interest form shapes that may be used as a geometric prior. Using an Implicit Neural Representation to parameterize a deformation field allows the coordinate space to be chosen arbitrarily. We propose to curve this coordinate space around anatomical structures that influence the motion in our time series, yielding a space that is aligned with the expected motion. The geometric information is therefore explicitly encoded into the neural representation, reducing the complexity of the optimized deformation function. We design and evaluate this concept using an abdominal 3D cine-MRI dataset, where the motion of interest is bowel motility. We align the coordinate system of the neural representations with automatically extracted centerlines of the small intestine. We show that explicitly encoding the intestine geometry in the neural representations improves registration accuracy for bowel loops with active motility when compared to registration using neural representations in the original coordinate system. Additionally, we show that registration accuracy can be further improved using a model that combines a neural representation in image coordinates with a separate neural representation that operates in the proposed tangent coordinate system. This approach may improve the efficiency of deformable registration when describing motion-of-interest that is influenced by the shape of anatomical structures.')
}}
{{ paper('3D Medical Axial Transformer: A Lightweight Transformer Model for 3D Brain Tumor Segmentation',
        'Cheng Liu, Hisanor Kiryu',
        openreview='https://openreview.net/forum?id=PX-jt92kQUM',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P050',
        paper='papers/P050',
        proceedings='',
        abstract='In recent years, Transformer-based models have gained attention in the field of medical image segmentation, with research exploring ways to integrate them with established architectures such as Unet. However, the high computational demands of these models have led most current approaches to focus on segmenting 2D slices of MRI or CT images, which can limit the ability of the model to learn semantic information in the depth axis and result in output with uneven edges. Additionally, the small size of medical image datasets, particularly those for brain tumor segmentation, poses a challenge for training transformer models. To address these issues, we propose 3D Medical Axial Transformer (MAT), a lightweight, end-to-end model for 3D brain tumor segmentation that employs an axial attention mechanism to reduce computational demands and self-distillation to improve performance on small datasets. Results indicate that our approach, which has fewer parameters and a simpler structure than other models, achieves superior performance and produces clearer output boundaries, making it more suitable for clinical applications.')
}}
{{ paper('Joint cortical registration of geometry and function using semi-supervised learning',
        'Jian Li, Greta Tuckute, Evelina Fedorenko, Brian L Edlow, Bruce Fischl, Adrian V Dalca',
        openreview='https://openreview.net/forum?id=n9v_BuIcY7G',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P062',
        paper='papers/P062',
        proceedings='',
        abstract='Brain surface-based image registration, an important component of brain image analysis, establishes spatial correspondence between cortical surfaces. Existing iterative and learning-based approaches focus on accurate registration of folding patterns of the cerebral cortex, and assume that geometry predicts function and thus functional areas will also be well aligned. However, structure/functional variability of anatomically corresponding areas across subjects has been widely reported. In this work, we introduce a learning-based cortical registration framework, JOSA, which jointly aligns folding patterns and functional maps while simultaneously learning an optimal atlas. We demonstrate that JOSA can substantially improve registration performance in both anatomical and functional domains over existing methods. By employing a semi-supervised training strategy, the proposed framework obviates the need for functional data during inference, enabling its use in broad neuroscientific domains where functional data may not be observed. The source code of JOSA will be released to the public at https://voxelmorph.net.')
}}
{{ paper('Semantic Segmentation of 3D Medical Images Through a Kaleidoscope: Data from the Osteoarthritis Initiative',
        'Boyeong Woo, Marlon Bran Lorenzana, Craig Engstrom, William Baresic, Jurgen Fripp, Stuart Crozier, Shekhar S. Chandra',
        openreview='https://openreview.net/forum?id=80ZHtBKHKHo',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P070',
        paper='papers/P070',
        proceedings='',
        abstract='While there have been many studies on using deep learning for medical image analysis, the lack of manually annotated data remains a challenge in training a deep learning model for segmentation of medical images. This work shows how the kaleidoscope transform (KT) can be applied to a 3D convolutional neural network to improve its generalizability when the training set is extremely small. In this study, the KT was applied to a context aggregation network (CAN) for semantic segmentation of anatomical structures in knee MR images. In the proposed model, KAN3D, the input image is rearranged into a batch of downsampled images (KT) before the convolution operations, and then the voxels are rearranged back to their original positions (inverse KT) after the convolution operations to produce the predicted segmentation mask for the input image. Compared to the CAN3D (without the KT), the KAN3D was able to reduce overfitting without data augmentation while maintaining a fast training and inference time. The paper discusses the observed advantages and disadvantages of KAN3D.')
}}
{{ paper('Whole brain radiomics for clustered federated personalization in brain tumor segmentation',
        'Matthis Manthe, Stefan Duffner, Carole Lartizien',
        openreview='https://openreview.net/forum?id=1CyXExO15K',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P075',
        paper='papers/P075',
        proceedings='',
        abstract='Federated learning and its application to medical image segmentation have recently become a popular research topic. This training paradigm suffers from statistical heterogeneity between participating institutions’ local datasets, incurring convergence slowdown as well as potential accuracy loss compared to classical training.  To mitigate this effect, federated personalization emerged as the federated optimization of one model per distribution. We propose a novel personalization algorithm tailored to the feature shift induced by the usage of different scanners and acquisition parameters by different institutions. This method is the first to account for both inter and intra-institution feature shifts (multiple scanners used in a single institution). It is based on the computation, within each centre, of a series of radiomic features capturing the global texture of each 3D image volume, followed by a clustering analysis pooling all feature vectors transferred from the local institutions to the central server. Each computed clustered decentralized dataset (potentially including data from different institutions) then serves to finetune a global model obtained through classical federated learning. We validate our approach on the Federated Brain Tumor Segmentation 2022 Challenge dataset (FeTS2022).')
}}
{{ paper('Incomplete learning of multi-modal connectome for brain disorder diagnosis via modal-mixup and deep supervision',
        'Yanwu Yang, Hairui Chen, Zhikai Chang, Yang Xiang, Chenfei Ye, Ting Ma',
        openreview='https://openreview.net/forum?id=WjrcYNTPunQ',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P082',
        paper='papers/P082',
        proceedings='',
        abstract='Recently, the study of multi-modal brain networks has dramatically facilitated the efficiency in brain disorder diagnosis by characterizing multiple types of connectivity of brain networks and their intrinsic complementary information. Despite the promising performance achieved by multi-modal technologies, most existing multi-modal approaches can only learn from samples with complete modalities, which wastes a considerable amount of mono-modal data. Otherwise, most existing data imputation approaches still rely on a large number of samples with complete modalities. In this study, we propose a modal-mixup data imputation method by randomly sampling incomplete samples and synthesizing them into complete data for auxiliary training. Moreover, to mitigate the noise in the complementary information between unpaired modalities in the synthesized data, we introduce a bilateral network with deep supervision for improving and regularizing mono-modal representations with disease-specific information. Experiments on the ADNI dataset demonstrate the superiority of our proposed method for disease classification in terms of different rates of samples with complete modalities.')
}}
{{ paper('Considerations for data acquisition and modeling strategies: Mitosis detection in computational pathology',
        'Zongliang Ji, Philip Rosenfield, Christina Eng, Sarah Bettigole, Danielle C Gibson, Hamid Masoudi, Matthew Hanna, Nicolo Fusi, Kristen A Severson',
        openreview='https://openreview.net/forum?id=RyV4J_PjNv',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P087',
        paper='papers/P087',
        proceedings='',
        abstract='Preparing data for machine learning tasks in health and life science applications requires decisions that affect the cost, model properties and performance. In this work, we study the implication of data collection strategies, focusing on a case study of mitosis detection. Specifically, we investigate the use of expert and crowd-sourced labelers, the impact of aggregated vs single labels, and the framing of the problem as either classification or object detection. Our results demonstrate the value of crowd-sourced labels, importance of uncertainty quantification, and utility of negative samples. ')
}}
{{ paper('Automatic 3D/2D Deformable Registration in Minimally Invasive Liver Resection using a Mesh Recovery Network',
        'Mathieu Labrunie, Daniel Pizarro, Christophe Tilmant, Adrien Bartoli',
        openreview='https://openreview.net/forum?id=nG87JqzSMc',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P105',
        paper='papers/P105',
        proceedings='',
        abstract="We propose the patient-specific Liver Mesh Recovery (LMR) framework, to automatically achieve Augmented Reality (AR) guidance by registering a preoperative 3D model in Minimally Invasive Liver Resection (MILR). Existing methods solve registration in MILR by pose estimation followed with numerical optimisation and suffer from a prohibitive intraoperative runtime. The proposed LMR is inspired by the recent Human Mesh Recovery (HMR) framework and forms the first learning-based method to solve registration in MILR. In contrast to existing methods, the computation load in LMR occurs preoperatively, at training time. We construct a patient-specific deformation model and generate patient-specific training data reproducing the typical defects of the automatically detected registration primitives. Experimental results show that LMR\\'s registration accuracy is on par with optimisation-based methods, whilst running in real-time intraoperatively.")
}}
{{ paper('Improving Stain Invariance of CNNs for Segmentation by Fusing Channel Attention and Domain-Adversarial Training',
        'Kudaibergen Abutalip, Numan Saeed, Mustaqeem Khan, Abdulmotaleb El Saddik',
        openreview='https://openreview.net/forum?id=uZ1SVZgEJ02',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P118',
        paper='papers/P118',
        proceedings='',
        abstract='Variability in staining protocols, such as different slide preparation techniques, chemicals, and scanner configurations, can result in a diverse set of whole slide images (WSIs). This distribution shift can negatively impact the performance of deep learning models on unseen samples, presenting a significant challenge for developing new computational pathology applications. In this study, we propose a method for improving the generalizability of convolutional neural networks (CNNs) to stain changes in a single-source setting for semantic segmentation. Recent studies indicate that style features mainly exist as covariances in earlier network layers. We design a channel attention mechanism based on these findings that detects stain-specific features and modify the previously proposed stain-invariant training scheme. We reweigh the outputs of earlier layers and pass them to the stain-adversarial training branch. We evaluate our method on multi-center, multi-stain datasets and demonstrate its effectiveness through interpretability analysis. Our approach achieves substantial improvements over baselines and competitive performance compared to other methods, as measured by various evaluation metrics. We also show that combining our method with stain augmentation leads to mutually beneficial results and outperforms other techniques. Overall, our study makes significant contributions to the field of computational pathology.')
}}
{{ paper('Automatic Patient-level Diagnosis of Prostate Disease with Fused 3D MRI and Tabular Clinical Data',
        'Oleksii Bashkanov, Marko Rak, Lucas Engelage, Christianus Hansen',
        openreview='https://openreview.net/forum?id=Oji7tGC4oI',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P128',
        paper='papers/P128',
        proceedings='',
        abstract='Computer-aided diagnosis systems for automatic prostate cancer diagnosis can provide radiologists with decision support during image reading. However, in this case, patient-relevant information often remains unexploited due to the greater focus on the image recognition side, with various imaging devices and modalities, while omitting other potentially valuable clinical data. Therefore, our work investigates the performance of recent methods for the fusion of rich image data and heterogeneous tabular data. Those data may include patient demographics as well as laboratory data, e.g., prostate-specific antigen (PSA). Experiments on the large dataset (3800 subjects) indicated that when using the fusion method with demographic data in clinically significant prostate cancer (csPCa) detection tasks, the mean area under the receiver operating characteristic curve (ROC AUC) has improved significantly from 0.736 to 0.765. We also observed that the naïve concatenation performs similarly or even better than the \\mbox{state-of-the-art} fusion modules. We also achieved better prediction quality in grading prostate disease by including more samples from longitudinal PSA profiles in the tabular feature set. Thus, by including the three last PSA samples per patient, the best-performing model has reached AUC of 0.794 and a quadratic weighted kappa score (QWK) of 0.464, which constitutes a significant improvement compared with the image-only method, with ROC AUC of 0.736 and QWK of 0.342.')
}}
{{ paper('Reproducibility of Training Deep Learning Models for Medical Image Analysis',
        'Joeran Bosma, Dre Peeters, Natália Alves, Anindo Saha, Zaigham Saghir, Colin Jacobs, henkjan huisman',
        openreview='https://openreview.net/forum?id=MR01DcGST9',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P133',
        paper='papers/P133',
        proceedings='',
        abstract='Performance of deep learning algorithms varies due to their development data and training method, but also due to several stochastic processes during training. Due to these random factors, a single training run may not accurately reflect the performance of a given training method. Statistical comparisons in literature between different deep learning training methods typically ignore this performance variation between training runs and incorrectly claim significance of changes in training method. We hypothesize that the impact of such performance variation is substantial, such that it may invalidate biomedical competition leaderboards and some scientific papers. To test this, we investigate the reproducibility of training deep learning algorithms for medical image analysis. We repeated training runs from prior scientific studies: three diagnostic tasks (pancreatic cancer detection in CT, clinically significant prostate cancer detection in MRI, and lung nodule malignancy risk estimation in low-dose CT) and two organ segmentation tasks (pancreas segmentation in CT and prostate segmentation in MRI). A previously published top-performing algorithm for each task was trained multiple times to determine the variance in model performance. For all three diagnostic algorithms, performance variation from retraining was significant compared to data variance. Statistically comparing independently trained algorithms from the same training method using the same dataset should follow the null hypothesis, but we observed claimed significance with a p-value below 0.05 in $15\\%$ of comparisons with conventional testing (paired bootstrapping). We conclude that variance in model performance due to retraining is substantial and should be accounted for. ')
}}
{{ paper('DBGSL: Dynamic Brain Graph Structure Learning',
        'Alexander Campbell, Antonio Giuliano Zippo, Luca Passamonti, Nicola Toschi, Pietro Lio',
        openreview='https://openreview.net/forum?id=Us31horKNLG',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P138',
        paper='papers/P138',
        proceedings='',
        abstract='Recently, graph neural networks (GNNs) have shown success at learning representations of brain graphs derived from functional magnetic resonance imaging (fMRI) data. The majority of existing GNN methods, however, assume brain graphs are static over time and the graph adjacency matrix is known prior to model training. These assumptions are at odds with neuroscientific evidence that brain graphs are time-varying with a connectivity structure that depends on the choice of functional connectivity measure. Noisy brain graphs that do not truly represent the underling fMRI data can have a detrimental impact on the performance of GNNs. As a solution, we propose Dynamic Brain Graph Structure Learning (DBGSL), a novel method for learning the optimal time-varying dependency structure of fMRI data induced by a downstream prediction task. Experiments demonstrate DBGSL achieves state-of-the-art performance for sex classification using real-world resting-state and task fMRI data. Moreover, analysis of the learnt dynamic graphs highlights prediction-related brain regions which align with existing neuroscience literature.')
}}
{{ paper('Alleviating tiling effect by random walk sliding window in high-resolution histological whole slide image synthesis',
        'Shunxing Bao, Ho Hin Lee, Qi Yang, Lucas Walker Remedios, Ruining Deng, Can Cui, Leon Yichen Cai, Kaiwen Xu, Xin Yu, Sophie Chiron, Yike Li, Nathan Heath Patterson, Yaohong Wang, Jia Li, Qi Liu, Ken S. Lau, Joseph T. Roland, Lori A. Coburn, Keith T. Wilson, Bennett A. Landman, Yuankai Huo',
        openreview='https://openreview.net/forum?id=uZl3yA2dBt',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P146',
        paper='papers/P146',
        proceedings='',
        abstract='Multiplex immunofluorescence (MxIF) is an advanced molecular imaging technique that can simultaneously provide biologists with multiple (i.e., more than 20) molecular markers on a single histological tissue section. Unfortunately, due to imaging restrictions, the more routinely used hematoxylin and eosin (H&E) stain is typically unavailable with MxIF on the same tissue section. As biological H&E staining is not feasible, previous efforts have been made to obtain H&E whole slide image (WSI) from MxIF via deep learning empowered virtual staining. However, the tiling effect is a long-lasting problem in high-resolution WSI-wise synthesis. The MxIF to H&E synthesis is no exception. Limited by computational resources, the cross-stain image synthesis is typically performed at the patch-level. Thus, discontinuous intensities might be visually identified along with the patch boundaries assembling all individual patches back to a WSI. In this work, we propose a deep learning based unpaired high-resolution image synthesis method to obtain virtual H&E WSIs from MxIF WSIs (each with 27 markers/stains) with reduced tiling effects. Briefly, we first extend the CycleGAN framework by adding simultaneous nuclei and mucin segmentation supervision as spatial constraints. Then, we introduce a random sliding window shifting strategy during the optimized inference stage to alleviate the tiling effects. The validation results show that our spatially constrained synthesis method achieves a 56% performance gain for the downstream cell segmentation task. The proposed inference method reduces the tiling effects by using 50% fewer computation resources without compromising performance. The proposed random sliding window inference method is a plug-and-play module, which can be generalized and used for other high-resolution WSI image synthesis applications.')
}}
{{ paper('Evaluating the Fairness of Deep Learning Uncertainty Estimates in Medical Image Analysis',
        'Raghav Mehta, Changjian Shui, Tal Arbel',
        openreview='https://openreview.net/forum?id=Pd4_U5ZzEY',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P161',
        paper='papers/P161',
        proceedings='',
        abstract="Although deep learning (DL) models have shown great success in many medical image analysis tasks, deployment of the resulting models into  real clinical contexts requires: (1) that they exhibit robustness and fairness across different sub-populations, and (2) that the confidence in DL model predictions be accurately expressed in the form of uncertainties. Unfortunately, recent studies have indeed shown significant biases in DL models across demographic subgroups (e.g., race, sex, age) in the context of medical image analysis, indicating a lack of fairness in the models. Although several methods have been proposed in the ML literature to mitigate a lack of fairness in DL models, they focus entirely on the absolute performance between groups without considering their effect on uncertainty estimation. In this work, we present the first exploration of the effect of popular fairness models on overcoming biases across subgroups in medical image analysis in terms of bottom-line performance, and their effects on uncertainty quantification. We perform extensive experiments on three different clinically relevant tasks: (i) skin lesion classification, (ii) brain tumour segmentation, and (iii) Alzheimer\\'s disease clinical score regression. Our results indicate that popular ML methods, such as data-balancing and distributionally robust optimization, succeed in mitigating fairness issues in terms of the model performances for some of the tasks. However, this can come at the cost of poor uncertainty estimates associated with the model predictions. This tradeoff must be mitigated if fairness models are to be adopted in medical image analysis. ")
}}
{{ paper('Multi-scale Hierarchical Vision Transformer with Cascaded Attention Decoding for Medical Image Segmentation',
        'Md Mostafijur Rahman, Radu Marculescu',
        openreview='https://openreview.net/forum?id=u0MHV19E2n',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P165',
        paper='papers/P165',
        proceedings='',
        abstract='Transformers have shown great success in medical image segmentation. However, transformers may exhibit a limited generalization ability due to the underlying single-scale self-attention (SA) mechanism. In this paper, we address this issue by introducing a Multi-scale hiERarchical vIsion Transformer (MERIT) backbone network, which improves the generalizability of the model by computing SA at multiple scales. We also incorporate an attention-based decoder, namely Cascaded Attention Decoding (CASCADE), for further refinement of multi-stage features generated by MERIT. Finally, we introduce an effective multi-stage feature mixing loss aggregation (MUTATION) method for better model training via implicit ensembling. Our experiments on two widely used medical image segmentation benchmarks (i.e., Synapse Multi-organ, ACDC) demonstrate the superior performance of MERIT over state-of-the-art methods. Our MERIT architecture and MUTATION loss aggregation can be used with downstream medical image and semantic segmentation tasks.')
}}
{{ paper('Toward Unpaired Multi-modal Medical Image Segmentation via Learning Structured Semantic Consistency',
        'Jie Yang, Ye Zhu, Chaoqun Wang, Zhen Li, Ruimao Zhang',
        openreview='https://openreview.net/forum?id=e9qGhrfP1v',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P181',
        paper='papers/P181',
        proceedings='',
        abstract='Integrating multi-modal data to promote medical image analysis has recently gained great attention. This paper presents a novel scheme to learn the mutual benefits of different modalities to achieve better segmentation results for unpaired multi-modal medical images. Our approach tackles two critical issues of this task from a practical perspective: (1) how to effectively learn the semantic consistencies of various modalities (e.g., CT and MRI), and (2) how to leverage the above consistencies to regularize the network learning while preserving its simplicity. To address (1), we leverage a carefully designed External Attention Module (EAM) to align semantic class representations and their correlations of different modalities. To solve (2), the proposed EAM is designed as an external plug-and-play one, which can be discarded once the model is optimized. We have demonstrated the effectiveness of the proposed method on two medical image segmentation scenarios: (1) cardiac structure segmentation, and (2) abdominal multi-organ segmentation. Extensive results show that the proposed method outperforms its counterparts by a wide margin.')
}}
{{ paper('Trainable Prototype Enhanced Multiple Instance Learning for Whole Slide Image Classification',
        'Litao Yang, Deval Mehta, Sidong Liu, Dwarikanath Mahapatra, Antonio Di Ieva, Zongyuan Ge',
        openreview='https://openreview.net/forum?id=P3tSZhxBwJw',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P189',
        paper='papers/P189',
        proceedings='',
        abstract='Digital pathology based on whole slide images (WSIs) plays a key role in cancer diagnosis and clinical practice. Due to the high resolution of the WSI and unavailability of patch level annotations, WSI classification is usually formulated as a weakly supervised problem, which relies on multiple instance learning (MIL) based on patches of a WSI. In this paper, we aim to learn an optimal patch-level feature space by integrating prototype learning with MIL. To this end, we develop a Trainable Prototype enhanced deep MIL (TPMIL) framework for weakly supervised WSI classification. In contrast to the conventional methods which rely on a certain number of selected patches for feature space refinement, we softly cluster all the instances by allocating them to their corresponding prototypes. Additionally, our method is able to reveal the correlations between different tumor subtypes through distances between corresponding trained prototypes. More importantly, TPMIL also enables to provide a more accurate interpretability based on the distance of the instances from the trained prototypes which serves as an alternative to the conventional attention score-based interpretability. We test our method on two WSI datasets and it achieves a new SOTA.')
}}
{{ paper('Intra- and Inter-Cellular Awareness for 3D Neuron Tracking and Segmentation in Large-Scale Connectomics',
        'Hao Zhai, Jing Liu, Bei Hong, Jiazheng Liu, Qiwei Xie, Hua Han',
        openreview='https://openreview.net/forum?id=3_qtVh7gTyy',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P201',
        paper='papers/P201',
        proceedings='',
        abstract='Currently, most state-of-the-art pipelines for 3D micro-connectomic reconstruction deal with neuron over-segmentation, agglomeration and subcellular compartment (nuclei, mitochondria, synapses, etc.) detection separately. Inspired by the proofreading consensus of experts, we established a paradigm to acquire priori knowledge of cellular characteristics and ultrastructures, as well as determine the connectivity of neural circuits simultaneously. Following this novel paradigm, we were keen to bring the Intra- and Inter-Cellular Awareness back when Tracking and Segmenting neurons in connectomics. Our proposed method (II-CATS) utilizes few-shot learning techniques to encode the internal neurite representation and its learnable components, which could significantly impact neuron tracings. We further go beyond the original expected run length (ERL) metric by focusing on biological constraints (bERL) or spanning from the nucleus to spines (nERL). With the evaluation of these metrics, we perform typical experiments on multiple electron microscopy datasets on diverse animals and scales. In particular, our proposed method is naturally suitable for tracking neurons that have been identified by staining.')
}}
{{ paper('Selective experience replay compression using coresets for lifelong deep reinforcement learning in medical imaging',
        'Guangyao Zheng, Samson Zhou, Vladimir Braverman, Michael A. Jacobs, Vishwa Sanjay Parekh',
        openreview='https://openreview.net/forum?id=pP3p0rmeyRb',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P213',
        paper='papers/P213',
        proceedings='',
        abstract='Selective experience replay is a popular strategy for integrating lifelong learning with deep reinforcement learning. Selective experience replay aims to recount selected experiences from previous tasks to avoid catastrophic forgetting. Furthermore, selective experience replay based techniques are model agnostic and allow experiences to be shared across different models. However, storing experiences from all previous tasks make lifelong learning using selective experience replay computationally very expensive and impractical as the number of tasks increase. To that end, we propose a reward distribution-preserving coreset compression technique for compressing experience replay buffers stored for selective experience replay.   We evaluated the coreset lifelong deep reinforcement learning technique on the brain tumor segmentation (BRATS) dataset for the task of ventricle localization and on the whole-body MRI for localization of left knee cap, left kidney, right trochanter, left lung, and spleen. The coreset lifelong learning models trained on a sequence of 10 different brain MR imaging environments demonstrated excellent performance localizing the ventricle with a mean pixel error distance of 12.93, 13.46, 17.75, and 18.55 for the compression ratios of 10x, 20x, 30x, and 40x, respectively. In comparison, the conventional lifelong learning model localized the ventricle with a mean pixel distance of 10.87. Similarly, the coreset lifelong learning models trained on whole-body MRI demonstrated no significant difference (p=0.28) between the 10x compressed coreset lifelong learning models and conventional lifelong learning models for all the landmarks. The mean pixel distance for the 10x compressed models across all the landmarks was 25.30, compared to 19.24 for the conventional lifelong learning models. Our results demonstrate that the potential of the coreset-based ERB compression method for compressing experiences without a significant drop in performance.')
}}
{{ paper('A deep learning method trained on synthetic data for digital breast tomosynthesis reconstruction',
        'Arnaud Quillent, Vincent Jonas Bismuth, Isabelle Bloch, Christophe Kervazo, Said Ladjal',
        openreview='https://openreview.net/forum?id=xcMTcyk2v69',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P219',
        paper='papers/P219',
        proceedings='',
        abstract='Digital Breast Tomosynthesis (DBT) is an X-ray imaging modality enabling the reconstruction of 3D volumes of breasts. DBT is mainly used for cancer screening, and is intended to replace conventional mammography in the coming years. However, DBT reconstructions are impeded by several types of artefacts induced by the geometry of the device itself, degrading the image quality and limiting its resolution along the thickness of the compressed breast. In this study, we propose a deep-learning-based pipeline to address the DBT reconstruction problem, focusing on the removal of sparse-view and limited-angle artefacts. Specifically, this procedure is composed of two steps: a classic reconstruction algorithm is first applied on normalised projections, then a deep neural network is tasked with erasing the artefacts present in the obtained volumes. A major difficulty to solve our problem is the lack of real conditions artefact-free data. To overcome this complication, we resort to a new dataset comprised of synthetic breast texture phantoms. We then show that our training method and database strategy are promising to tackle the problem as they improve the informational value of planes orthogonal to the detector, which are not currently used by radiologists due to their poor quality. Eventually, we assess the impact of removing the bias components from the network and using stacks of slices as inputs, with regard to the generalisation ability of our approach on both synthetic and clinical data.')
}}
{{ paper('Estimating Uncertainty in PET Image Reconstruction via Deep Posterior Sampling',
        'Tin Vlašić, Tomislav Matulić, Damir Seršić',
        openreview='https://openreview.net/forum?id=oqPQke7xz2',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P235',
        paper='papers/P235',
        proceedings='',
        abstract='Positron emission tomography (PET) is an important functional medical imaging technique often used in the evaluation of certain brain disorders, whose reconstruction problem is ill-posed. The vast majority of reconstruction methods in PET imaging, both iterative and deep learning, return a single estimate without quantifying the associated uncertainty. Due to ill-posedness and noise, a single solution can be misleading or inaccurate. Thus, providing a measure of uncertainty in PET image reconstruction can help medical practitioners in making critical decisions. This paper proposes a deep learning-based method for uncertainty quantification in PET image reconstruction via posterior sampling. The method is based on training a conditional generative adversarial network whose generator approximates sampling from the posterior in Bayesian inversion. The generator is conditioned on reconstruction from a low-dose PET scan obtained by a conventional reconstruction method and a high-quality magnetic resonance image and learned to estimate a corresponding standard-dose PET scan reconstruction. We show that the proposed model generates high-quality posterior samples and yields physically-meaningful uncertainty estimates.')
}}
{{ paper('Effect of Intensity Standardization on Deep Learning for WML Segmentation in Multi-Centre FLAIR MRI',
        'Abdollah Ghazvanchahi, Pejman Jahbedar Maralani, Alan R. Moody, April Khademi',
        openreview='https://openreview.net/forum?id=sp-X1rXn8_',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P243',
        paper='papers/P243',
        proceedings='',
        abstract='Deep learning (DL) methods for white matter lesion (WML) segmentation in MRI suffer a reduction in performance when applied on data from a scanner or centre that is out-of-distribution (OOD) from the training data. This is critical for translation and widescale adoption, since current models cannot be readily applied to data from new institutions.  In this work, we evaluate several intensity standardization methods for MRI as a preprocessing step for WML segmentation in multi-centre Fluid-Attenuated Inversion Recovery (FLAIR) MRI. We evaluate a method specifically developed for FLAIR MRI called IAMLAB along with other popular normalization techniques such as White-strip, Nyul and Z-score. We proposed an Ensemble model that combines predictions from each of these models.  A skip-connection UNet (SC UNet) was trained on the standardized images, as well as the original data and segmentation performance was evaluated over several dimensions. The training (in-distribution) data consists of a single study, of 60 volumes, and the test (OOD) data is 128 unseen volumes from three clinical cohorts. Results show IAMLAB and Ensemble provide higher WML segmentation performance compared to models from original data or other normalization methods. IAMLAB & Ensemble have the highest dice similarity coefficient (DSC) on the in-distribution data (0.78 & 0.80) and on clinical OOD data. DSC was significantly higher for IAMLAB compared to the original data (p<0.05) for all lesion categories (LL>25mL: 0.77 vs. 0.71; 10mL<= LL<25mL: 0.66 vs. 0.61; LL<10mL: 0.53 vs. 0.52).  The IAMLAB and Ensemble normalization methods are mitigating MRI domain shift and are optimal for DL-based WML segmentation in unseen FLAIR data.')
}}
[% / %]

# Wednesday, July 12

## Oral session 7 - Segmentation 2 - 9:15 - 10:00am (note the late start as the virtual poster session wraps up at 9am)
[% .papers %]
{{ paper('MMCFormer: Missing Modality Compensation Transformer for Brain Tumor Segmentation',
        'Sanaz Karimijafarbigloo, Reza Azad, Amirhossein Kazerouni, Saeed Ebadollahi, Dorit Merhof',
        openreview='https://openreview.net/forum?id=PD0ASSmvlE',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O115',
        paper='papers/O115',
        proceedings='',
        abstract='Human brain tumours and more specifically gliomas are amongst the most life-threatening cancers which usually arise from abnormal growth of the glial stem cells. In practice, Magnetic Resonance Imaging (MRI) modalities, which offer different contrasts to elucidate tissue properties, provide comprehensive information regarding the brain’s structure and also potential clues for detecting tumors. Hence, multi-modal MRI is commonly utilized for the diagnosis of brain tumors. However, since the set of acquired modalities may vary between clinical sites, brain tumor studies may miss one or two MRI modalities. To address missing information in an end-to-end manner, we propose MMCFormer, a novel missing modality compensation network. Our strategy builds upon 3D efficient transformer blocks and uses a co-training strategy to effectively train a missing modality network. To ensure feature consistency in a multi-scale fashion, MMCFormer utilizes global contextual agreement modules in each scale of the encoders. Furthermore, to transfer modality-specific representations, we propose to incorporate auxiliary tokens in the bottleneck stage to model interaction between full and missing-modality paths. On top of that, we include feature consistency losses to reduce the domain gap in network prediction and increase the prediction reliability for the missing modality path. Extensive experiments on the BraTS 2018 dataset demonstrate the benefits of our approach compared to competing approaches. The implementation code will be publicly available after the paper acceptance.')
}}
{{ paper('Improving Segmentation of Objects with Varying Sizes in Biomedical Images using Instance-wise and Center-of-Instance Segmentation Loss Function',
        'Febrian Rachmadi, Charissa Poon, henrik skibbe',
        openreview='https://openreview.net/forum?id=8o83y0_YtE',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O130',
        paper='papers/O130',
        proceedings='',
        abstract='In this paper, we propose a novel two-component loss for biomedical image segmentation tasks called the Instance-wise and Center-of-Instance (ICI) loss, a loss function that addresses the instance imbalance problem commonly encountered when using pixel-wise loss functions such as the Dice loss. The Instance-wise component improves the detection of small instances or blobs\\" in image datasets with both large and small instances. The Center-of-Instance component improves the overall detection accuracy. We compared the ICI loss with two existing losses, the Dice loss and the blob loss, in the task of stroke lesion segmentation using the ATLAS R2.0 challenge dataset from MICCAI 2022. Compared to the other losses, the ICI loss provided a better balanced segmentation, and significantly outperformed the Dice loss with an improvement of $1.7-3.7\\%$ and the blob loss by $0.6-5.0\\%$ in terms of the Dice similarity coefficient on both validation and test set, suggesting that the ICI loss is a potential solution to the instance imbalance problem.')
}}
{{ paper('GeoLS: Geodesic Label Smoothing for Image Segmentation',
        'Sukesh Adiga Vasudeva, Jose Dolz, Herve Lombaert',
        openreview='https://openreview.net/forum?id=mTIP1bkmR0q',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O236',
        paper='papers/O236',
        proceedings='',
        abstract='Smoothing hard-label assignments has emerged as a popular strategy in training discriminative models. Nevertheless, most existing approaches are typically designed for classification tasks, ignoring underlying properties of dense prediction problems, such as medical image segmentation. First, these strategies often ignore the spatial relations between a given pixel and its neighbours. And second, the image context associated with each label is overlooked, which can convey important information about potential errors or ambiguities in the segmentation masks. To address these limitations, we propose in this work geodesic label smoothing (GeoLS), which integrates image information into the label smoothing process by leveraging the geodesic distance transform of the images. As the resulting label assignment is based on the computed geodesic map, class-wise relationships in the soft-labels are better modeled, as it considers image gradients at the boundary of two or more categories. Furthermore, spatial pixel-wise relationships are captured in the geodesic distance transform, integrating richer information than resorting to the Euclidean distance between pixels. We evaluate our method on two publicly available segmentation benchmarks and compare them to popular segmentation loss functions that directly modify the standard hard-label assignments. The proposed geodesic label smoothing improves the segmentation accuracy over existing soft-labeling strategies, demonstrating the validity of integrating image information into the label smoothing process. The code to reproduce our results is available at: https://github.com/anonymous35783578/GeoLS.')
}}
[% / %]

## Oral session 8 - Computer-assisted diagnosis - 1:30 - 2:30pm
[% .papers %]
{{ paper('Sparse Activations for Interpretable Disease Grading',
        'Kerol R. Djoumessi Donteu, Indu Ilanchezian, Laura Kühlewein, Hanna Faber, Christian F. Baumgartner, Bubacarr Bah, Philipp Berens, Lisa M. Koch',
        openreview='https://openreview.net/forum?id=us8BFTsWOq',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O006',
        paper='papers/O006',
        proceedings='',
        abstract="Interpreting deep learning models typically relies on post-hoc saliency map techniques. However, these techniques often fail to serve as actionable feedback to clinicians, and they do not directly explain the decision mechanism. Here, we propose an inherently interpretable model that combines the feature extraction capabilities of deep neural networks with advantages of sparse linear models in interpretability. Our approach relies on straightforward but effective changes to a deep bag-of-local-features model (BagNet). These modifications lead to fine-grained and sparse class evidence maps which, by design, correctly reflect the model\\'s decision mechanism. Our model is particularly suited for tasks which rely on characterising regions of interests that are very small and distributed over the image. In this paper, we focus on the detection of Diabetic Retinopathy, which is characterised by the progressive presence of small retinal lesions on fundus images. We observed good classification accuracy despite our added sparseness constraint. In addition, our model precisely highlighted retinal lesions relevant for the disease grading task and excluded irrelevant regions from the decision mechanism. The results suggest our sparse BagNet model can be a useful tool for clinicians as it allows efficient inspection of the model predictions and facilitates clinicians\\' and patients\\' trust.")
}}
{{ paper('Simple and Efficient Confidence Score for Grading Whole Slide Images',
        'Melanie Lubrano, Yaëlle Bellahsen Harrar, Rutger RH Fick, Cécile Badoual, Thomas Walter',
        openreview='https://openreview.net/forum?id=DA1hOTvcMWa',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O058',
        paper='papers/O058',
        proceedings='',
        abstract='Grading precancerous lesions on whole slide images is a challenging task: the continuous space of morphological phenotypes makes clear-cut decisions between different grades often difficult, leading to low inter- and intra-rater agreements. More and more Artificial Intelligence (AI) algorithms are developed to help pathologists perform and standardize their diagnosis. However, those models can render their prediction without consideration of the ambiguity of the classes and can fail without notice which prevent their wider acceptance in a clinical context.  In this paper, we propose a new score to measure the confidence of AI models in grading tasks. Our confidence score is specifically adapted to ordinal output variables, is versatile and does not require extra training or additional inferences nor particular architecture changes.  Comparison to other popular techniques such as Monte Carlo Dropout and deep ensembles shows that our method provides state-of-the art results, while being simpler, more versatile and less computationally intensive.  The score is also easily interpretable and consistent with real life hesitations of pathologists. We show that the score is capable of accurately identifying mispredicted slides and that accuracy for high confidence decisions is significantly higher than for low-confidence decisions (gap in AUC of 17.1\\% on the test set).  We believe that the proposed confidence score could be leveraged by pathologists directly in their workflow and assist them on difficult tasks such as grading precancerous lesions.')
}}
{{ paper('Frozen Language Model Helps ECG Zero-Shot Learning',
        'Jun Li, Che Liu, Sibo Cheng, Rossella Arcucci, Shenda Hong',
        openreview='https://openreview.net/forum?id=UAr59yTUWR2',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O191',
        paper='papers/O191',
        proceedings='',
        abstract='The electrocardiogram (ECG) is one of the most commonly used non-invasive, convenient medical monitoring tools that assist in the clinical diagnosis of heart diseases. Recently, deep learning (DL) techniques, particularly self-supervised learning (SSL), have demonstrated great potential in the classification of ECGs. SSL pre-training has achieved competitive performance with only a small amount of annotated data after fine-tuning. However, current SSL methods rely on the availability of annotated data and are unable to predict labels not existing in fine-tuning datasets. To address this challenge, we propose \\textbf{M}ultimodal \\textbf{E}CG-\\textbf{T}ext \\textbf{S}elf-supervised pre-training (METS), \\textbf{the first work} to utilize the auto-generated clinical reports to guide ECG SSL pre-training. We use a trainable ECG encoder and a frozen language model to embed paired ECGs and automatically machine-generated clinical reports separately, then the ECG embedding and paired report embedding are compared with other unpaired embeddings. In downstream classification tasks, METS achieves around 10\\% improvement in performance without using any annotated data via zero-shot classification, compared to other supervised and SSL baselines that rely on annotated data. Furthermore, METS achieves the highest recall and F1 scores on the MIT-BIH dataset, despite MIT-BIH containing different classes of ECGs compared to the pre-trained dataset. The extensive experiments have demonstrated the advantages of using ECG-Text multimodal self-supervised learning in terms of generalizability and effectiveness.')
}}
{{ paper('An end-to-end framework for diagnosing COVID-19 pneumonia via Parallel Recursive MLP module and Bi-LTSM correlation',
        'Yiwen Liu, Wenyu Xing, Mingbo Zhao, MINGQUAN LIN',
        openreview='https://openreview.net/forum?id=2cgTLIy1Zx',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O198',
        paper='papers/O198',
        proceedings='',
        abstract='To fully extract the feature information of lung parenchyma in Chest X-ray images and realize the auxiliary diagnosis of COVID-19 pneumonia, this paper proposed an end-to-end deep learning model, which is mainly composed of object detection, depth feature generation, and multi-channel fusion classification. Firstly, the convolutional neural network (CNN) and region proposal network (RPN)-based object detection module was adopted to detect chest cavity region of interest (ROI). Then, according to the obtained coordinate information of ROI and the convolution feature map of original image, the new convolution feature maps of ROI were obtained with number of 13. By screening 4 representative feature maps form 4 convolution layers with different receptive fields and combining with original ROI image, the 5-dimensional (5D) feature maps were generated as the multi-channel input of classification module. Moreover, in each channel of classification module, three pyramidal recursive MLPs were employed to achieve cross-scale and cross-channel feature analysis. Finally, the correlation analysis of multi-channel output was realized by bi-directional long short memory (Bi-LSTM) module, and the auxiliary diagnosis of pneumonia disease was realized through fully connected layer and SoftMax function. Experimental results show that the proposed model has better classification performance and diagnosis effect than previous methods, with great clinical application potential.')
}}
[% / %]

## Posters - 10:00am - 11:30am & 2:30pm - 3:30pm

[% .papers %]
{{ paper('An end-to-end framework for diagnosing COVID-19 pneumonia via Parallel Recursive MLP module and Bi-LTSM correlation',
        'Yiwen Liu, Wenyu Xing, Mingbo Zhao, MINGQUAN LIN',
        openreview='https://openreview.net/forum?id=2cgTLIy1Zx',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O198',
        paper='papers/O198',
        proceedings='',
        abstract='To fully extract the feature information of lung parenchyma in Chest X-ray images and realize the auxiliary diagnosis of COVID-19 pneumonia, this paper proposed an end-to-end deep learning model, which is mainly composed of object detection, depth feature generation, and multi-channel fusion classification. Firstly, the convolutional neural network (CNN) and region proposal network (RPN)-based object detection module was adopted to detect chest cavity region of interest (ROI). Then, according to the obtained coordinate information of ROI and the convolution feature map of original image, the new convolution feature maps of ROI were obtained with number of 13. By screening 4 representative feature maps form 4 convolution layers with different receptive fields and combining with original ROI image, the 5-dimensional (5D) feature maps were generated as the multi-channel input of classification module. Moreover, in each channel of classification module, three pyramidal recursive MLPs were employed to achieve cross-scale and cross-channel feature analysis. Finally, the correlation analysis of multi-channel output was realized by bi-directional long short memory (Bi-LSTM) module, and the auxiliary diagnosis of pneumonia disease was realized through fully connected layer and SoftMax function. Experimental results show that the proposed model has better classification performance and diagnosis effect than previous methods, with great clinical application potential.')
}}
{{ paper('Frozen Language Model Helps ECG Zero-Shot Learning',
        'Jun Li, Che Liu, Sibo Cheng, Rossella Arcucci, Shenda Hong',
        openreview='https://openreview.net/forum?id=UAr59yTUWR2',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O191',
        paper='papers/O191',
        proceedings='',
        abstract='The electrocardiogram (ECG) is one of the most commonly used non-invasive, convenient medical monitoring tools that assist in the clinical diagnosis of heart diseases. Recently, deep learning (DL) techniques, particularly self-supervised learning (SSL), have demonstrated great potential in the classification of ECGs. SSL pre-training has achieved competitive performance with only a small amount of annotated data after fine-tuning. However, current SSL methods rely on the availability of annotated data and are unable to predict labels not existing in fine-tuning datasets. To address this challenge, we propose \\textbf{M}ultimodal \\textbf{E}CG-\\textbf{T}ext \\textbf{S}elf-supervised pre-training (METS), \\textbf{the first work} to utilize the auto-generated clinical reports to guide ECG SSL pre-training. We use a trainable ECG encoder and a frozen language model to embed paired ECGs and automatically machine-generated clinical reports separately, then the ECG embedding and paired report embedding are compared with other unpaired embeddings. In downstream classification tasks, METS achieves around 10\\% improvement in performance without using any annotated data via zero-shot classification, compared to other supervised and SSL baselines that rely on annotated data. Furthermore, METS achieves the highest recall and F1 scores on the MIT-BIH dataset, despite MIT-BIH containing different classes of ECGs compared to the pre-trained dataset. The extensive experiments have demonstrated the advantages of using ECG-Text multimodal self-supervised learning in terms of generalizability and effectiveness.')
}}
{{ paper('GeoLS: Geodesic Label Smoothing for Image Segmentation',
        'Sukesh Adiga Vasudeva, Jose Dolz, Herve Lombaert',
        openreview='https://openreview.net/forum?id=mTIP1bkmR0q',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O236',
        paper='papers/O236',
        proceedings='',
        abstract='Smoothing hard-label assignments has emerged as a popular strategy in training discriminative models. Nevertheless, most existing approaches are typically designed for classification tasks, ignoring underlying properties of dense prediction problems, such as medical image segmentation. First, these strategies often ignore the spatial relations between a given pixel and its neighbours. And second, the image context associated with each label is overlooked, which can convey important information about potential errors or ambiguities in the segmentation masks. To address these limitations, we propose in this work geodesic label smoothing (GeoLS), which integrates image information into the label smoothing process by leveraging the geodesic distance transform of the images. As the resulting label assignment is based on the computed geodesic map, class-wise relationships in the soft-labels are better modeled, as it considers image gradients at the boundary of two or more categories. Furthermore, spatial pixel-wise relationships are captured in the geodesic distance transform, integrating richer information than resorting to the Euclidean distance between pixels. We evaluate our method on two publicly available segmentation benchmarks and compare them to popular segmentation loss functions that directly modify the standard hard-label assignments. The proposed geodesic label smoothing improves the segmentation accuracy over existing soft-labeling strategies, demonstrating the validity of integrating image information into the label smoothing process. The code to reproduce our results is available at: https://github.com/anonymous35783578/GeoLS.')
}}
{{ paper('Improving Segmentation of Objects with Varying Sizes in Biomedical Images using Instance-wise and Center-of-Instance Segmentation Loss Function',
        'Febrian Rachmadi, Charissa Poon, henrik skibbe',
        openreview='https://openreview.net/forum?id=8o83y0_YtE',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O130',
        paper='papers/O130',
        proceedings='',
        abstract='In this paper, we propose a novel two-component loss for biomedical image segmentation tasks called the Instance-wise and Center-of-Instance (ICI) loss, a loss function that addresses the instance imbalance problem commonly encountered when using pixel-wise loss functions such as the Dice loss. The Instance-wise component improves the detection of small instances or blobs\\" in image datasets with both large and small instances. The Center-of-Instance component improves the overall detection accuracy. We compared the ICI loss with two existing losses, the Dice loss and the blob loss, in the task of stroke lesion segmentation using the ATLAS R2.0 challenge dataset from MICCAI 2022. Compared to the other losses, the ICI loss provided a better balanced segmentation, and significantly outperformed the Dice loss with an improvement of $1.7-3.7\\%$ and the blob loss by $0.6-5.0\\%$ in terms of the Dice similarity coefficient on both validation and test set, suggesting that the ICI loss is a potential solution to the instance imbalance problem.')
}}
{{ paper('Inherent Consistent Learning for Accurate Semi-supervised Medical Image Segmentation',
        'Ye Zhu, Jie Yang, Siqi Liu, Ruimao Zhang',
        openreview='https://openreview.net/forum?id=diXhe9kUnQ',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O179',
        paper='papers/O179',
        proceedings='',
        abstract='Semi-supervised medical image segmentation has attracted much attention in recent years because of the high cost of medical image annotations. In this paper, we propose a novel Inherent Consistent Learning (ICL) method, aims to learn robust semantic category representations through the semantic consistency guidance of labeled and unlabeled data to help segmentation. In practice, we introduce two external modules, namely Supervised Semantic Proxy Adaptor (SSPA) and Unsupervised Semantic Consistent Learner (USCL) that is based on the attention mechanism to align the semantic category representations of labeled and unlabeled data, as well as update the global semantic representations over the entire training set. The proposed ICL is a plug-and-play scheme for various network architectures, and the two modules are not involved in the testing stage. Experimental results on three public benchmarks show that the proposed method can outperform the state-of-the-art, especially when the number of annotated data is extremely limited. Code is available at: https://github.com/zhuye98/ICL.git')
}}
{{ paper('MMCFormer: Missing Modality Compensation Transformer for Brain Tumor Segmentation',
        'Sanaz Karimijafarbigloo, Reza Azad, Amirhossein Kazerouni, Saeed Ebadollahi, Dorit Merhof',
        openreview='https://openreview.net/forum?id=PD0ASSmvlE',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O115',
        paper='papers/O115',
        proceedings='',
        abstract='Human brain tumours and more specifically gliomas are amongst the most life-threatening cancers which usually arise from abnormal growth of the glial stem cells. In practice, Magnetic Resonance Imaging (MRI) modalities, which offer different contrasts to elucidate tissue properties, provide comprehensive information regarding the brain’s structure and also potential clues for detecting tumors. Hence, multi-modal MRI is commonly utilized for the diagnosis of brain tumors. However, since the set of acquired modalities may vary between clinical sites, brain tumor studies may miss one or two MRI modalities. To address missing information in an end-to-end manner, we propose MMCFormer, a novel missing modality compensation network. Our strategy builds upon 3D efficient transformer blocks and uses a co-training strategy to effectively train a missing modality network. To ensure feature consistency in a multi-scale fashion, MMCFormer utilizes global contextual agreement modules in each scale of the encoders. Furthermore, to transfer modality-specific representations, we propose to incorporate auxiliary tokens in the bottleneck stage to model interaction between full and missing-modality paths. On top of that, we include feature consistency losses to reduce the domain gap in network prediction and increase the prediction reliability for the missing modality path. Extensive experiments on the BraTS 2018 dataset demonstrate the benefits of our approach compared to competing approaches. The implementation code will be publicly available after the paper acceptance.')
}}
{{ paper('Simple and Efficient Confidence Score for Grading Whole Slide Images',
        'Melanie Lubrano, Yaëlle Bellahsen Harrar, Rutger RH Fick, Cécile Badoual, Thomas Walter',
        openreview='https://openreview.net/forum?id=DA1hOTvcMWa',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O058',
        paper='papers/O058',
        proceedings='',
        abstract='Grading precancerous lesions on whole slide images is a challenging task: the continuous space of morphological phenotypes makes clear-cut decisions between different grades often difficult, leading to low inter- and intra-rater agreements. More and more Artificial Intelligence (AI) algorithms are developed to help pathologists perform and standardize their diagnosis. However, those models can render their prediction without consideration of the ambiguity of the classes and can fail without notice which prevent their wider acceptance in a clinical context.  In this paper, we propose a new score to measure the confidence of AI models in grading tasks. Our confidence score is specifically adapted to ordinal output variables, is versatile and does not require extra training or additional inferences nor particular architecture changes.  Comparison to other popular techniques such as Monte Carlo Dropout and deep ensembles shows that our method provides state-of-the art results, while being simpler, more versatile and less computationally intensive.  The score is also easily interpretable and consistent with real life hesitations of pathologists. We show that the score is capable of accurately identifying mispredicted slides and that accuracy for high confidence decisions is significantly higher than for low-confidence decisions (gap in AUC of 17.1\\% on the test set).  We believe that the proposed confidence score could be leveraged by pathologists directly in their workflow and assist them on difficult tasks such as grading precancerous lesions.')
}}
{{ paper('Sparse Activations for Interpretable Disease Grading',
        'Kerol R. Djoumessi Donteu, Indu Ilanchezian, Laura Kühlewein, Hanna Faber, Christian F. Baumgartner, Bubacarr Bah, Philipp Berens, Lisa M. Koch',
        openreview='https://openreview.net/forum?id=us8BFTsWOq',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='O006',
        paper='papers/O006',
        proceedings='',
        abstract="Interpreting deep learning models typically relies on post-hoc saliency map techniques. However, these techniques often fail to serve as actionable feedback to clinicians, and they do not directly explain the decision mechanism. Here, we propose an inherently interpretable model that combines the feature extraction capabilities of deep neural networks with advantages of sparse linear models in interpretability. Our approach relies on straightforward but effective changes to a deep bag-of-local-features model (BagNet). These modifications lead to fine-grained and sparse class evidence maps which, by design, correctly reflect the model\\'s decision mechanism. Our model is particularly suited for tasks which rely on characterising regions of interests that are very small and distributed over the image. In this paper, we focus on the detection of Diabetic Retinopathy, which is characterised by the progressive presence of small retinal lesions on fundus images. We observed good classification accuracy despite our added sparseness constraint. In addition, our model precisely highlighted retinal lesions relevant for the disease grading task and excluded irrelevant regions from the decision mechanism. The results suggest our sparse BagNet model can be a useful tool for clinicians as it allows efficient inspection of the model predictions and facilitates clinicians\\' and patients\\' trust.")
}}
{{ paper('Diffusion Models for Contrast Harmonization of Magnetic Resonance Images',
        'Alicia Durrer, Julia Wolleb, Florentin Bieder, Tim Sinnecker, Matthias Weigel, Robin Sandkuehler, Cristina Granziera, Özgür Yaldizli, Philippe C. Cattin',
        openreview='https://openreview.net/forum?id=Xs_Hd23_PP',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P008',
        paper='papers/P008',
        proceedings='',
        abstract='Magnetic resonance (MR) images from multiple sources often show differences in image contrast related to acquisition settings or the used scanner type. For long-term studies, longitudinal comparability is essential but can be impaired by these contrast differences, leading to biased results when using automated evaluation tools. This study presents a diffusion model-based approach for contrast harmonization. We use a data set consisting of scans of 18 Multiple Sclerosis patients and 22 healthy controls. Each subject was scanned in two MR scanners of different magnetic field strengths (1.5 T and 3 T), resulting in a paired data set that shows scanner-inherent differences. We map images from the source contrast to the target contrast for both directions, from 3 T to 1.5 T and from 1.5 T to 3 T. As we only want to change the contrast, not the anatomical information, our method uses the original image to guide the image-to-image translation process by adding structural information. The aim is that the mapped scans display increased comparability with scans of the target contrast for downstream tasks. We evaluate this method for the task of segmentation of cerebrospinal fluid, grey matter and white matter. Our method achieves good and consistent results for both directions of the mapping.')
}}
{{ paper('On-the-Fly Test-time Adaptation for Medical Image Segmentation',
        'Jeya Maria Jose Valanarasu, Pengfei Guo, Vibashan VS, Vishal M. Patel',
        openreview='https://openreview.net/forum?id=UQDalTzrEg',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P011',
        paper='papers/P011',
        proceedings='',
        abstract='One major problem in deep learning-based solutions for medical imaging is the drop in performance when a model is tested on a data distribution different from the one that it is trained on.  Adapting the source model to target data distribution at test-time is an efficient solution for the data-shift problem. Previous methods solve this by adapting the model to target distribution by using techniques like entropy minimization or regularization. In these methods, the models are still updated by back-propagation using an unsupervised loss on complete test data distribution. In real-world clinical settings, it makes more sense to adapt a model to a new test image on-the-fly and avoid model update during inference due to privacy concerns and lack of computing resource at deployment. To this end, we propose a new setting - On-the-Fly Adaptation which is zero-shot and episodic i.e., the model is adapted to a single image at a time and also does not perform any back-propagation during test-time). To achieve this, we propose a new framework called Adaptive UNet where each convolutional block is equipped with an adaptive batch normalization layer to adapt the features with respect to a domain code. The domain code is generated using a pre-trained encoder trained on a large corpus of medical images. During test-time, the model takes in just the new test image and generates a domain code to adapt the features of source model according to the test data. We validate the performance on both 2D and 3D data distribution shifts where we get a better performance compared to previous test-time adaptation methods.')
}}
{{ paper('A Robust Mean Teacher Framework for Semi-Supervised Cell Detection in Histopathology Images',
        'Ziqi Wen, Chuyang Ye',
        openreview='https://openreview.net/forum?id=PEWigppmw3b',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P015',
        paper='papers/P015',
        proceedings='',
        abstract='Cell detection in histopathology images facilitates clinical diagnosis, and deep learning methods have been applied to the detection problem with substantially improved performance. However, cell detection methods based on deep learning usually require a large number of annotated training samples, which are costly and time-consuming to obtain, and it is desirable to develop methods where detection networks can be adequately trained with only a few annotated training samples. Since unlabeled data is much less expensive to obtain, it is possible to address this problem with semi-supervised learning, where abundant unlabeled data is combined with the limited annotated training samples for network training. In this work, we propose a semi-supervised object detection method for cell detection in histopathology images, which is based on and improves the mean teacher framework. In standard mean teacher, the detection results on unlabeled data given by the teacher model can be noisy, which may negatively impact the learning of the student model. To address this problem, we propose to suppress the noise in the detection results of the teacher model by mixing the unlabeled training images with labeled training images of which the ground truth detection results are available. In addition, we propose to further incorporate a loss term that is robust to noise when the the student model learns from the teacher model. To evaluate the proposed method, experiments were performed on a publicly available dataset for multi-class cell detection, and the experimental results show that our method improves the performance of cell detection in histopathology images in the semi-supervised setting.')
}}
{{ paper('Rotation-Scale Equivariant Steerable Filters',
        'Yilong Yang, Srinandan Dasmahapatra, Sasan Mahmoodi',
        openreview='https://openreview.net/forum?id=A0MyiAwE_E4',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P032',
        paper='papers/P032',
        proceedings='',
        abstract='Incorporating either rotation equivariance or scale equivariance into CNNs has proved to be effective in improving models’ generalization performance. However, jointly integrating rotation and scale equivariance into CNNs has not been widely explored. Digital histology imaging of biopsy tissue can be captured at arbitrary orientation and magnification and stored at different resolutions, resulting in cells appearing in different scales. When conventional CNNs are applied to histopathology image analysis, the generalization performance of models is limited because 1) a part of the parameters of filters are trained to fit rotation transformation, thus decreasing the capability of learning other discriminative features; 2) fixed-size filters trained on images at a given scale fail to generalize to those at different scales. To deal with these issues, we propose the Rotation-Scale Equivariant Steerable Filter (RSESF), which incorporates steerable filters and scale-space theory. The RSESF contains copies of filters that are linear combinations of Gaussian filters, whose direction is controlled by directional derivatives and whose scale parameters are trainable but constrained to span disjoint scales in successive layers of the network. Extensive experiments on two gland segmentation datasets demonstrate that our method outperforms other approaches, with much fewer trainable parameters and fewer GPU resources required. The source code is available at: https://github.com/ynulonger/RSESF.')
}}
{{ paper('MTSR-MRI: Combined Modality Translation and Super-Resolution of Magnetic Resonance Images',
        'Avirup Dey, Mehran Ebrahimi',
        openreview='https://openreview.net/forum?id=mUPIsk20oGt',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P038',
        paper='papers/P038',
        proceedings='',
        abstract='Magnetic resonance imaging (MRI) is a common non-invasive imaging technique with high soft tissue contrast. Different MRI modalities are used for the diagnosis of various conditions including T1-weighted and T2-weighted MRI. In this paper, we introduce MTSR-MRI, a novel method that can not only upscale low-resolution scans but also translates between the T1-weighted  and T2-weighted modalities. This will potentially reduce the scan time or repeat scans by taking low-resolution inputs in one modality and returning plausible high-resolution output in another modality. Due to the ambiguity that persists in image-to-image translation tasks, we consider the distribution of possible outputs in a conditional generative setting. The mapping is distilled in a low-dimensional latent distribution which can be randomly sampled at test time, thus allowing us to generate multiple plausible high-resolution outputs from a given low-resolution input. We validate the proposed method on the BraTS-18 dataset qualitatively and quantitatively using a variety of similarity measures. The implementation of this work will be available at https://github.com/AvirupJU/MTSR-MRI . ')
}}
{{ paper('Reverse Engineering Breast MRIs: Predicting Acquisition Parameters Directly from Images',
        'Nicholas Konz, Maciej A Mazurowski',
        openreview='https://openreview.net/forum?id=JZBNeVLAqp',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P054',
        paper='papers/P054',
        proceedings='',
        abstract="The image acquisition parameters (IAPs) used to create MRI scans are central to defining the appearance of the images. Deep learning models trained on data acquired using certain parameters might not generalize well to images acquired with different parameters. Being able to recover such parameters directly from an image could help determine whether a deep learning model is applicable, and could assist with data harmonization and/or domain adaptation. Here, we introduce a neural network model that can predict many complex IAPs used to generate an MR image with high accuracy solely using the image, with a single forward pass. These predicted parameters include field strength, echo and repetition times, acquisition matrix, scanner model, scan options, and others. Even challenging parameters such as contrast agent type can be predicted with good accuracy. We perform a variety of experiments and analyses of our model\\'s ability to predict IAPs on many MRI scans of new patients, and demonstrate its usage in a realistic application. Predicting IAPs from the images is an important step toward better understanding the relationship between image appearance and IAPs. This in turn will advance the understanding of many concepts related to the generalizability of neural network models on medical images, including domain shift, domain adaptation, and data harmonization. ")
}}
{{ paper('Whole-slide-imaging Cancer Metastases Detection and Localization with Limited Tumorous Data',
        'Yinsheng He, Xingyu Li',
        openreview='https://openreview.net/forum?id=BF4NpwMuei',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P067',
        paper='papers/P067',
        proceedings='',
        abstract='Recently, various deep learning methods have shown significant successes in medical image analysis, especially in the detection of cancer metastases in hematoxylin and eosin (H&E) stained whole-slide images (WSIs). However, in order to obtain good performance, these research achievements rely on hundreds of well-annotated WSIs. In this study, we tackle the tumor localization and detection problem under the setting of few labeled whole slide images and introduce a patch-based analysis pipeline based on the latest reverse knowledge distillation architecture. To address the extremely unbalanced normal and tumorous samples in training sample collection, we applied the focal loss formula to the representation similarity metric for model optimization. Compared with prior arts, our method achieves similar performance by less than ten percent of training samples on the public Camelyon16 dataset. In addition, this is the first work that show the great potential of the knowledge distillation models in computational histopathology. Our python implementation will be publically accessible upon paper acceptance.')
}}
{{ paper('Metadata-guided Consistency Learning for High Content Images',
        'Johan Fredin Haslum, Christos Matsoukas, Karl-Johan Leuchowius, Erik Müllers, Kevin Smith',
        openreview='https://openreview.net/forum?id=PzzhiSNnyF8',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P071',
        paper='papers/P071',
        proceedings='',
        abstract='High content imaging assays can capture rich phenotypic response data for large sets of compound treatments, aiding in the characterization and discovery of novel drugs. However, extracting representative features from high content images that can capture subtle nuances in phenotypes remains challenging. The lack of high-quality labels makes it difficult to achieve satisfactory results with supervised deep learning. Self-Supervised learning methods have shown great success on natural images, and offer an attractive alternative also to microscopy images. However, we find that self-supervised learning techniques underperform on high content imaging assays. One challenge is the undesirable domain shifts present in the data known as batch effects, which may be caused by biological noise or uncontrolled experimental conditions. To this end, we introduce Cross-Domain Consistency Learning (CDCL), a novel approach that is able to learn in the presence of batch effects. CDCL enforces the learning of biological similarities while disregarding undesirable batch-specific signals, which leads to more useful and versatile representations. These features are organised according to their morphological changes and are more useful for downstream tasks - such as distinguishing treatments and mechanism of action.')
}}
{{ paper('Multimodal Image-Text Matching Improves Retrieval-based Chest X-Ray Report Generation',
        'Jaehwan Jeong, Katherine Tian, Andrew Li, Sina Hartung, Subathra Adithan, Fardad Behzadi, Juan Calle, David Osayande, Michael Pohlen, Pranav Rajpurkar',
        openreview='https://openreview.net/forum?id=aZ0OuYMSMMZ',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P076',
        paper='papers/P076',
        proceedings='',
        abstract='Automated generation of clinically accurate radiology reports can improve patient care. Previous report generation methods that rely on image captioning models often generate incoherent and incorrect text due to their lack of relevant domain knowledge, while retrieval-based attempts frequently retrieve reports that are irrelevant to the input image. In this work, we propose Contrastive X-Ray REport Match (X-REM), a novel retrieval-based radiology report generation module that uses an image-text matching score to measure the similarity of a chest X-ray image and radiology report for report retrieval. We observe that computing the image-text matching score with a language-image model can effectively capture the fine-grained interaction between image and text that is often lost when using cosine similarity. X-REM outperforms multiple prior radiology report generation modules in terms of both natural language and clinical metrics. Human evaluation of the generated reports suggests that X-REM increased the number of zero-error reports and decreased the average error severity compared to the baseline retrieval approach. Our code is available at: https://github.com/rajpurkarlab/X-REM')
}}
{{ paper('Patched Diffusion Models for Unsupervised Anomaly Detection in Brain MRI',
        'Finn Behrendt, Debayan Bhattacharya, Julia Krüger, Roland Opfer, Alexander Schlaefer',
        openreview='https://openreview.net/forum?id=O-uZr5S1tJE',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P083',
        paper='papers/P083',
        proceedings='',
        abstract='The use of supervised deep learning techniques to detect pathologies in brain MRI scans can be challenging due to the diversity of brain anatomy and the need for annotated data sets. An alternative approach is to use unsupervised anomaly detection, which only requires sample-level labels of healthy brains to create a reference representation. This reference representation can then be compared to unhealthy brain anatomy in a pixel-wise manner to identify abnormalities. To accomplish this, generative models are needed to create anatomically consistent MRI scans of healthy brains. While recent diffusion models have shown promise in this task, accurately generating the complex structure of the human brain remains a challenge. In this paper, we propose a method that reformulates the generation task of diffusion models as a patch-based estimation of healthy brain anatomy, using spatial context to guide and improve reconstruction. We evaluate our approach on data of tumors and multiple sclerosis lesions and demonstrate a relative improvement of 25.1% compared to existing baselines.')
}}
{{ paper('Spatial Correspondence between Graph Neural Network-Segmented Images',
        'Qian Li, Yunguan Fu, Qianye Yang, Zhijiang Du, Hongjian Yu, Yipeng Hu',
        openreview='https://openreview.net/forum?id=d7J0IiMqcZd',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P090',
        paper='papers/P090',
        proceedings='',
        abstract='Graph neural networks (GNNs) have been proposed for medical image segmentation, by predicting anatomical structures represented by graphs of vertices and edges. One such type of graphs are predefined with fixed size and connectivity to represent a reference of anatomical regions of interest, thus known as templates. This work explores the potentials in these GNNs with common topology for establishing spatial correspondence, implicitly maintained during segmenting two or more images. With an example application of registering local vertebral sub-regions found in CT images, our experimental results showed that the GNN-based segmentation is capable of accurate and reliable localisation of the same interventionally interesting structures between images, not limited to the segmentation classes. The reported average target registration errors of 2.2$\\pm$1.3 mm and 2.7$\\pm$1.4 mm, for aligning holdout test images with a reference and for aligning two test images, respectively, were by a considerable margin lower than those from the tested non-learning and learning-based registration algorithms. Further ablation studies assess the contributions towards the registration performance, from individual components in the originally segmentation-purposed network and its training algorithm. The results highlight that the proposed segmentation-in-lieu-of-registration approach shares methodological similarity with existing registration methods, such as the use of displacement smoothness constraint and point distance minimisation albeit on non-grid graphs, which interestingly yielded benefits for both segmentation and registration. We therefore conclude that the template-based GNN segmentation can effectively establish spatial correspondence in our application, without any other dedicated registration algorithms.')
}}
{{ paper('Convolutional-recurrent neural networks approximate diffusion tractography from T1-weighted MRI and associated anatomical context',
        'Leon Yichen Cai, Ho Hin Lee, Nancy Rose Newlin, Cailey Irene Kerley, Praitayini Kanakaraj, Qi Yang, Graham Walter Johnson, Daniel Moyer, Kurt Gregory Schilling, Francois Rheault, Bennett A. Landman',
        openreview='https://openreview.net/forum?id=TelM2TBYgoA',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P110',
        paper='papers/P110',
        proceedings='',
        abstract='Diffusion MRI (dMRI) streamline tractography is the gold-standard for in vivo estimation of white matter (WM) pathways in the brain. However, the high angular resolution dMRI acquisitions capable of fitting the microstructural models needed for tractography are often time-consuming and not routinely collected clinically, restricting the scope of tractography analyses. To address this limitation, we build on recent advances in deep learning which have demonstrated that streamline propagation can be learned from dMRI directly without traditional model fitting. Specifically, we propose learning the streamline propagator from T1w MRI to facilitate arbitrary tractography analyses when dMRI is unavailable. To do so, we present a novel convolutional-recurrent neural network (CoRNN) trained in a teacher-student framework that leverages T1w MRI, associated anatomical context, and streamline memory from data acquired for the Human Connectome Project. We characterize our approach under two common tractography paradigms, WM bundle analysis and structural connectomics, and find approximately a 5-15% difference between measures computed from streamlines generated with our approach and those generated using traditional dMRI tractography. When placed in the literature, these results suggest that the accuracy of WM measures computed from T1w MRI with our method is on the level of scan-rescan dMRI variability and raise an important question: is tractography truly a microstructural phenomenon, or has dMRI merely facilitated its discovery and implementation?')
}}
{{ paper('Addressing Chest Radiograph Projection Bias in Deep Classification Models',
        'Sofia Cardoso Pereira, Joana Rocha, Alex Gaudio, Asim Smailagic, Aurélio Campilho, Ana Maria Mendonça',
        openreview='https://openreview.net/forum?id=k8K2zEiv_m',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P121',
        paper='papers/P121',
        proceedings='',
        abstract='Deep learning-based models are widely used for disease classification in chest radiographs. This exam can be performed in one of two projections (posteroanterior or anteroposterior), depending on the direction that the X-ray beam travels through the body. Since projection visibly affects the way anatomical structures appear in the scans, it may introduce bias in classifiers, especially when spurious correlations between a given disease and a projection occur. This paper examines the influence of chest radiograph projection on the performance of deep learning-based classification models and proposes an approach to mitigate projection-induced bias. Results show that a DenseNet-121 model is better at classifying images from the most representative projection in the data set, suggesting that projection is taken into account by the classifier. Moreover, this model can classify chest X-ray projection better than any of the fourteen radiological findings considered, without being explicitly trained for that task, putting it at high risk for projection bias. We propose a label-conditional gradient reversal framework to make the model insensitive to projection, by forcing the extracted features to be simultaneously good for disease classification and bad for projection classification, resulting in a framework with reduced projection-induced bias.')
}}
{{ paper('Semi-supervised Learning with Contrastive and Topology Losses for Catheter Segmentation and Misplacement Prediction',
        'Tianyu Hwang, Chih-Hung Wang, Holger R Roth, Dong Yang, Can Zhao, Chien-Hua Huang, Weichung Wang',
        openreview='https://openreview.net/forum?id=9mPSPWo5tzu',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P129',
        paper='papers/P129',
        proceedings='',
        abstract="Chest X-ray images are often used to determine the proper placement of catheters, as incorrect placement can lead to severe complications. With the advent of deep learning, computer-aided detection methods have been developed to assist radiologists in identifying catheter misplacement by detecting and highlighting the catheter\\'s path. However, obtaining large, pixel-wise labeled datasets can be challenging due to the labor-intensive nature of annotation. To address this issue, we proposed a novel semi-supervised learning method that combines contrastive loss and topology loss. This method takes advantage of the known topological properties of catheters and does not require extensive labeling. We collected 7,378 chest X-ray images from the *****, which were labeled for misplacement of nasogastric and endotracheal tube catheters, and included pixel-wise annotation. Moreover, the CLiP dataset was used as an unlabeled dataset for semi-supervised learning. We used a hybrid U-Net architecture with an added classification head to perform simultaneous segmentation of the catheter and misplacement classification. Our model achieved an average AUC of 0.977 for classification and a average Dice score of 0.598 for segmentation.")
}}
{{ paper('Generative Adversarial Networks for Coronary CT Angiography Acquisition Protocol Correction with Explicit Attenuation Constraints',
        'Rudolf Leonardus Mirjam Van Herten, Louis van Harten, Nils Planken, Ivana Isgum',
        openreview='https://openreview.net/forum?id=MIHF_buWGUQ',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P136',
        paper='papers/P136',
        proceedings='',
        abstract='The image quality of coronary CT angiography (CCTA) is important for the correct diagnosis of patients with suspected coronary artery disease, which is heavily influenced by image acquisition. Timing of the contrast media injection specifically influences the level of arterial enhancement, and it is aimed to allow optimal assessment of the coronary artery morphology. However, a consensus on an optimal acquisition protocol that can account for the large variety in patient cohorts has not been reached, commonly resulting in suboptimal arterial enhancement. In this work, we propose a generative adversarial network for the retrospective correction of contrast media attenuation in CCTA, thus reducing the dependency on an optimal timing protocol at acquisition. We develop and evaluate the method in a set of 1,179 CCTA scans with varying levels of contrast enhancement. We evaluate the consistency of intensity values in the coronary arteries and evaluate performance of coronary centerline extraction as a commonly performed analysis task. Results show that correction of contrast media attenuation values in CCTA scans is feasible, and that it improves the performance of automatic centerline extraction. The method may allow improved analysis of coronary arteries  in CCTA scans with suboptimal contrast enhancement.')
}}
{{ paper('TransNetR: Transformer-based Residual Network for Polyp Segmentation with Multi-Center Out-of-Distribution Testing',
        'Debesh Jha, Nikhil Kumar Tomar, Vanshali Sharma, Ulas Bagci',
        openreview='https://openreview.net/forum?id=-8mexJCWH_-',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P143',
        paper='papers/P143',
        proceedings='',
        abstract='Colonoscopy is considered the most effective screening test to detect colorectal cancer (CRC) and its precursor lesions, i.e., polyps. However, the procedure experiences high miss rates due to polyp heterogeneity and inter-observer dependency. Hence, several deep learning powered systems have been proposed considering the criticality of polyp detection and segmentation in clinical practices. Despite achieving improved outcomes, the existing automated approaches are inefficient in attaining real-time processing speed. Moreover, they suffer from a significant performance drop when evaluated on inter-patient data, especially those collected from different centers. Therefore, we intend to develop a novel real-time deep learning based architecture, Transformer based Residual network (TransNetR), for colon polyp segmentation and evaluate its diagnostic performance. The proposed architecture, TransNetR, is an encoder-decoder network that consists of a pre-trained ResNet50 as the encoder, three decoder blocks, and an upsampling layer at the end of the network. TransNetR obtains a high dice coefficient of 0.8706 and a mean Intersection over union of 0.8016 and retains a real-time processing speed of 54.60 on the Kvasir-SEG dataset. Apart from this,  the major contribution of the work lies in exploring the generalizability of the TransNetR by testing the proposed algorithm on the out-of-distribution (test distribution is unknown and different from training distribution) dataset. As a use case, we tested our proposed algorithm on the PolypGen (6 unique centers) dataset and two other popular polyp segmentation benchmarking datasets. We obtained state-of-the-art performance on all three datasets during out-of-distribution testing. The source code of TransNetR is available at https://github.com/Anonymous/TransNetR. ')
}}
{{ paper('SFT-KD-Recon: Learning a Student-friendly Teacher for Knowledge Distillation in Magnetic Resonance Image Reconstruction',
        'NagaGayathri Matcha, Sriprabha Ramanarayanan, Mohammad Al Fahim, Rahul G S, Keerthi Ram, Mohanasankar Sivaprakasam',
        openreview='https://openreview.net/forum?id=j6GZ2IEia_E',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P147',
        paper='papers/P147',
        proceedings='',
        abstract="Deep cascaded architectures for magnetic resonance imaging (MRI) acceleration have shown remarkable success in providing high-quality reconstruction. However, as the number of cascades increases, the improvements in reconstruction tend to become marginal, indicating possible excess model capacity. Knowledge distillation (KD) is an emerging technique to compress these models, in which a trained deep teacher\\' network is used to distill knowledge to a smaller student\\' network, such that the student  learns to mimic the behavior of the teacher. Most KD methods focus on effectively training the student with a pre-trained teacher that is unaware of the student model. We propose SFT-KD-Recon, a student-friendly teacher training approach along with the student as a prior step to KD to make the teacher aware of the student\\'s structure and capacity and enable aligning the teacher\\'s representations with the student.  In SFT, the teacher is jointly trained with the unfolded branch configurations of the student blocks using three loss terms - teacher-reconstruction loss, student-reconstruction loss, and teacher-student imitation loss, followed by KD of the student. We perform extensive experiments for MRI acceleration in 4x and 5x under-sampling, on the brain and cardiac datasets on five KD methods using the proposed approach as a prior step. We consider the DC-CNN architecture and setup teacher as D5C5 (141765 parameters), and student as D3C5 (49285 parameters) denoting 2.87:1 compression.  Results show that (i) our approach consistently improves the KD methods with improved reconstruction performance and image quality, and (ii) the student distilled using our approach is competitive with the teacher, with the performance gap reduced from 0.53 dB to 0.03 dB.")
}}
{{ paper('FlexR: Few-shot Classification with Language Embeddings for Structured Reporting of Chest X-rays',
        'Matthias Keicher, Kamilia Zaripova, Tobias Czempiel, Kristina Mach, Ashkan Khakzar, Nassir Navab',
        openreview='https://openreview.net/forum?id=wiN5LQThnIV',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P162',
        paper='papers/P162',
        proceedings='',
        abstract='The automation of chest X-ray reporting has garnered significant interest due to the time-consuming nature of the task. However, the clinical accuracy of free-text reports has proven challenging to quantify using natural language processing metrics, given the complexity of medical information, the variety of writing styles, and the potential for typos and inconsistencies. Structured reporting and standardized reports, on the other hand, can provide consistency and formalize the evaluation of clinical correctness. However, high-quality annotations for structured reporting are scarce. Therefore, we propose a method to predict clinical findings defined by sentences in structured reporting templates, which can be used to fill such templates. The approach involves training a contrastive language-image model using chest X-rays and related free-text radiological reports, then creating textual prompts for each structured finding and optimizing a classifier to predict clinical findings in the medical image. Results show that even with limited image-level annotations for training, the method can accomplish the structured reporting tasks of severity assessment of cardiomegaly and localizing pathologies in chest X-rays.')
}}
{{ paper('Evaluating Adversarial Robustness of Low dose CT Recovery',
        'Kanchana Vaishnavi Gandikota, Paramanand Chandramouli, Hannah Dröge, Michael Moeller',
        openreview='https://openreview.net/forum?id=L-N1uAxfQk1',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P166',
        paper='papers/P166',
        proceedings='',
        abstract='Low dose computer tomography (CT) acquisition using reduced radiation or sparse angle measurements is recommended to decrease the harmful effects of X-ray radiation. Recent works successfully apply deep networks to the problem of low dose CT recovery on benchmark datasets. However, their robustness needs a thorough evaluation before use in clinical settings. In this work, we evaluate the robustness of different deep learning  approaches and classical methods for CT recovery.We show that deep networks, including model based networks encouraging data consistency are more susceptible to untargeted attacks. Surprisingly, we observe that data consistency is not heavily affected  even for these poor quality reconstructions, motivating the need for better regularization for the networks. We demonstrate the feasibility of  universal attacks and study attack transferability across different methods.  We analyze robustness to attacks causing localized changes in clinically relevant regions. Both classical approaches and deep networks are affected by such attacks leading to change in  visual appearance of localized lesions, for extremely small perturbations. As the resulting reconstructions have high data consistency with original measurements, these localized attacks can be used to explore the solution space of CT recovery problem. ')
}}
{{ paper('MedSegDiff: Medical Image Segmentation with Diffusion Probabilistic Model',
        'Junde Wu, RAO FU, Huihui Fang, Yu Zhang, Yehui Yang, Haoyi Xiong, Huiying Liu, Yanwu Xu',
        openreview='https://openreview.net/forum?id=Jdw-cm2jG9',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P185',
        paper='papers/P185',
        proceedings='',
        abstract='Diffusion Probabilistic Model (DPM) has recently become one of the hottest topics in computer vision. Its image generation applications, such as Imagen, Latent Diffusion Models, and Stable Diffusion, have demonstrated impressive generation capabilities, which have sparked extensive discussions in the community. Furthermore, many recent studies have found DPM to be useful in a variety of other vision tasks, including image deblurring, super-resolution, and anomaly detection. Inspired by the success of DPM, we propose MedSegDiff, the first DPM-based model for general medical image segmentation tasks. To enhance the step-wise regional attention in DPM for medical image segmentation, we propose Dynamic Conditional Encoding, which establishes state-adaptive conditions for each sampling step. Additionally, we propose the Feature Frequency Parser (FF-Parser) to eliminate the negative effect of high-frequency noise components in this process. We verify the effectiveness of MedSegDiff on three medical segmentation tasks with different image modalities, including optic cup segmentation over fundus images, brain tumor segmentation over MRI images, and thyroid nodule segmentation over ultrasound images. Our experimental results show that MedSegDiff outperforms state-of-the-art (SOTA) methods by a considerable performance gap, demonstrating the generalization and effectiveness of the proposed model.')
}}
{{ paper('FUSQA: Fetal Ultrasound Segmentation Quality Assessment',
        'Sevim Cengiz, Ibrahim Almakky, Mohammad Yaqub',
        openreview='https://openreview.net/forum?id=Umyz5JHIXpD',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P199',
        paper='papers/P199',
        proceedings='',
        abstract='Deep learning models have been effective for various fetal ultrasound segmentation tasks. However, generalization to new unseen data has raised questions about their effectiveness for clinical adoption. Normally, a transition to new unseen data requires time-consuming and costly quality assurance processes to validate the segmentation performance post-transition. Segmentation quality assessment efforts have focused on natural images, where the problem has been typically formulated as a dice score regression task. In this paper, we propose a simplified Fetal Ultrasound Segmentation Quality Assessment (FUSQA) model to tackle the segmentation performance deterioration challenge. We formulate the segmentation quality assessment process as an automated classification task to distinguish between good and poor quality segmentation masks for more accurate gestational age estimation. We validate the performance of our proposed approach on two datasets we collect from two hospitals using different ultrasound machines. We compare different architectures, with our best-performing architecture achieving over 90% classification accuracy on distinguishing between good and poor quality segmentation masks from an unseen dataset. Additionally, there was only a 1.45-days difference between the gestational age reported by doctors and estimated based on CRL measurements using well-segmented masks. On the other hand, this difference increased and reached up to 7.73 days when we calculated CRL from the poorly segmented masks. As a result, AI-based approaches can potentially aid fetal ultrasound segmentation quality assessment and might detect poor segmentation in real-time screening in the future.')
}}
{{ paper('Zero-Shot Self-Supervised Joint Temporal Image and Sensitivity Map Reconstruction via Linear Latent Space',
        'Molin Zhang, Junshen Xu, Yamin Arefeen, Elfar Adalsteinsson',
        openreview='https://openreview.net/forum?id=gaMVPWvzF1d',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P204',
        paper='papers/P204',
        proceedings='',
        abstract='Fast spin-echo (FSE) pulse sequences for Magnetic Resonance Imaging (MRI) offer important imaging contrast in clinically feasible scan times. T2-shuffling is widely used to resolve temporal signal dynamics in FSE acquisitions by exploiting temporal correlations via linear latent space and a predefined regularizer. However, predefined regularizers fail to exploit the incoherence especially for 2D acquisitions.Recent self-supervised learning methods achieve high-fidelity reconstructions by learning a regularizer from undersampled data without a standard supervised training data set. In this work, we propose a novel approach that utilizes a self supervised learning framework to learn a regularizer constrained on a linear latent space which improves time-resolved FSE images reconstruction quality. Additionally, in regimes without groundtruth sensitivity maps, we propose joint estimation of coil-sensitivity maps using an iterative reconstruction technique. Our technique functions is in a zero-shot fashion, as it only utilizes data from a single scan of highly undersampled time series images. We perform experiments on simulated and retrospective in-vivo data to evaluate the performance of the proposed zero-shot learning method for temporal FSE reconstruction. The results demonstrate the success of our proposed method where NMSE and SSIM are significantly increased and the artifacts are reduced.')
}}
{{ paper('Domain adaptation using optimal transport for invariant learning using histopathology datasets',
        'Kianoush Falahkheirkhah, Alex Xijie Lu, David Alvarez-Melis, Grace Huynh',
        openreview='https://openreview.net/forum?id=nmZRTaZZv5Z',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P215',
        paper='papers/P215',
        proceedings='',
        abstract='Histopathology is critical for the diagnosis of many diseases, including cancer. These protocols typically require pathologists to manually evaluate slides under a microscope, which is time-consuming and subjective, leading to interest in machine learning to automate analysis. However, computational techniques are limited by batch effects, where technical factors like differences in preparation protocol or scanners can alter the appearance of slides, causing models trained on one institution or patient to fail when generalizing to others. Here, we propose a domain adaptation method that improves the generalization of histopathological models to data from unseen institutions, without the need for labels or retraining in these new settings. Our approach introduces an optimal transport (OT) loss, that extends adversarial methods that penalize models if images from different institutions can be distinguished in their representation space. Unlike previous methods, which operate on single samples, our loss accounts for distributional differences between batches of images. We show that on the Camelyon17 dataset, while both methods can adapt to global differences in color distribution, only our OT loss can reliably classify a cancer phenotype unseen during training. Together, our results suggest that OT improves generalization on rare but critical phenotypes that may only make up a small fraction of the total tiles and variation in a slide.  ')
}}
{{ paper('A comparison of self-supervised pretraining approaches for predicting disease risk from chest radiograph images',
        'Yanru Chen, Michael T Lu, Vineet K Raghu',
        openreview='https://openreview.net/forum?id=HzpdwXFc_Q',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P222',
        paper='papers/P222',
        proceedings='',
        abstract='Deep learning is the state-of-the-art for medical imaging tasks, but requires large, labeled datasets. For risk prediction, large datasets are rare since they require both imaging and follow-up (e.g., diagnosis codes). However, the release of publicly available imaging data with diagnostic labels presents an opportunity for self and semi-supervised approaches to improve label efficiency for risk prediction. Though several studies have compared self-supervised approaches in natural image classification, object detection, and medical image interpretation, there is limited data on which approaches learn robust representations for risk prediction. We present a comparison of semi- and self-supervised learning to predict mortality risk using chest x-ray images. We find that a semi-supervised autoencoder outperforms contrastive and transfer learning in internal and external validation. ')
}}
{{ paper('Domain Adaptation using Silver Standard Masks for Lateral Ventricle Segmentation in FLAIR MRI',
        'Owen Crystal, April Khademi, Alan R Moody, Pejman J Maralani, Sandra E Black',
        openreview='https://openreview.net/forum?id=Ed-9HCu7l2r',
        pdf='http://proceedings.mlr.press/v121//.pdf',
        id='P237',
        paper='papers/P237',
        proceedings='',
        abstract='Lateral ventricular volume (LVV) is an important biomarker for clinical investigation. We present the first transfer learning-based LVV segmentation method for fluid-attenuated inversion recovery (FLAIR) MRI. To mitigate covariate shifts between source and target domains, this work proposes an domain adaptation method that optimizes performance on three target datasets. Silver standard (SS) masks were generated from the target domain using a novel conventional image processing ventricular segmentation algorithm and used to supplement the gold standard (GS) data from the source domain, Canadian Atherosclerosis Imaging Network (CAIN). Four models were tested on held-out test sets from four datasets: 1) SS+GS: trained on target SS masks and fine-tuned on source GS masks, 2) GS+SS: trained on source GS masks and fine-tuned on target SS masks, 3) trained on source GS (GS CAIN Only) and 4) trained on target SS masks (SS Only). The SS+GS model had the best and most consistent performance (mean DSC = 0.89, CoV = 0.05) and showed significantly p < 0.05) higher DSC compared to the GS-only model on three target domains. Results suggest pre-training with noisy labels from the target domain allows the model to adapt to the dataset-specific characteristics and provides robust parameter initialization while fine-tuning with GS masks allows the model to learn detailed features. This method has wide application to other medical imaging problems where labeled data is scarce, and can be used as a per-dataset calibration method to accelerate wide-scale adoption. ')
}}
[% / %]



[![Short program](images/program.png)](images/program.png)
Note that Nashville is on the [UTC-5 timezone](https://www.timeanddate.com/time/zone/usa/nashville).
