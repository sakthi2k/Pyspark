# Databricks notebook source
# DBTITLE 1,orderBy() & sort()
#  Definition:-
'''
--> Sort the dataframe in ascending or descending order based on single or 
multiple columns.
-->By default , sorting will happen in ascending order. we can explicity
metion asc or desc using asc(), desc()  functions

'''

# COMMAND ----------

data = [(1, 'maheer', 'M', 2000, 'IT'), (2, 'wafa', 'M', 4000, 'HR'),
        (3, 'asi', 'F', 3000, 'Payroll'), (4, 'sarfaraj','M',3000, 'HR')]

schema = ['id', 'name', 'gender', 'salary', 'dep']
df = spark.createDataFrame(data, schema)
df.show()

# COMMAND ----------

# DBTITLE 1,Sort
# default is Ascending order
df.sort(df.dep,df.id)show()

# COMMAND ----------

# DBTITLE 1,OrderBy
df.orderBy("dep").show()

# COMMAND ----------

# DBTITLE 1,Sort by column wise
df.sort(df.dep,df.id.desc()).show()

# COMMAND ----------

# DBTITLE 1,Order by column wise
df.orderBy(df.dep.desc(),df.id.desc()).show()

# COMMAND ----------

