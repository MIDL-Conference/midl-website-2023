---
title: "Virtual event"
---
{% from "_macros.html" import paper %}
# Virtual event

[% .papers %]
{{ paper('A Robust Mean Teacher Framework for Semi-Supervised Cell Detection in Histopathology Images',
        'Ziqi Wen, Chuyang Ye',
        openreview='https://openreview.net/forum?id=PEWigppmw3b',
        pdf='https://openreview.net/pdf?id=PEWigppmw3b',
        id='P015',
        paper='papers/P015',
        proceedings='',
        abstract='Cell detection in histopathology images facilitates clinical diagnosis, and deep learning methods have been applied to the detection problem with substantially improved performance. However, cell detection methods based on deep learning usually require a large number of annotated training samples, which are costly and time-consuming to obtain, and it is desirable to develop methods where detection networks can be adequately trained with only a few annotated training samples. Since unlabeled data is much less expensive to obtain, it is possible to address this problem with semi-supervised learning, where abundant unlabeled data is combined with the limited annotated training samples for network training. In this work, we propose a semi-supervised object detection method for cell detection in histopathology images, which is based on and improves the mean teacher framework. In standard mean teacher, the detection results on unlabeled data given by the teacher model can be noisy, which may negatively impact the learning of the student model. To address this problem, we propose to suppress the noise in the detection results of the teacher model by mixing the unlabeled training images with labeled training images of which the ground truth detection results are available. In addition, we propose to further incorporate a loss term that is robust to noise when the the student model learns from the teacher model. To evaluate the proposed method, experiments were performed on a publicly available dataset for multi-class cell detection, and the experimental results show that our method improves the performance of cell detection in histopathology images in the semi-supervised setting.',
        video='https://youtu.be/SKtcmrrD6xo')
}}
{{ paper('Real-Time Quantitative Ultrasound and Radar Knowledge-Based Medical Imaging',
        'Tom Sharon, Hila Naaman, Yonathan Eder, Yonina C. Eldar',
        openreview='https://openreview.net/forum?id=B2Cb5y2A6DJ',
        pdf='https://openreview.net/pdf?id=B2Cb5y2A6DJ',
        id='S016',
        paper='papers/S016',
        proceedings='',
        abstract='Ultrasound and radar signals are useful for medical imaging due to their non-invasive, non-radiative, low-cost, and accessible nature. However, traditional imaging techniques lack resolution, contrast, and physical interpretation. Quantitative medical imaging is necessary for this purpose, as it provides a visual representation of physical characteristics. However, current techniques have drawbacks, including convergence to local minima and delayed results, which can lead to unsatisfactory outcomes. To address these limitations, we propose a neural network that incorporates the symmetries and properties of the received signals to achieve real-time quantitative mappings of physical properties. Our method achieves high accuracy using several numerical metrics for complex shapes with less than 0.15 seconds per test sample, compared to 0.75-2 hours for the competing method. ',
        video='https://youtu.be/IJH6QYnmvU0')
}}
{{ paper('A Deep-Learning Based Approach to Accelerate Groundtruth Generation for Biomarker Status Identification in Chromogenic Duplex Images',
        'Satarupa Mukherjee, Qinle Ba, Jim Martin, Yao Nie',
        openreview='https://openreview.net/forum?id=dI6wYt1qr1o',
        pdf='https://openreview.net/pdf?id=dI6wYt1qr1o',
        id='S023',
        paper='papers/S023',
        proceedings='',
        abstract='Immunohistochemistry based companion diagnosis relies on the examination of single biomarkers for patient stratification. However, recent years have seen an increasing need to characterize the interactions among biomarkers in the tumor microenvironment. To this end, chromogenic multiplexing immunohistochemistry (mIHC) serves as a promising solution, which enables simultaneous detection of multiple biomarkers in the same tissue sections. To automate whole-slide scoring for mIHC, a crucial analysis step involves the identification of cell locations along with their biomarker staining status (presence/absence of positive staining signals), which we call biomarker status identification. However, developing algorithms for such analysis, especially deep-learning (DL) models, often requires manual labeling at the cell-level, which is time-consuming and resource-intensive. Here, we present a DL based method to accelerate groundtruth label generation for chromogenic duplex (tissue samples stained with two biomarkers) images. We first generated approximate cell labels and then developed a DL based interactive segmentation system to efficiently refine the cell labels. Our method avoided extensive manual labeling and reduced the time of label generation to 50%-25% of manual labeling, while achieving $<$5% error rate in pathologist review.',
        video='https://youtu.be/_uSRj0-Pqe4')
}}
{{ paper('Generation of Multi-modal Brain Tumor MRIs with Disentangled Latent Diffusion Model',
        'Yoonho Na, Kyuri Kim, Sung-Joon Ye, Hwiyoung Kim, Jimin Lee',
        openreview='https://openreview.net/forum?id=4HHb2cTgbO1',
        pdf='https://openreview.net/pdf?id=4HHb2cTgbO1',
        id='S027',
        paper='papers/S027',
        proceedings='',
        abstract='Deep-learning based image generation methods have been widely used to overcome data deficiency.  The same is true also as in medical field, where data shortage problem is frequent. In this study, we propose multi-modal brain tumor Magnetic Resonance Imaging (MRI) generation framework, called Disentangled Latent Diffusion Model (DLDM) to tackle data deficiency in medical imaging.  We train an autoencoder that disentangles the feature of multi-modal MR images into modality-sharing and modality-specific representations.  By utilizing the feature disentanglement learned from the autoencoder, we were able to train a diffusion model that can generate modality-sharing and modality-specific latent vector.  We evaluate our approach with clean-FID and improved precision \\& recall. The results were compared with GAN-based model, StyleGAN2.',
        video='None')
}}
{{ paper('Reproducibility of the Methods in Medical Imaging with Deep Learning.',
        'Attila Simkó, Anders Garpebring, Joakim Jonsson, Tufve Nyholm, Tommy Löfstedt',
        openreview='https://openreview.net/forum?id=_P59zCfXOt',
        pdf='https://openreview.net/pdf?id=_P59zCfXOt',
        id='O029',
        paper='papers/O029',
        proceedings='',
        abstract='Concerns about the reproducibility of deep learning research are more prominent than ever, with no clear solution in sight. The Medical Imaging with Deep Learning (MIDL) conference has made advancements in employing empirical rigor with regards to reproducibility by advocating open access, and recently also recommending authors to make their code public---both aspects being adopted by the majority of the conference submissions.  We have evaluated all accepted full paper submissions to MIDL between 2018 and 2022 using established, but adjusted guidelines addressing the reproducibility and quality of the public repositories.  The evaluations show that publishing repositories and using public datasets are becoming more popular, which helps traceability, but the quality of the repositories shows room for improvement in every aspect. Merely 22% of all submissions contain a repository that was deemed repeatable using our evaluations.  From the commonly encountered issues during the evaluations, we propose a set of guidelines for machine learning-related research for medical imaging applications, adjusted specifically for future submissions to MIDL. We presented our results to future MIDL authors who were eager to continue an open discussion on the topic of code reproducibility.',
        video='https://youtu.be/bNSsm0ptYmQ')
}}
{{ paper('Data-Free One-Shot Federated Regression: An Application to Bone Age Assessment',
        'Zhou Zheng, Yuichiro Hayashi, Masahiro Oda, Takayuki Kitasaka, Kensaku Mori',
        openreview='https://openreview.net/forum?id=A--Xy77jTa',
        pdf='https://openreview.net/pdf?id=A--Xy77jTa',
        id='S030',
        paper='papers/S030',
        proceedings='',
        abstract='We consider a novel problem setting: data-free one-shot federated regression. This setting aims to prepare a global model through a single round of communication without relying on auxiliary information, e.g., proxy datasets. To address this problem, we propose a practical framework that consists of three stages: local training, data synthesizing, and knowledge distillation, and demonstrate its efficacy with an application to bone age assessment. We conduct validation under independent and identical distribution (IID) and non-IID settings while considering both model homogeneity and heterogeneity. Validation results show that our method surpasses FedAvgOneShot by a large margin and sometimes even outperforms the proxy-data-dependent approach FedOneShot.',
        video='https://youtu.be/yBLyiUdDKYw')
}}
{{ paper('Rotation-Scale Equivariant Steerable Filters',
        'Yilong Yang, Srinandan Dasmahapatra, Sasan Mahmoodi',
        openreview='https://openreview.net/forum?id=A0MyiAwE_E4',
        pdf='https://openreview.net/pdf?id=A0MyiAwE_E4',
        id='P032',
        paper='papers/P032',
        proceedings='',
        abstract='Incorporating either rotation equivariance or scale equivariance into CNNs has proved to be effective in improving models’ generalization performance. However, jointly integrating rotation and scale equivariance into CNNs has not been widely explored. Digital histology imaging of biopsy tissue can be captured at arbitrary orientation and magnification and stored at different resolutions, resulting in cells appearing in different scales. When conventional CNNs are applied to histopathology image analysis, the generalization performance of models is limited because 1) a part of the parameters of filters are trained to fit rotation transformation, thus decreasing the capability of learning other discriminative features; 2) fixed-size filters trained on images at a given scale fail to generalize to those at different scales. To deal with these issues, we propose the Rotation-Scale Equivariant Steerable Filter (RSESF), which incorporates steerable filters and scale-space theory. The RSESF contains copies of filters that are linear combinations of Gaussian filters, whose direction is controlled by directional derivatives and whose scale parameters are trainable but constrained to span disjoint scales in successive layers of the network. Extensive experiments on two gland segmentation datasets demonstrate that our method outperforms other approaches, with much fewer trainable parameters and fewer GPU resources required. The source code is available at: https://github.com/ynulonger/RSESF.',
        video='https://youtu.be/8PtZLo2Ihkw')
}}
{{ paper('Comp2Comp: Open-Source Body Composition Assessment on Computed Tomography',
        'Louis Blankemeier, Malte Jensen, Eduardo Pontes Reis, Juan Manuel Zambrano Chaves, Adrit Rao, Sally Yao, Pauline Margaret Berens, Andrew Wentland, Bhanushree Bahl, Kushboo Arora, Oliver Oppers Aalami, Bhavik Patel, Leon Lenchik, Marc H. Willis, Robert D. Boutin, Arjun D Desai, Akshay S Chaudhari',
        openreview='https://openreview.net/forum?id=VcgBBAQfMP',
        pdf='https://openreview.net/pdf?id=VcgBBAQfMP',
        id='S044',
        paper='papers/S044',
        proceedings='',
        abstract='Computed tomography (CT) can provide quantitative body composition metrics of tissue volume, morphology, and quality which are valuable for disease prediction and prognostication. However, manually extracting these measures is a cumbersome and time-consuming task. Proprietary software to automate this process exist, but these software are closed-source, impeding large-scale access to and usage of these tools. To address this, we have built Comp2Comp, an open-source Python package for rapid and automated body composition analysis of CT scans. The primary advantages of Comp2Comp are its open-source nature, the inclusion of multiple tissue analysis capabilities within a single package, and its extensible design. We discuss the architecture of Comp2Comp and report initial validation results. Comp2Comp can be found at https://github.com/StanfordMIMI/Comp2Comp.',
        video='None')
}}
{{ paper('Shape Equivariant Learning for Robust MRI Segmentation',
        'Ainkaran Santhirasekaram, Mathias Winkler, Andrea G. Rockall, Ben Glocker',
        openreview='https://openreview.net/forum?id=TyA5AyU_tSv',
        pdf='https://openreview.net/pdf?id=TyA5AyU_tSv',
        id='S045',
        paper='papers/S045',
        proceedings='',
        abstract='The reliability of deep learning based segmentation models is essential to the safe translation of these models into clinical practise. Unfortunately, these models are sensitive to distributional shifts. This is particularly notable in MRI, where there is a large variation of acquisition protocols across different domains leading to varying textural profiles. We hypothesise that the constrained anatomical variability across subjects can be leveraged to discretize the latent space to a dictionary of shape components. We achieve this by using multiple MRI sequences to learn texture invariant and shape equivariant features which are used to construct a shape dictionary using vector quantisation. This dictionary is then sampled to compose the segmentation output. Our method achieves SOTA performance in the task of single domain generalisation (SDG) for prostate zonal segmentation.',
        video='https://youtu.be/3UyFKHH6_Yg')
}}
{{ paper('Video pretraining advances 3D deep learning on chest CT tasks',
        'Alexander Ke, Shih-Cheng Huang, Chloe P O\'Connell, Michal Klimont, Serena Yeung, Pranav Rajpurkar',
        openreview='https://openreview.net/forum?id=zhpP7zluLBk',
        pdf='https://openreview.net/pdf?id=zhpP7zluLBk',
        id='P046',
        paper='papers/P046',
        proceedings='',
        abstract='Pretraining on large natural image classification datasets such as ImageNet has aided model development on data-scarce 2D medical tasks. 3D medical tasks often have much less data than 2D medical tasks, prompting practitioners to rely on pretrained 2D models to featurize slices. However, these 2D models have been surpassed by 3D models on 3D computer vision benchmarks since they do not natively leverage cross-sectional or temporal information. In this study, we explore whether natural video pretraining for 3D models can enable higher performance on smaller datasets for 3D medical tasks. We demonstrate video pretraining improves the average performance of seven 3D models on two chest CT datasets, regardless of finetuning dataset size, and that video pretraining allows 3D models to outperform 2D baselines. Lastly, we observe that pretraining on the large-scale out-of-domain Kinetics dataset improves performance more than pretraining on a typically-sized in-domain CT dataset. Our results show consistent benefits of video pretraining across a wide array of architectures, tasks, and training dataset sizes, supporting a shift from small-scale in-domain pretraining to large-scale out-of-domain pretraining for 3D medical tasks.',
        video='None')
}}
{{ paper('Learning Retinal Representations from Multi-modal Imaging via Contrastive Pre-training',
        'Emese Sükei, Elisabeth Rumetshofer, Niklas Schmidinger, Ursula Schmidt-Erfurth, Günter Klambauer, Hrvoje Bogunović',
        openreview='https://openreview.net/forum?id=newlahoISt1',
        pdf='https://openreview.net/pdf?id=newlahoISt1',
        id='S055',
        paper='papers/S055',
        proceedings='',
        abstract="Contrastive representation learning techniques trained on large multi-modal datasets, such as CLIP and CLOOB, have demonstrated impressive capabilities of producing highly transferable representations for different downstream tasks. In the field of ophthalmology, large multi-modal datasets are conveniently accessible as retinal imaging scanners acquire both 2D fundus images and 3D optical coherence tomography to evaluate the disease. Motivated by this, we propose a CLIP/CLOOB objective-based model to learn joint representations of the two retinal imaging modalities. We evaluate our model\\'s capability to accurately retrieve the appropriate OCT based on a fundus image belonging to the same eye. Furthermore, we showcase the transferability of the obtained representations by conducting linear probing and fine-tuning on several prediction tasks from OCT.",
        video='https://youtu.be/8anDKyJuGe0')
}}
{{ paper('Nearest Neighbor Radiomics for Self-Supervised Chest X-ray Pneumonia Identification',
        'Cailin Winston, Caleb Winston, Chloe Winston',
        openreview='https://openreview.net/forum?id=rUpjCWd0BB',
        pdf='https://openreview.net/pdf?id=rUpjCWd0BB',
        id='S067',
        paper='papers/S067',
        proceedings='',
        abstract='Self-supervised training minimizes a contrastive loss objective for unlabeled data. Contrastive loss estimates the distance in the latent space between positive pairs, which are pairs of images that are expected to have the same label. For medical images, choosing positive pairs is challenging because simple transformations like rotations or blurs are not class-invariant. In this paper, we show that choosing positive pairs with nearest-neighbor radiomics features for self-supervised training improves chest X-ray pneumonia identification accuracy by 8.4% without labeled data.',
        video='None')
}}
{{ paper('Semantic Segmentation of 3D Medical Images Through a Kaleidoscope: Data from the Osteoarthritis Initiative',
        'Boyeong Woo, Marlon Bran Lorenzana, Craig Engstrom, William Baresic, Jurgen Fripp, Stuart Crozier, Shekhar S. Chandra',
        openreview='https://openreview.net/forum?id=80ZHtBKHKHo',
        pdf='https://openreview.net/pdf?id=80ZHtBKHKHo',
        id='P070',
        paper='papers/P070',
        proceedings='',
        abstract='While there have been many studies on using deep learning for medical image analysis, the lack of manually annotated data remains a challenge in training a deep learning model for segmentation of medical images. This work shows how the kaleidoscope transform (KT) can be applied to a 3D convolutional neural network to improve its generalizability when the training set is extremely small. In this study, the KT was applied to a context aggregation network (CAN) for semantic segmentation of anatomical structures in knee MR images. In the proposed model, KAN3D, the input image is rearranged into a batch of downsampled images (KT) before the convolution operations, and then the voxels are rearranged back to their original positions (inverse KT) after the convolution operations to produce the predicted segmentation mask for the input image. Compared to the CAN3D (without the KT), the KAN3D was able to reduce overfitting without data augmentation while maintaining a fast training and inference time. The paper discusses the observed advantages and disadvantages of KAN3D.',
        video='https://youtu.be/03tWDzQfWlg')
}}
{{ paper('Multimodal Image-Text Matching Improves Retrieval-based Chest X-Ray Report Generation',
        'Jaehwan Jeong, Katherine Tian, Andrew Li, Sina Hartung, Subathra Adithan, Fardad Behzadi, Juan Calle, David Osayande, Michael Pohlen, Pranav Rajpurkar',
        openreview='https://openreview.net/forum?id=aZ0OuYMSMMZ',
        pdf='https://openreview.net/pdf?id=aZ0OuYMSMMZ',
        id='P076',
        paper='papers/P076',
        proceedings='',
        abstract='Automated generation of clinically accurate radiology reports can improve patient care. Previous report generation methods that rely on image captioning models often generate incoherent and incorrect text due to their lack of relevant domain knowledge, while retrieval-based attempts frequently retrieve reports that are irrelevant to the input image. In this work, we propose Contrastive X-Ray REport Match (X-REM), a novel retrieval-based radiology report generation module that uses an image-text matching score to measure the similarity of a chest X-ray image and radiology report for report retrieval. We observe that computing the image-text matching score with a language-image model can effectively capture the fine-grained interaction between image and text that is often lost when using cosine similarity. X-REM outperforms multiple prior radiology report generation modules in terms of both natural language and clinical metrics. Human evaluation of the generated reports suggests that X-REM increased the number of zero-error reports and decreased the average error severity compared to the baseline retrieval approach. Our code is available at: https://github.com/rajpurkarlab/X-REM',
        video='https://youtu.be/jqlCFoU-w2U')
}}
{{ paper('Uncertainty for Proximal Femur Fractures Classification',
        'Selina Frenner, Mayar Lotfy, Marc Beirer, Peter Biberthaler, Shadi Albarqouni',
        openreview='https://openreview.net/forum?id=kvpAErerdkc',
        pdf='https://openreview.net/pdf?id=kvpAErerdkc',
        id='S082',
        paper='papers/S082',
        proceedings='',
        abstract='Deep Learning methods over the past years provided high-performance solutions for the medical applications. Yet, robustness and quality control is still required for clinical applicability. In this work, the uncertainty of proximal femur fracture classification,was modeled. We introduce a reliability measure to our predictive model using the Monte Carlo Dropout approach. We performed an extensive quantitative and qualitative analysis to validate the results. We further exposed the results to expert physicians in order to get feedback on the model’s performance and uncertainty measures. Results demonstrate a positive correlation between the miss-classification of the model’s prediction and high uncertainty scores. Additionally, the uncertainty measures are mimicking the actual radiologist’s uncertainty for challenging examples reflected on intra- and inter- experts variability.',
        video='https://youtu.be/izOwvBHzejA')
}}
{{ paper('Incomplete learning of multi-modal connectome for brain disorder diagnosis via modal-mixup and deep supervision',
        'Yanwu Yang, Hairui Chen, Zhikai Chang, Yang Xiang, Chenfei Ye, Ting Ma',
        openreview='https://openreview.net/forum?id=WjrcYNTPunQ',
        pdf='https://openreview.net/pdf?id=WjrcYNTPunQ',
        id='P082',
        paper='papers/P082',
        proceedings='',
        abstract='Recently, the study of multi-modal brain networks has dramatically facilitated the efficiency in brain disorder diagnosis by characterizing multiple types of connectivity of brain networks and their intrinsic complementary information. Despite the promising performance achieved by multi-modal technologies, most existing multi-modal approaches can only learn from samples with complete modalities, which wastes a considerable amount of mono-modal data. Otherwise, most existing data imputation approaches still rely on a large number of samples with complete modalities. In this study, we propose a modal-mixup data imputation method by randomly sampling incomplete samples and synthesizing them into complete data for auxiliary training. Moreover, to mitigate the noise in the complementary information between unpaired modalities in the synthesized data, we introduce a bilateral network with deep supervision for improving and regularizing mono-modal representations with disease-specific information. Experiments on the ADNI dataset demonstrate the superiority of our proposed method for disease classification in terms of different rates of samples with complete modalities.',
        video='https://youtu.be/4eLh_bwT_Tk')
}}
{{ paper('Overcoming Interpretability and Accuracy Trade-off in Medical Imaging',
        'Ivaxi Sheth, Samira Ebrahimi Kahou',
        openreview='https://openreview.net/forum?id=BSf6JALJoc',
        pdf='https://openreview.net/pdf?id=BSf6JALJoc',
        id='S087',
        paper='papers/S087',
        proceedings='',
        abstract='Neural networks are considered black boxes. Deploying them into the healthcare domain poses a challenge in understanding model behavior beyond final prediction. There have been recent attempts to establish the trustworthiness of a model. Concept learning models provide insight into the model by introducing a bottleneck layer before the final prediction. They encourage interpretable insights into deep learning models by conditioning final predictions on intermediate predictions of explainable high-level concepts. However, using concept-based models causes a drop in performance which poses an accuracy vs explainability trade-off. To overcome this challenge we propose Coop-CBM, a novel concept learning model. We validate the performance of Coop-CBM on diverse dermatology and histopathology images. ',
        video='https://youtu.be/oYUIteM6cz0')
}}
{{ paper('ζ-mixup: Richer, More Realistic Mixing of Multiple Images',
        'Kumar Abhishek, Colin Joseph Brown, Ghassan Hamarneh',
        openreview='https://openreview.net/forum?id=iXjsAarmqn',
        pdf='https://openreview.net/pdf?id=iXjsAarmqn',
        id='S098',
        paper='papers/S098',
        proceedings='',
        abstract='Data augmentation (DA), an effective regularization technique, generates training samples to enhance the diversity of data and the richness of label information for training modern deep learning models. mixup, a popular recent DA method, augments training datasets with convex combinations of original samples pairs, but can generate undesirable samples, with data being sampled off the manifold and with incorrect labels. In this work, we propose ζ-mixup, a generalization of mixup with provably and demonstrably desirable properties that allows for convex combinations of $N \\geq 2$ samples, thus leading to more realistic and diverse outputs that incorporate information from $N$ original samples using a $p$-series interpolant. We show that, compared to mixup, ζ-mixup better preserves the intrinsic dimensionality of the original datasets, a desirable property for training generalizable models, and is at least as fast as mixup. Evaluation on several natural and medical image datasets shows that ζ-mixup outperforms mixup, CutMix, and traditional DA methods.',
        video='https://youtu.be/K1Y8kMdaqjo')
}}
{{ paper('Facial AU-aid hypomimia diagnosis based on GNN',
        'Yingjing Xu, Bo Lin, Wei Luo, Shuiguang Deng, Jianwei Yin',
        openreview='https://openreview.net/forum?id=BLWmZy6kSL7',
        pdf='https://openreview.net/pdf?id=BLWmZy6kSL7',
        id='S101',
        paper='papers/S101',
        proceedings='',
        abstract="Hypomimia is a prevalent symptom of Parkinson\\'s Disease(PD). It is characterized by reduced facial expression and delayed facial movement. The work proposes a framework to use Graph Neural Network(GNN) to extract related action unit(AU) features on the facial smiling videos to help to improve the recognition of hypomimia with PD. AU is an effective representation of the facial state and movement, while GNN has great capability to present relationship information between facial areas. A related AU representation can pay more attention to the relationships between the facial areas in order to increase the accuracy of the diagnosis. Experiments were conducted using an in-house dataset of 105 facial smiling videos, which contains 55 healthy control(HC) participants and 50 PD patients. Our method\\'s performance was compared to that of random forest (RF) and support vector machine (SVM) classifiers.  Our method achieved an Accuracy, PPV, TPR, and F1 score of {91.7%, 92.8%, 90.6%, 91.7%}, while the RF and SVM achieved {84.5%,84.8%, 82.7\\%, 83.7%} and {88.7%, 88.0%, 88,7%, 88.3%} respectively on the dataset. ",
        video='None')
}}
{{ paper('Automatic Contrast Phase Detection on Abdominal Computed Tomography using Clinically-Inspired Techniques',
        'Eduardo Pontes Reis, Louis Blankemeier, Juan Manuel Zambrano Chaves, Malte Jensen, Sally Yao, Cesar Augusto Madid Truyts, Marc H. Willis, Robert D. Boutin, Edson Amaro Jr, Akshay S Chaudhari',
        openreview='https://openreview.net/forum?id=B8e-iS9j43',
        pdf='https://openreview.net/pdf?id=B8e-iS9j43',
        id='S112',
        paper='papers/S112',
        proceedings='',
        abstract='Accurately determining contrast phase in an abdominal computed tomography (CT) series is an important step prior to deploying downstream artificial intelligence methods trained to operateon the specific series. Inspired by how radiologists assess contrast phase status, this paper presents a simple approach to automatically detect the contrast phase. This method combines features extracted from the segmentation of key anatomical structures with a gradient boosting classifier for this task. The algorithm demonstrates high accuracy in categorizing the images into non-contrast (96.6\\% F1 score), arterial (78.9\\% F1 score), venous (92.2\\% F1 score), and delayed phases (95.0\\% F1 score), making it a valuable tool for enhancing AI applicability in medical imaging.',
        video='https://youtu.be/LFzh_w15hSM')
}}
{{ paper('Expansion Microscopy Imaging Isotropic Restoration by Unsupervised Deep Learning',
        'Meng-Yun Wu, Da-Yu Huang, Ya-Ding Liu, Li-An Chu, Gary.  Han Chang',
        openreview='https://openreview.net/forum?id=NiUSj5tDKf',
        pdf='https://openreview.net/pdf?id=NiUSj5tDKf',
        id='S114',
        paper='papers/S114',
        proceedings='',
        abstract='The development of fluorescence light sheets and expansion microscopy (ExM) in recent years enables the visualization of detailed neural structures to help unlock the secrets of neural functioning. Deep learning techniques have then become essential tools to process the ever-increasing amount of high-quality and high-resolution images. In this study, we developed a single-scale deconvolution model for extracting multiscale deconvoluted response (MDR) from the volumes of microscopy images of neurons and generative models to translate images between the lateral and axial views. The results demonstrated that deep learning as a promising tool in approving image volume quality and comprehension of structural information of light sheet microscopy.',
        video='https://youtu.be/YFv548AxPy8')
}}
{{ paper('Improving Zero-Shot Detection of Low Prevalence Chest Pathologies using Domain Pre-trained Language Models',
        'Aakash Mishra, Rajat Mittal, Christy Jestin, Kostas Tingos, Pranav Rajpurkar',
        openreview='https://openreview.net/forum?id=tQvYo-DMrO',
        pdf='https://openreview.net/pdf?id=tQvYo-DMrO',
        id='S120',
        paper='papers/S120',
        proceedings='',
        abstract="Recent advancements in zero-shot learning have enabled the use of paired image-text data to replace structured labels, replacing the need for expert annotated datasets. Domain pre-trained models, such as CXR-BERT, BlueBERT, and ClinicalBERT, offer the potential to improve the performance of CLIP-like models with specific domain knowledge by replacing BERT weights at the cost of breaking the original model\\'s alignment. We evaluate the performance of zero-shot classification models with domain-specific pre-training for detecting low-prevalence pathologies. Even though replacing the weights of the original CLIP-BERT degrades model performance on commonly found pathologies, we show that pre-trained text towers perform exceptionally better on low-prevalence diseases. This motivates future ensemble models with a combination of differently trained language models for maximal performance.",
        video='https://youtu.be/mFRnZMp_X_k')
}}
{{ paper('Bias Field Correction in MRI with Hampel Noise Denoising Diffusion Probabilistic Model',
        'Junhyeok Lee, Junghwa Kang, Yoonho Nam, TaeYoung Lee',
        openreview='https://openreview.net/forum?id=Ob7xQXamjo_',
        pdf='https://openreview.net/pdf?id=Ob7xQXamjo_',
        id='S121',
        paper='papers/S121',
        proceedings='',
        abstract='Non-uniform bias field due to external factors hampers quantitative MR image analysis. For reliable quantitative MR image analysis, appropriate correction for the bias field is necessary. In this study, we propose Hampel denoising diffusion model to effectively correct the bias field from MR images. Compared with N4 and Gaussian denoising diffusion models, the proposed model provided higher PSNRs, SSIMs and lower MSEs. Higher efficiency could be achieved compared to N4 when our model takes 9 times faster in inference time.',
        video='https://youtu.be/EEXFKUhQdO4')
}}
{{ paper('CSGAN: a consistent structural GAN for AS-OCT image despeckling by image translation',
        'Sanqian Li, Muxing Xiong, Risa Higashita, Jiang Liu',
        openreview='https://openreview.net/forum?id=JY4oJg6-gc',
        pdf='https://openreview.net/pdf?id=JY4oJg6-gc',
        id='S123',
        paper='papers/S123',
        proceedings='',
        abstract='Anterior segment optical coherence tomography (AS-OCT) is a recent imaging technique for visualizing the physiological structure of the anterior segment. The speckle noise inherited in ASOCT images degrades the visual quality and hampers the subsequent medical analysis. Previous work was devoted to removing the speckles and acquiring satisfying images. According to the clinical requirements, it might be desirable to maintain locally higher data fidelity instead of enforcing visually appealing but rather wrong image structural features. Catering to this expectation, we propose a Consistent Structural Generative Adversarial Network (CSGAN) to learn the clean style of low-speckle in repeated AS-OCT images and simultaneously preserve the tiny but vital structural knowledge among the latent feature, spatial and frequency domains. Specifically, we design a latent constraint into the generator to capture the inherent content in the feature domain and adopt the perceptual similarities to directly preserve structural detail in the spatial dimension. Besides, we introduce a focal frequency scheme that adaptively represents and distinguishes hard frequencies to compensate for the spatial loss and refine the generated image to improve image quality. Finally, the experimental results demonstrate that the CSGAN can achieve satisfactory despeckling results with preserving structural details on the AS-Casia dataset.',
        video='https://youtu.be/gtY_1ATeWAo')
}}
{{ paper('Semi-supervised Learning with Contrastive and Topology Losses for Catheter Segmentation and Misplacement Prediction',
        'Tianyu Hwang, Chih-Hung Wang, Holger R Roth, Dong Yang, Can Zhao, Chien-Hua Huang, Weichung Wang',
        openreview='https://openreview.net/forum?id=9mPSPWo5tzu',
        pdf='https://openreview.net/pdf?id=9mPSPWo5tzu',
        id='P129',
        paper='papers/P129',
        proceedings='',
        abstract="Chest X-ray images are often used to determine the proper placement of catheters, as incorrect placement can lead to severe complications. With the advent of deep learning, computer-aided detection methods have been developed to assist radiologists in identifying catheter misplacement by detecting and highlighting the catheter\\'s path. However, obtaining large, pixel-wise labeled datasets can be challenging due to the labor-intensive nature of annotation. To address this issue, we proposed a novel semi-supervised learning method that combines contrastive loss and topology loss. This method takes advantage of the known topological properties of catheters and does not require extensive labeling. We collected 7,378 chest X-ray images from the *****, which were labeled for misplacement of nasogastric and endotracheal tube catheters, and included pixel-wise annotation. Moreover, the CLiP dataset was used as an unlabeled dataset for semi-supervised learning. We used a hybrid U-Net architecture with an added classification head to perform simultaneous segmentation of the catheter and misplacement classification. Our model achieved an average AUC of 0.977 for classification and a average Dice score of 0.598 for segmentation.",
        video='https://youtu.be/pLRFWXEZqI0')
}}
{{ paper('DBGSL: Dynamic Brain Graph Structure Learning',
        'Alexander Campbell, Antonio Giuliano Zippo, Luca Passamonti, Nicola Toschi, Pietro Lio',
        openreview='https://openreview.net/forum?id=Us31horKNLG',
        pdf='https://openreview.net/pdf?id=Us31horKNLG',
        id='P138',
        paper='papers/P138',
        proceedings='',
        abstract='Recently, graph neural networks (GNNs) have shown success at learning representations of brain graphs derived from functional magnetic resonance imaging (fMRI) data. The majority of existing GNN methods, however, assume brain graphs are static over time and the graph adjacency matrix is known prior to model training. These assumptions are at odds with neuroscientific evidence that brain graphs are time-varying with a connectivity structure that depends on the choice of functional connectivity measure. Noisy brain graphs that do not truly represent the underling fMRI data can have a detrimental impact on the performance of GNNs. As a solution, we propose Dynamic Brain Graph Structure Learning (DBGSL), a novel method for learning the optimal time-varying dependency structure of fMRI data induced by a downstream prediction task. Experiments demonstrate DBGSL achieves state-of-the-art performance for sex classification using real-world resting-state and task fMRI data. Moreover, analysis of the learnt dynamic graphs highlights prediction-related brain regions which align with existing neuroscience literature.',
        video='None')
}}
{{ paper('DBGDGM: Dynamic Brain Graph Deep Generative Model',
        'Alexander Campbell, Simeon Emilov Spasov, Nicola Toschi, Pietro Lio',
        openreview='https://openreview.net/forum?id=WHS3Zv9pxz',
        pdf='https://openreview.net/pdf?id=WHS3Zv9pxz',
        id='P139',
        paper='papers/P139',
        proceedings='',
        abstract='Graphs are a natural representation of brain activity derived from functional magnetic imaging (fMRI) data. It is well known that clusters of anatomical brain regions, known as functional connectivity networks (FCNs), encode temporal relationships which can serve as useful biomarkers for understanding brain function and dysfunction. Previous works, however, ignore the temporal dynamics of the brain and focus on static graphs. In this paper, we propose a dynamic brain graph deep generative model (DBGDGM) which simultaneously clusters brain regions into temporally evolving communities and learns dynamic unsupervised node embeddings. Specifically, DBGDGM represents brain graph nodes as embeddings sampled from a distribution over communities that evolve over time. We parameterise this community distribution using neural networks that learn from subject and node embeddings as well as past community assignments. Experiments demonstrate DBGDGM outperforms baselines in graph generation, dynamic link prediction, and is comparable for graph classification. Finally, an analysis of the learnt community distributions reveals overlap with known FCNs reported in neuroscience literature.',
        video='None')
}}
{{ paper('Evaluating Adversarial Robustness of Low dose CT Recovery',
        'Kanchana Vaishnavi Gandikota, Paramanand Chandramouli, Hannah Dröge, Michael Moeller',
        openreview='https://openreview.net/forum?id=L-N1uAxfQk1',
        pdf='https://openreview.net/pdf?id=L-N1uAxfQk1',
        id='P166',
        paper='papers/P166',
        proceedings='',
        abstract='Low dose computer tomography (CT) acquisition using reduced radiation or sparse angle measurements is recommended to decrease the harmful effects of X-ray radiation. Recent works successfully apply deep networks to the problem of low dose CT recovery on benchmark datasets. However, their robustness needs a thorough evaluation before use in clinical settings. In this work, we evaluate the robustness of different deep learning  approaches and classical methods for CT recovery.We show that deep networks, including model based networks encouraging data consistency are more susceptible to untargeted attacks. Surprisingly, we observe that data consistency is not heavily affected  even for these poor quality reconstructions, motivating the need for better regularization for the networks. We demonstrate the feasibility of  universal attacks and study attack transferability across different methods.  We analyze robustness to attacks causing localized changes in clinically relevant regions. Both classical approaches and deep networks are affected by such attacks leading to change in  visual appearance of localized lesions, for extremely small perturbations. As the resulting reconstructions have high data consistency with original measurements, these localized attacks can be used to explore the solution space of CT recovery problem. ',
        video='https://youtu.be/2kI-rHBoaIg')
}}
{{ paper('Inherent Consistent Learning for Accurate Semi-supervised Medical Image Segmentation',
        'Ye Zhu, Jie Yang, Siqi Liu, Ruimao Zhang',
        openreview='https://openreview.net/forum?id=diXhe9kUnQ',
        pdf='https://openreview.net/pdf?id=diXhe9kUnQ',
        id='O179',
        paper='papers/O179',
        proceedings='',
        abstract='Semi-supervised medical image segmentation has attracted much attention in recent years because of the high cost of medical image annotations. In this paper, we propose a novel Inherent Consistent Learning (ICL) method, aims to learn robust semantic category representations through the semantic consistency guidance of labeled and unlabeled data to help segmentation. In practice, we introduce two external modules, namely Supervised Semantic Proxy Adaptor (SSPA) and Unsupervised Semantic Consistent Learner (USCL) that is based on the attention mechanism to align the semantic category representations of labeled and unlabeled data, as well as update the global semantic representations over the entire training set. The proposed ICL is a plug-and-play scheme for various network architectures, and the two modules are not involved in the testing stage. Experimental results on three public benchmarks show that the proposed method can outperform the state-of-the-art, especially when the number of annotated data is extremely limited. Code is available at: https://github.com/zhuye98/ICL.git',
        video='None')
}}
{{ paper('TransRP: Transformer-based PET/CT feature extraction incorporating clinical data for recurrence-free survival prediction in oropharyngeal cancer',
        'Baoqiang Ma, Jiapan Guo, Lisanne Van Dijk, P.M.A. van Ooijen, Stefan Both, Nanna Maria Sijtsema',
        openreview='https://openreview.net/forum?id=eF_6td_piu-',
        pdf='https://openreview.net/pdf?id=eF_6td_piu-',
        id='P187',
        paper='papers/P187',
        proceedings='',
        abstract='The growing number of subtypes and treatment options for oropharyngeal squamous cell carcinoma (OPSCC), a common type of head and neck cancer (HNC), highlights the need for personalized therapies. Prognostic outcome prediction models can identify different risk groups for investigation of intensified or de-escalated treatment strategies. Convolution neural networks (CNNs) have been shown to have improved predictive performance compared to traditional clinical and radiomics models by extracting comprehensive and representative features. However, CNNs are limited in their ability to learn global features within an entire volume. In this study, we propose a Transformer-based model for predicting recurrence-free survival (RFS) in OPSCC patients, called TransRP. TransRP consists of a CNN encoder to extract rich PET/CT image features, a Transformer encoder to learn global context features, and a fully connected network to incorporate clinical data for RFS prediction. We investigated three different methods for combining clinical features into TransRP. The experiments were conducted using the public HECKTOR 2022 challenge dataset, which includes pretreatment PET/CT scans, Gross Tumor Volume masks, clinical data, and RFS for OPSCC patients. The dataset was split into a test set (n = 120) and a training set (n = 362) for five-fold cross-validation. The results show that TransRP achieved the highest test concordance index of 0.698 (an improvement > 2%) in RFS prediction compared to several state-of-the-art clinical and CNN-based methods. In addition, we found that incorporating clinical features with image features obtained from the Transformer encoder performed better than using the Transformer encoder to extract features from both clinical and image features. The code for this study is available at (anonymized temporarily for review).',
        video='https://youtu.be/eVOpC1VjZms')
}}
{{ paper('Trainable Prototype Enhanced Multiple Instance Learning for Whole Slide Image Classification',
        'Litao Yang, Deval Mehta, Sidong Liu, Dwarikanath Mahapatra, Antonio Di Ieva, Zongyuan Ge',
        openreview='https://openreview.net/forum?id=P3tSZhxBwJw',
        pdf='https://openreview.net/pdf?id=P3tSZhxBwJw',
        id='P189',
        paper='papers/P189',
        proceedings='',
        abstract='Digital pathology based on whole slide images (WSIs) plays a key role in cancer diagnosis and clinical practice. Due to the high resolution of the WSI and unavailability of patch level annotations, WSI classification is usually formulated as a weakly supervised problem, which relies on multiple instance learning (MIL) based on patches of a WSI. In this paper, we aim to learn an optimal patch-level feature space by integrating prototype learning with MIL. To this end, we develop a Trainable Prototype enhanced deep MIL (TPMIL) framework for weakly supervised WSI classification. In contrast to the conventional methods which rely on a certain number of selected patches for feature space refinement, we softly cluster all the instances by allocating them to their corresponding prototypes. Additionally, our method is able to reveal the correlations between different tumor subtypes through distances between corresponding trained prototypes. More importantly, TPMIL also enables to provide a more accurate interpretability based on the distance of the instances from the trained prototypes which serves as an alternative to the conventional attention score-based interpretability. We test our method on two WSI datasets and it achieves a new SOTA.',
        video='https://youtu.be/kXBiZna7TtA')
}}
{{ paper('FUSQA: Fetal Ultrasound Segmentation Quality Assessment',
        'Sevim Cengiz, Ibrahim Almakky, Mohammad Yaqub',
        openreview='https://openreview.net/forum?id=Umyz5JHIXpD',
        pdf='https://openreview.net/pdf?id=Umyz5JHIXpD',
        id='P199',
        paper='papers/P199',
        proceedings='',
        abstract='Deep learning models have been effective for various fetal ultrasound segmentation tasks. However, generalization to new unseen data has raised questions about their effectiveness for clinical adoption. Normally, a transition to new unseen data requires time-consuming and costly quality assurance processes to validate the segmentation performance post-transition. Segmentation quality assessment efforts have focused on natural images, where the problem has been typically formulated as a dice score regression task. In this paper, we propose a simplified Fetal Ultrasound Segmentation Quality Assessment (FUSQA) model to tackle the segmentation performance deterioration challenge. We formulate the segmentation quality assessment process as an automated classification task to distinguish between good and poor quality segmentation masks for more accurate gestational age estimation. We validate the performance of our proposed approach on two datasets we collect from two hospitals using different ultrasound machines. We compare different architectures, with our best-performing architecture achieving over 90% classification accuracy on distinguishing between good and poor quality segmentation masks from an unseen dataset. Additionally, there was only a 1.45-days difference between the gestational age reported by doctors and estimated based on CRL measurements using well-segmented masks. On the other hand, this difference increased and reached up to 7.73 days when we calculated CRL from the poorly segmented masks. As a result, AI-based approaches can potentially aid fetal ultrasound segmentation quality assessment and might detect poor segmentation in real-time screening in the future.',
        video='https://youtu.be/aTh7U5oZn2I')
}}
{{ paper('SegPrompt: Using Segmentation Map as a Better Prompt to Finetune Deep Models for Kidney Stone Classification',
        'Wei Zhu, Runtao Zhou, Yuan Yao, Timothy Douglas Campbell, Rajat Kumar Jain, Jiebo Luo',
        openreview='https://openreview.net/forum?id=QXjGotk45lb',
        pdf='https://openreview.net/pdf?id=QXjGotk45lb',
        id='P200',
        paper='papers/P200',
        proceedings='',
        abstract='Recently, deep learning has produced encouraging results for kidney stone classification using endoscope images. However, the shortage of annotated training data poses a severe problem in improving the performance and generalization ability of the trained model. It is thus crucial to fully exploit the limited data at hand. In this paper, we propose SegPrompt to alleviate the data shortage problems by exploiting segmentation maps from two aspects. First, SegPrompt integrates segmentation maps to facilitate classification training so that the classification model is aware of the regions of interest. The proposed method allows the image and segmentation tokens to interact with each other to fully utilize the segmentation map information. Second, we use the segmentation maps as prompts to tune the pretrained deep model, resulting in much fewer trainable parameters than vanilla finetuning. We perform extensive experiments on the collected kidney stone dataset. The results show that SegPrompt can achieve an advantageous balance between the model fitting ability and the generalization ability, eventually leading to an effective model with limited training data.',
        video='https://youtu.be/h7haeTLoBOg')
}}
{{ paper('Intra- and Inter-Cellular Awareness for 3D Neuron Tracking and Segmentation in Large-Scale Connectomics',
        'Hao Zhai, Jing Liu, Bei Hong, Jiazheng Liu, Qiwei Xie, Hua Han',
        openreview='https://openreview.net/forum?id=3_qtVh7gTyy',
        pdf='https://openreview.net/pdf?id=3_qtVh7gTyy',
        id='P201',
        paper='papers/P201',
        proceedings='',
        abstract='Currently, most state-of-the-art pipelines for 3D micro-connectomic reconstruction deal with neuron over-segmentation, agglomeration and subcellular compartment (nuclei, mitochondria, synapses, etc.) detection separately. Inspired by the proofreading consensus of experts, we established a paradigm to acquire priori knowledge of cellular characteristics and ultrastructures, as well as determine the connectivity of neural circuits simultaneously. Following this novel paradigm, we were keen to bring the Intra- and Inter-Cellular Awareness back when Tracking and Segmenting neurons in connectomics. Our proposed method (II-CATS) utilizes few-shot learning techniques to encode the internal neurite representation and its learnable components, which could significantly impact neuron tracings. We further go beyond the original expected run length (ERL) metric by focusing on biological constraints (bERL) or spanning from the nucleus to spines (nERL). With the evaluation of these metrics, we perform typical experiments on multiple electron microscopy datasets on diverse animals and scales. In particular, our proposed method is naturally suitable for tracking neurons that have been identified by staining.',
        video='None')
}}
{{ paper('Domain adaptation using optimal transport for invariant learning using histopathology datasets',
        'Kianoush Falahkheirkhah, Alex Xijie Lu, David Alvarez-Melis, Grace Huynh',
        openreview='https://openreview.net/forum?id=nmZRTaZZv5Z',
        pdf='https://openreview.net/pdf?id=nmZRTaZZv5Z',
        id='P215',
        paper='papers/P215',
        proceedings='',
        abstract='Histopathology is critical for the diagnosis of many diseases, including cancer. These protocols typically require pathologists to manually evaluate slides under a microscope, which is time-consuming and subjective, leading to interest in machine learning to automate analysis. However, computational techniques are limited by batch effects, where technical factors like differences in preparation protocol or scanners can alter the appearance of slides, causing models trained on one institution or patient to fail when generalizing to others. Here, we propose a domain adaptation method that improves the generalization of histopathological models to data from unseen institutions, without the need for labels or retraining in these new settings. Our approach introduces an optimal transport (OT) loss, that extends adversarial methods that penalize models if images from different institutions can be distinguished in their representation space. Unlike previous methods, which operate on single samples, our loss accounts for distributional differences between batches of images. We show that on the Camelyon17 dataset, while both methods can adapt to global differences in color distribution, only our OT loss can reliably classify a cancer phenotype unseen during training. Together, our results suggest that OT improves generalization on rare but critical phenotypes that may only make up a small fraction of the total tiles and variation in a slide.  ',
        video='https://youtu.be/GMYL3fUc2_o')
}}
{{ paper('High-Fidelity Image Synthesis from Pulmonary Nodule Lesion Maps using Semantic Diffusion Model',
        'Xuan Zhao, Benjamin Hou',
        openreview='https://openreview.net/forum?id=2M-2-75emE',
        pdf='https://openreview.net/pdf?id=2M-2-75emE',
        id='S050',
        paper='papers/S050',
        proceedings='',
        abstract='Lung cancer has been one of the leading causes of cancer-related deaths worldwide for years. With the emergence of deep learning, computer-assisted diagnosis (CAD) models based on learning algorithms can accelerate the nodule screening process, providing valuable assis- tance to radiologists in their daily clinical workflows. However, developing such robust and accurate models often requires large-scale and diverse medical datasets with high-quality annotations. Generating synthetic data provides a pathway for augmenting datasets at a larger scale. Therefore, in this paper, we explore the use of Semantic Diffusion Mod- els (SDM) to generate high-fidelity pulmonary CT images from segmentation maps. We utilize annotation information from the LUNA16 dataset to create paired CT images and masks, and assess the quality of the generated images using the Fr ́echet Inception Distance (FID), as well as on two common clinical downstream tasks: nodule detection and nodule localization. Achieving improvements of 3.953% for detection accuracy and 8.5% for AP50 in nodule localization task, respectively, demonstrates the feasibility of the approach.',
        video='https://youtu.be/06peLTLnmWg')
}}
{{ paper('Deep Learning Regression of Cardiac Phase on Real-Time MRI',
        'Samira Masoudi, Amin Mahmoodi, Hafsa Babar, Albert Hsiao',
        openreview='https://openreview.net/forum?id=5063TZgHfQm',
        pdf='https://openreview.net/pdf?id=5063TZgHfQm',
        id='S110',
        paper='papers/S110',
        proceedings='',
        abstract='Cine steady-state free-precession (SSFP) is the backbone of cardiac MRI, providing visualization of cardiac structure and function over the cardiac cycle, but requires concurrent ECG-gating to combine k-space data over multiple heart beats. However, cine SSFP is limited by a number of factors including arrhythmia, where beat-to-beat variability causes image artifacts. Real-time (RT) SSFP and recent innovations in image reconstruction provides a new potential alternative, capable of acquiring images without averaging over multiple heart beats. However, analysis of cardiac function from this image data can be complex, requiring retrospective analysis of function over multiple cardiac cycles and slices.  We propose a deep learning regression method to facilitate cardiac phase detection, leveraging synthetic training approach from historical cine SSFP image data, and evaluate the effectiveness of this approach for detecting cardiac phase on RT SSFP images, manually labeled by expert readers. This combined approach using RT SSFP may have multiple potential advantages over traditional cine SSFP for evaluating cardiac function in patients with arrhythmia or difficulty tolerating long breath holds.',
        video='None')
}}
{{ paper('An end-to-end Complex-valued Neural Network approach for k-space interpolation in Parallel MRI',
        'Poornima Jain, Neelam Sinha, G. Srinivasaraghavan',
        openreview='https://openreview.net/forum?id=7mwxN2h7SM',
        pdf='https://openreview.net/pdf?id=7mwxN2h7SM',
        id='S117',
        paper='papers/S117',
        proceedings='',
        abstract='Parallel MRI techniques in the k-space, like GRAPPA are widely used in accelerated MRI. Recently neural-network based non-linear approaches have shown improved performance over linear methods like GRAPPA. But present day neural networks are largely tailored to process real data, hence the complex-valued k-space data is processed as two-dimensional real data in these. In this work, we study the performance of an end-to-end complex-valued architecture trained using complex-valued optimization, for interpolating missing values in the k-space for parallel MR which we call the Complex rRAKI. We propose a generalized version of the ReLU activation function on the complex plane called the PlaneReLU. The performance of the Complex rRAKI is evaluated on two publicly-available k-space MRI datasets, the fastmri multicoil brain dataset and the fastmri multicoil knee dataset. Com- parison of obtained results with those on the baseline rRAKI are also presented. The proposed Complex rRAKI achieves improved performance over the baseline with respect to standard metrics SSIM and NRMSE with 50% fewer parameters.',
        video='https://youtu.be/2PaXyy2Bwt4')
}}
{{ paper('Spatial Correspondence between Graph Neural Network-Segmented Images',
        'Qian Li, Yunguan Fu, Qianye Yang, Zhijiang Du, Hongjian Yu, Yipeng Hu',
        openreview='https://openreview.net/forum?id=d7J0IiMqcZd',
        pdf='https://openreview.net/pdf?id=d7J0IiMqcZd',
        id='P090',
        paper='papers/P090',
        proceedings='',
        abstract='Graph neural networks (GNNs) have been proposed for medical image segmentation, by predicting anatomical structures represented by graphs of vertices and edges. One such type of graphs are predefined with fixed size and connectivity to represent a reference of anatomical regions of interest, thus known as templates. This work explores the potentials in these GNNs with common topology for establishing spatial correspondence, implicitly maintained during segmenting two or more images. With an example application of registering local vertebral sub-regions found in CT images, our experimental results showed that the GNN-based segmentation is capable of accurate and reliable localisation of the same interventionally interesting structures between images, not limited to the segmentation classes. The reported average target registration errors of 2.2$\\pm$1.3 mm and 2.7$\\pm$1.4 mm, for aligning holdout test images with a reference and for aligning two test images, respectively, were by a considerable margin lower than those from the tested non-learning and learning-based registration algorithms. Further ablation studies assess the contributions towards the registration performance, from individual components in the originally segmentation-purposed network and its training algorithm. The results highlight that the proposed segmentation-in-lieu-of-registration approach shares methodological similarity with existing registration methods, such as the use of displacement smoothness constraint and point distance minimisation albeit on non-grid graphs, which interestingly yielded benefits for both segmentation and registration. We therefore conclude that the template-based GNN segmentation can effectively establish spatial correspondence in our application, without any other dedicated registration algorithms.',
        video='https://youtu.be/Sh0d9CWp9dE')
}}
{{ paper('3D Supervised Contrastive-Learning Network for Classification of Ovarian Neoplasms',
        'Tarun Kanti Roy, Suely Oliveira, Jesus Gonzalez Bosquet, Xiaodong Wu',
        openreview='https://openreview.net/forum?id=BC4UYzbLRZ',
        pdf='https://openreview.net/pdf?id=BC4UYzbLRZ',
        id='S073',
        paper='papers/S073',
        proceedings='',
        abstract="Ovarian cancer ranks the $5^{th}$ in cancer deaths among women, accounting for more deaths than any other cancer of the female reproductive system.  We propose a 3D contrastive learning based predictive model to discriminate benign from malignant masses in abdominal CT scans for ovarian cancer patients. We used fully supervised contrastive learning(SCL) approach which allowed us to effectively leverage the label information of our small dataset of 331 patients. All patients\\' data was collected at the University of Iowa. Three different architectures (VGG, ResNet and DenseNet) were implemented for  feature extraction by contrastive learning. We showed that SCL consistently out-performed over the traditional cross-entropy based networks with VGG and two ResNet variants. With five fold cross validation, our best contrastive learning model achieves an accuracy of 92.8\\%, mean AUC of 92.4\\%, mean recall of 94.45\\% and mean specificity of 90.37\\%.  This work shows that contrastive learning is a promising deep learning method to improve early detection of women at risk of harboring ovarian cancer.",
        video='None')
}}
{{ paper('Characterizing Continual Learning Scenarios for Tumor Classification in Histopathology Images',
        'Veena Kaustaban, Qinle Ba, Ipshita Bhattacharya, Nahil Sobh, Satarupa Mukherjee, Jim Martin, Mohammad Saleh Miri, Christoph Guetter, Amal Chaturvedi',
        openreview='https://openreview.net/forum?id=e6B-OAcJfuD',
        pdf='https://openreview.net/pdf?id=e6B-OAcJfuD',
        id='S093',
        paper='papers/S093',
        proceedings='',
        abstract='Deep-learning models have achieved unprecedented performance in fundamental computational tasks in digital pathology (DP) based analysis, such as image classification, cell detection and tissue segmentation. However, such models are known to suffer from catastrophic forgetting when adapted to unseen data distribution with transfer learning. With an increasing need for deep-learning models to handle ever-changing data distributions, including evolving patient population and new diagnosis assays, it is crucial to introduce methods for alleviating the such model forgetting. To this end, continual learning (CL) models are promising candidates. However, to our best knowledge, there’s no systematic study of CL models in DP-specific applications. Here, we propose various CL scenarios in DP settings, where histopathology image data from different sources/distributions arrive sequentially, the knowledge of which is integrated into a single model without training all the data from scratch. To benchmark the performance of recently proposed continual learning algorithms in the proposed CL scenarios, We augmented a dataset for colorectal cancer H&E classification to simulate shifts of image appearance and evaluated CL methods on this dataset. Furthermore, we leveraged a breast cancer H&E dataset along with the colorectal cancer dataset to assess continual learning methods for learning from multiple tumor types. We revealed promising results of CL in DP applications, potentially paving the way for application of these methods in clinical practice.',
        video='None')
}}
{{ paper('MProtoNet: A Case-Based Interpretable Model for Brain Tumor Classification with 3D Multi-parametric Magnetic Resonance Imaging',
        'Yuanyuan Wei, Roger Tam, Xiaoying Tang',
        openreview='https://openreview.net/forum?id=6Wbj3QCo4U4',
        pdf='https://openreview.net/pdf?id=6Wbj3QCo4U4',
        id='P218',
        paper='papers/P218',
        proceedings='',
        abstract='Recent applications of deep convolutional neural networks in medical imaging raise concerns about their interpretability. While most explainable deep learning applications use post hoc methods (such as GradCAM) to generate feature attribution maps, there is a new type of case-based reasoning models, namely ProtoPNet and its variants, which identify prototypes during training and compare input image patches with those prototypes. We propose the first medical prototype network (MProtoNet) to extend ProtoPNet to brain tumor classification with 3D multi-parametric magnetic resonance imaging (mpMRI) data. To address different requirements between 2D natural images and 3D mpMRIs especially in terms of localizing attention regions, a new attention module with soft masking and online-CAM loss is introduced. Soft masking helps sharpen attention maps, while online-CAM loss directly utilizes image-level labels when training the attention module. MProtoNet achieves statistically significant improvements in interpretability metrics of both correctness and localization coherence (with a best activation precision of $0.713\\pm0.058$) without human-annotated labels during training, when compared with GradCAM and several ProtoPNet variants. The source code is available at https://github.com/aywi/mprotonet.',
        video='None')
}}
{{ paper('MEDIMP: 3D Medical Images and clinical Prompts for renal transplant representation learning',
        'Leo Milecki, Vicky Kalogeiton, Sylvain Bodard, Dany Anglicheau, Jean-Michel Correas, Marc-Olivier Timsit, Maria Vakalopoulou',
        openreview='https://openreview.net/forum?id=jt-ochRhqG',
        pdf='https://openreview.net/pdf?id=jt-ochRhqG',
        id='P055',
        paper='papers/P055',
        proceedings='',
        abstract='Renal transplantation emerges as the most effective solution for end-stage renal disease. Occurring from complex causes, a substantial risk of transplant chronic dysfunction persists and may lead to graft loss. Medical imaging plays a substantial role in renal transplant monitoring in clinical practice. However, graft supervision is multi-disciplinary, notably joining nephrology, urology, and radiology, while identifying robust biomarkers from such high-dimensional and complex data for prognosis is challenging. In this work, taking inspiration from the recent success of Large Language Models (LLMs), we propose MEDIMP -- Medical Images and clinical Prompts -- a model to learn meaningful multi-modal representations of renal transplant Dynamic Contrast-Enhanced Magnetic Resonance Imaging (DCE MRI) by incorporating structural clinicobiological data after translating them into text prompts. MEDIMP is based on contrastive learning from joint text-image paired embeddings to perform this challenging task. Moreover, we propose a framework that generates medical prompts using automatic textual data augmentations from LLMs. Our goal is to learn meaningful manifolds of renal transplant DCE MRI, interesting for the prognosis of the transplant or patient status (2, 3, and 4 years after the transplant), fully exploiting the limited available multi-modal data most efficiently. Extensive experiments and comparisons with other renal transplant representation learning methods with limited data prove the effectiveness of MEDIMP in a relevant clinical setting, giving new directions toward medical prompts. Our code is available at https://github.com/leomlck/MEDIMP.',
        video='None')
}}
{{ paper('Bi-parametric prostate MR image synthesis using pathology and sequence-conditioned stable diffusion',
        'Shaheer U. Saeed, Tom Syer, Wen Yan, Qianye Yang, Mark Emberton, Shonit Punwani, Matthew John Clarkson, Dean Barratt, Yipeng Hu',
        openreview='https://openreview.net/forum?id=3QnxUSzR7iu',
        pdf='https://openreview.net/pdf?id=3QnxUSzR7iu',
        id='O053',
        paper='papers/O053',
        proceedings='',
        abstract='We propose an image synthesis mechanism for multi-sequence prostate MR images conditioned on text, to control lesion presence and sequence, as well as to generate paired bi-parametric images conditioned on images e.g. for generating diffusion-weighted MR from T2-weighted MR for paired data, which are two challenging tasks in pathological image synthesis. Our proposed mechanism utilises and builds upon the recent stable diffusion model by proposing image-based conditioning for paired data generation. We validate our method using 2D image slices from real suspected prostate cancer patients. The realism of the synthesised images is validated by means of a blind expert evaluation for identifying real versus fake images, where a radiologist with 4 years experience reading urological MR only achieves 59.4\\% accuracy across all tested sequences (where chance is 50\\%). For the first time, we evaluate the realism of the generated pathology by blind expert identification of the presence of suspected lesions, where we find that the clinician performs similarly for both real and synthesised images, with a 2.9 percentage point difference in lesion identification accuracy between real and synthesised images, demonstrating the potentials in radiological training purposes. Furthermore, we also show that a machine learning model, trained for lesion identification, shows better performance (76.2\\% vs 70.4\\%, statistically significant improvement) when trained with real data augmented by synthesised data as opposed to training with only real images, demonstrating usefulness for model training.',
        video='None')
}}
{{ paper('Whole brain radiomics for clustered federated personalization in brain tumor segmentation',
        'Matthis Manthe, Stefan Duffner, Carole Lartizien',
        openreview='https://openreview.net/forum?id=1CyXExO15K',
        pdf='https://openreview.net/pdf?id=1CyXExO15K',
        id='P075',
        paper='papers/P075',
        proceedings='',
        abstract='Federated learning and its application to medical image segmentation have recently become a popular research topic. This training paradigm suffers from statistical heterogeneity between participating institutions’ local datasets, incurring convergence slowdown as well as potential accuracy loss compared to classical training.  To mitigate this effect, federated personalization emerged as the federated optimization of one model per distribution. We propose a novel personalization algorithm tailored to the feature shift induced by the usage of different scanners and acquisition parameters by different institutions. This method is the first to account for both inter and intra-institution feature shifts (multiple scanners used in a single institution). It is based on the computation, within each centre, of a series of radiomic features capturing the global texture of each 3D image volume, followed by a clustering analysis pooling all feature vectors transferred from the local institutions to the central server. Each computed clustered decentralized dataset (potentially including data from different institutions) then serves to finetune a global model obtained through classical federated learning. We validate our approach on the Federated Brain Tumor Segmentation 2022 Challenge dataset (FeTS2022).',
        video='None')
}}
{{ paper('One-Class SVM on siamese neural network latent space for Unsupervised Anomaly Detection on brain MRI White Matter Hyperintensities',
        'Nicolas Pinon, Robin Trombetta, Carole Lartizien',
        openreview='https://openreview.net/forum?id=_c9r6-HCEaN',
        pdf='https://openreview.net/pdf?id=_c9r6-HCEaN',
        id='P217',
        paper='papers/P217',
        proceedings='',
        abstract='Anomaly detection remains a challenging task in neuroimaging when little to no supervision is available and when lesions can be very small or with subtle contrast. Patch-based representation learning has shown powerful representation capacities when applied to industrial or medical imaging and outlier detection methods have been applied successfully to these images. In this work, we propose an unsupervised anomaly detection (UAD) method based on a latent space constructed by a siamese patch-based auto-encoder and perform the outlier detection with a One-Class SVM training paradigm tailored to the lesion detection task in multi-modality neuroimaging. We evaluate performances of this model on a public database, the White Matter Hyperintensities (WMH) challenge and show in par performance with the two best performing state-of-the-art methods reported so far. ',
        video='None')
}}
[% / %]