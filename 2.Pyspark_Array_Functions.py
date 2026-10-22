# Databricks notebook source
# DBTITLE 1,Explode()_Function
from pyspark.sql.functions import explode,col
data = [ (1,'Sakthi',['java','aws']),(2,'Kumar',['Python','axure']) ]
schema = ['ID','Name','Skills']
df=spark.createDataFrame(data,schema)
print("Before Explode Function")
df.show()
df1 = df.withColumn('Skil',explode(col('Skills')))
print("After Explode Function")
display(df1)

# COMMAND ----------

# DBTITLE 1,split()
from pyspark.sql.functions import split,col
data = [ (1,'Sakthi','java,aws'),(2,'Kumar','Python,azure') ]
schema = ['ID','Name','Skills']
df=spark.createDataFrame(data,schema)
print("Before Split Function")
df.show()

print("After Split Function")
df1 = df.withColumn('Split Array', split(col('Skills'), ','))
display(df1)

# COMMAND ----------

# DBTITLE 1,Array
from pyspark.sql.functions import array,col
data = [ (1,'Sakthi','java','aws'),(2,'Kumar','Python','azure') ]
schema = ['ID','Name','Primary Skills', "Secondary Skill"]
df=spark.createDataFrame(data,schema)
print("Before Array Function")
df.show()

df1 = df.withColumn('Array_Column',array(col('Primary Skills'),col("Secondary Skill")))
print("After Array Function")
display(df1)


# COMMAND ----------

# DBTITLE 1,Array_contains
from pyspark.sql.functions import array_contains,col
data = [ (1,'Sakthi',['java','aws']),(2,'Kumar',['Python','azure']) ]
schema = ['ID','Name',"Skill"]
df=spark.createDataFrame(data,schema)
print("Before Array Contains Function")
df.show()

print("After Array Contains Function")
df1 = df.withColumn("Data_check_Using_Array_Contains", array_contains(col('Skill'),'java'))
display(df1)


# COMMAND ----------

