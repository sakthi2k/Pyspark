# Databricks notebook source
data1 = [(1, 'maheer',27 ), (2, 'wafa', 23)]
schema1 = ['id', 'name','age']

data2 = [(1, 'maheer',  2000)]
schema2 = ['id', 'name', 'salary']
print('Data Frame:-1')
df1 = spark.createDataFrame(data1, schema1).show()
print('Data Frame:-2')
df2 = spark.createDataFrame(data2, schema2).show()

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# DBTITLE 1,unionByName
df1.unionByName(df2,allowMissingColumns= True).show()

# COMMAND ----------

