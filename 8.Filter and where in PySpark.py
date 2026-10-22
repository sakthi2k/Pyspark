# Databricks notebook source
data = [(1,'maheer','male', 2000),(2,'wafa', 'male', 4000),(3,'Asi','Female', 3000)]
schema =['id','name','gender','salary']
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

df.filter(df.gender =='male').show()

# COMMAND ----------

df.filter("gender == 'male'").show()

# COMMAND ----------

df.where((df.gender =='male') & (df.salary == 2000)).show()

# COMMAND ----------

