# Databricks notebook source
from pyspark.sql.functions import lit
 #lit function is used to create a column

data =[('maheer','male', 2000),('wafa', 'male', 4000)]
schema = ['name','gender','salary']
df = spark.createDataFrame(data, schema)
display(df)

# COMMAND ----------

from pyspark.sql.functions import lit
 #lit function is used to create a column
df1= df.withColumn('newCol', lit('newColVal'))
df1.show()
df1.printSchema()

# COMMAND ----------

# DBTITLE 1,Accessing Column in different ways]
from pyspark.sql.functions import col
df.select(df.gender).show()

df.select(df['name']).show()   # Accessing through  dataframe

df.select(col('salary')).show()   # Using col function

# COMMAND ----------


from pyspark.sql.types import StructField, StructType, IntegerType, StringType
from pyspark.sql.functions import col

data =[('maheer','male', 2000,('black','brown')),('wafa', 'male', 4000,('black','blue'))]
propesType =StructType([
    StructField('hair',StringType()),\
        StructField('eye',StringType()) \
])
schema = StructType([
    StructField('name',StringType()), \
    StructField('gender',StringType()), \
    StructField('salary',IntegerType()), \
    StructField('props', propesType)
])
df = spark.createDataFrame(data, schema)
df.show()

# COMMAND ----------

df.select(df.name).show()

# COMMAND ----------

df.select(df['props.eye']).show()

# COMMAND ----------

df.select(col('props.hair')).show()

# COMMAND ----------

