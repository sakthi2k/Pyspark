# Databricks notebook source
data = [
    (1, "Arjun", 2000),
    (2, "Priya", 3000)
]
schema =['id','name','salary']
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

from pyspark.sql.functions import upper
df.withColumn('name', upper('name')).show()

# COMMAND ----------

def convertNameToUpper(df):
    return df.withColumn('name', upper(df.name))
def doubeTheSalary(df):
    return df.withColumn('salary', df.salary *2);


# COMMAND ----------

df1=df.transform(convertNameToUpper)
display(df1)
df2=df1.transform(doubeTheSalary)
display(df2)

# COMMAND ----------

df1=df.transform(convertNameToUpper)\
    .transform(doubeTheSalary)
display(df1)

# COMMAND ----------

# DBTITLE 1,Transform function from Pyspark
data1 = [(1,'Arjun',['Azure','Python']),(2,'Karthik',['AWS',"Java"])]
schema1 = ['id','name','skills']
df2 = spark.createDataFrame(data1,schema1)
df2.show()
df2.printSchema()

# COMMAND ----------

from pyspark.sql.functions import transform, upper
df2.select('id','name', transform('skills', lambda x: upper(x)).alias('Skills')).show()

def convertToUpper(x):
    return upper(x)
df2.select('id','name',transform('skills', convertToUpper).alias('skills')).show()

# COMMAND ----------

