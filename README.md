# Predicting the demand of a bakery

Overview
---
Project overview


Project structure
---

```
├── README.md                     <- The top-level README for developers using this project.
│
├── data
│   ├── 01_raw                    <- Imutable input data
│   ├── 02_intermediate           <- Cleaned version of raw
│   ├── 03_processed              <- The data used for modelling
│   ├── 04_models                 <- trained models
│   ├── 05_model_output           <- model output
│   └── 06_reporting              <- Reports and input to frontend
│
├── docs                          <- tfm thesis, presentations & user manuals
│
├── notebooks                     <- Jupyter notebooks. .
│
├── requirements.txt              <- The requirements file for reproducing the analysis environment, `pip freeze > requirements.txt`
│
│
└── src                           <- Source code for use in this project.
    │
    ├── d00_utils                 <- Functions used across the project
    │
    ├── d01_intermediate          <- Scripts to transform data from raw to intermediate
    │
    ├── d02_processing            <- Scripts to turn intermediate data into modelling input
    │
    ├── d03_modelling_evaluation  <- Scripts to train models and then use trained models to make
    │                                predictions
    │
    ├── d04_model_evaluation      <- Scripts that analyse model performance and model selection
    │    
    ├── d05_reporting             <- Scripts to produce reporting tables
    │
    └── d06_visualisation         <- Scripts to create frequently used plots
    │
    │   d06_test                  <- Scripts for testing

 *https://bit.ly/2Vq4VwA
```
Naming conventions
---
Naming convention is date YYYYMMDD (for ordering),`-` description, e.g.`190601-initial-data-exploration`.

Collaborators
---

 - Illán Lois Bermejo
 - Miguel Ruiz Nogues

