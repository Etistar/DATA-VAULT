#!/usr/bin/env python
# coding: utf-8

# ## test
# 
# New notebook

# In[5]:


# tests/test_kpi.py


df = spark.read.format("delta").load(
    "abfss://97b806a1-b504-4924-8b5f-98f028f65fc7@onelake.dfs.fabric.microsoft.com/8b942a7a-1624-4133-90cc-e842c3e7d468/Tables/fact_sales_prom"
)


# In[8]:


from pyspark.sql.functions import col

# Vérifier que 'total_sales' et 'store_id' ne contiennent pas de nulls
assert df.filter(col("total_sales").isNull()).count() == 0
assert df.filter(col("store_id").isNull()).count() == 0

# Vérifier que toutes les valeurs de ROI sont >= 0
assert df.filter(col("ROI") < 0).count() == 0

