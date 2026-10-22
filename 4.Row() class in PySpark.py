# Databricks notebook source
# DBTITLE 1,Accessing using Index
from pyspark.sql import Row
row = Row('Sakthi',1000) # it's similar to tuple in python
print(row[0])
print(row[1])


# COMMAND ----------

# DBTITLE 1,Accessing using Named Argument
row = Row(name ='Siva', Salary = '2000')
print(row.name + ' '+row.Salary)

# COMMAND ----------

row1 = Row(name='Sakthi',Salary='1000') # it's similar to tuple in python
row2 = Row(name ='Siva', Salary = '2000')
data = [row1, row2]
df = spark.createDataFrame(data)
display(df)

# COMMAND ----------

# DBTITLE 1,Create Row like a Class
Person = Row('name','Age')
p1 = Person('Abcd',23)
p2 = Person('High',25)
print('Calling a class')
print(p1.name +'   ' +p2.name)
data=[p1,p2]
df = spark.createDataFrame(data)
print("After creating Data frame")
df.show()

# COMMAND ----------

# DBTITLE 1,Create Row with nested StructField
data =[
      Row(name ='abc', prop = Row(age =23, gender = 'Male')), \
      Row(name ='cde', prop = Row(age =24, gender = 'Female'))]
df = spark.createDataFrame(data)
df.show()
df.printSchema()

# COMMAND ----------

