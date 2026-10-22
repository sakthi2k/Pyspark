# Databricks notebook source
from pyspark.sql.functions import when
data = [(1,'maheer','M',2000),(2,'roja','F',3000),(3,'abcd','',3000)]
schema = ['id','name','gender','salary']
df = spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

# DBTITLE 1,When () && Otherwise()
from pyspark.sql.functions import when
df1 = df.select(df.id,df.name,\
       when(df.gender == 'M','Male')\
       .when(df.gender =='F','Female')\
       .otherwise('Unknown').alias('gender') 
           )
df1.display()

# COMMAND ----------



