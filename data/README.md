# Data inputs

Download the datasets from their original publishers, then use the paths below. The raw files are not redistributed in this repository.

| Part | Source | Destination |
| :--- | :--- | :--- |
| Segmentation | [Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis) | `data/rfm/marketing_campaign.csv` |
| Churn | [Ecommerce Customer Churn Analysis and Prediction](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction) | `data/churn/data.xlsx` |
| Customer value | [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) | the nine CSV files in `data/olist/` |

For churn, rename the downloaded Excel workbook to `data.xlsx`; the notebook reads its `E Comm` sheet. The segmentation loader accepts tab- and semicolon-delimited exports. The Olist filenames must remain unchanged.

`manifest.json` records the sizes and SHA-256 checksums of the exact local inputs used for the course results. A mismatch can indicate a different dataset version or just a different export format; inspect it before comparing results. Dataset licenses and attribution requirements are those supplied by the respective publishers.

From the repository root, check the inputs with:

```bash
mamba run -n ai4cm-env python scripts/check_data.py
```
