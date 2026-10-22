# Databricks notebook source
data =[(1,'fcd', 2000),(2, 'abc', 4000),(3, 'aeiou', 4000),(3, 'adef', 4000)]
schema = ['id','name','salary']
df = spark.createDataFrame(data, schema)
df.show()
df.printSchema()

# COMMAND ----------

# DBTITLE 1,Alias_Namae
df.select(df.id.alias('Emp_ID'),\
          df.name.alias('Emp_Name'),\
          df.salary.alias('Emp_Salary')\
          ).show()

# COMMAND ----------

# DBTITLE 1,ASC && DESC
print("Ascending Order")
df.sort(df.name.asc()).show()
print("Descending Order")
df.sort(df.name.desc()).show()

# COMMAND ----------

# DBTITLE 1,Cast function
#Converting long data type to int data type
df.printSchema()  # Actual Schema 
df1 = df.select(df.id,df.name,df.salary.cast('int')) # converting to int
df1.printSchema()

# COMMAND ----------

# DBTITLE 1,Like
df.filter(df.name.like('a%')).show()

# COMMAND ----------

