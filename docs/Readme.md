
# Description des colonnes de notre dataframe 


```text

Sales Revenue (USD): Total revenue generated from sales.
Units Sold: Quantity of items sold.
Discount Percentage: The percentage discount applied to products.
Marketing Spend (USD): Budget allocated to marketing efforts.
Store ID: Identifier for the retail store.
Product Category: The category to which the product belongs (e.g., Electronics, Clothing).
Date: The date when the sale occurred.
Store Location: Geographic location of the store.
Day of the Week: Day when the sale took place.
Holiday Effect: Indicator of whether the sale happened during a holiday period



| Colonne           | Type      | Description              |
| ----------------- | --------- | ------------------------ |
| `date`            | date      | Date de vente            |
| `product_id`      | string    | ID produit               |
| `region`          | string    | Zone géographique        |
| `units_sold`      | int       | Quantité vendue          |
| `sales_revenue`   | float     | CA généré                |
| `promo_pct`       | float (%) | Pourcentage de promotion |
| `marketing_spend` | float     | Budget marketing investi |
| `holiday_flag`    | bool      | Jour férié ou pas        |

```

# Aborescence du projet 


```text
retail-promo-bi/
│
├── end_to_end_lakehouse/
|   ├── Table
│   ├── hub_product     /       <- Hub produit avec hash product_id
│   ├── hub_store       /       <- Hub store avec hash store_id
│   └── hub_date        /       <- Hub date avec hash date
│   ├── fact_sale_prom  /       <- Table de faits permettant de faire du Power BI
│   ├── link_sale       /       <- Link sale avec hash des différents hubs
│   └── sat_sale        /       <- Données descriptives des transactions
│
|   ├── File
│   ├── Retail_sales.csv/       <- Fichiers bruts (CSV)
|
├── notebooks/
│   ├── 01_Bronze.ipynb
│   ├── 02_Silver.ipynb
│   ├── 03_Gold.ipynb
│
├── docs/
│   ├── README.md
│   ├── specs_fonctionnelles.md
│   └── schema_data_vault.drawio
│
├── requirements.txt
└── tests/
```
