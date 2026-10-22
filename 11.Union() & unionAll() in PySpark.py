# Databricks notebook source
data1 = [(1, 'maheer', 'M', 2000, 'IT'), (2, 'wafa', 'M', 4000, 'HR')]
schema1 = ['id', 'name', 'gender', 'salary', 'dep']

data2 = [(1, 'maheer', 'M', 2000, 'IT'),(3, 'asi', 'F', 3000, 'Payroll'), (4, 'sarfaraj','M',3000, 'HR')]
schema2 = ['id', 'name', 'gender', 'salary', 'dep']

df1 = spark.createDataFrame(data1, schema1)
df2 = spark.createDataFrame(data2, schema2)
print('Data Frame:- 1')
df1.show()
print('Data Frame:- 2')
df2.show()

# COMMAND ----------

# DBTITLE 1,Union
newDF = df1.union(df2)  # Doesn't remove duplicates
newDF.show()

# COMMAND ----------

# DBTITLE 1,UnionALL
newDF1 = df1.unionAll(df2)  # Doesn't remove duplicates
newDF1.show()

# COMMAND ----------

# DBTITLE 1,Remove duplicates
 df1.unionAll(df2).distinct().show()

# COMMAND ----------

