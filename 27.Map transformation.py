# Databricks notebook source
# DBTITLE 1,Cell 1
data=[('Abcd',"Efgh"),("Ijkl","Mnop")]
df = spark.createDataFrame(data, ["col1", "col2"])
display(df)
rdd=df.rdd.map(lambda x:x+(x[0]+' '+x[1]))
df1=rdd.toDF(['firstname','lastname','full name'])
df1.show();


# COMMAND ----------

