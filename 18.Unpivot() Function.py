# Databricks notebook source
# DBTITLE 1,Cell 1
data =[('IT',8,5),
    ('Payrole',3,4),
     ('Hr',2 ,4) ]
schema =['dep','male','female']
df = spark.createDataFrame(data,schema)
display(df)

from pyspark.sql.functions import expr
unpivot_df=df.select('dep', expr("stack(2, 'M', male, 'F', female) as (gender, count)"))
unpivot_df.show()

# COMMAND ----------

