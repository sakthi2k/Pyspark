# Databricks notebook source
data=[(1,'Abcd',2000,200),
       (2,'Cdef',3000,100),
       (3,'Efghi',1000,400)]
schema=["ID","Name","Salary","bonus"]
df= spark.createDataFrame(data,schema)
df.show()

# COMMAND ----------

# DBTITLE 1,UDF
def totalPay(s,b):
    return s+b
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
# Register the UDF functions
TotalPayment = udf(lambda s,b:totalPay(s,b),IntegerType())


# COMMAND ----------

df.withColumn("TotalPay", TotalPayment(df.Salary,df.bonus)).show()


# COMMAND ----------

# Another way Register our UDF function using UDF
@udf(returnType =IntegerType())
def totalPay1(s,b):
    return s+b


# COMMAND ----------

df.select('*',totalPay1(df.Salary,df.bonus).alias('TotalPay')).show()

# COMMAND ----------

df.createOrReplaceTempView("Emp")

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from Emp

# COMMAND ----------

# To use UDF in the SQL query use the following
spark.udf.register(name='TotalPaySQL', f=totalPay, returnType=IntegerType())


# COMMAND ----------

# MAGIC %sql
# MAGIC select id, name, TotalPaySQL(Salary,bonus)as tot from emp;

# COMMAND ----------

