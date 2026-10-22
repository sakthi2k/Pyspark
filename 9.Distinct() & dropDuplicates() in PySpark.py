# Databricks notebook source
data = [(1,'maheer','male', 2000),(2,'wafa', 'male', 4000),
        (2,'wafa', 'male', 4000),(3,'Asi','female', 3000)]
schema =['id','name','gender','salary']
df=spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

# DBTITLE 1,Distinct function
# distinct will be applied all columns
#If we want apply column leve we have to go for drop duplicates functions
df.distinct().show()

# COMMAND ----------

# DBTITLE 1,Drop Duplicates Functions
# we can pass the columns which we want to see the distinct values
df.dropDuplicates(['gender','id']).show()

# COMMAND ----------

