# Databricks notebook source
data1=[(1,'Abcd',2000,2),
       (2,'Cdef',3000,1),
       (3,'Efghi',1000,4)]
schema1=["ID","Name","Salary","Department"]

data2=[(1,'IT'),(2,'HR'),(3,'Payroll')]
schema2=['ID',"Name"]
empDf=spark.createDataFrame(data1,schema1)
depDf=spark.createDataFrame(data2,schema2)
display(empDf)
display(depDf)

# COMMAND ----------

help(empDf.join)

# COMMAND ----------

# DBTITLE 1,INNER JOIN
#Inner Join
Inner_Join=empDf.join(depDf,empDf.Department == depDf.ID,'inner')
display(Inner_Join)

# COMMAND ----------

# DBTITLE 1,LEFT JOIN
#Left Join
left_Join=empDf.join(depDf,empDf.Department == depDf.ID,'left')
display(left_Join)

# COMMAND ----------

# DBTITLE 1,RIGHT JOIN
#Right Join
Right_Join=empDf.join(depDf,empDf.Department == depDf.ID,'right')
display(Right_Join)

# COMMAND ----------

# DBTITLE 1,FULL JOIN
#Full Join
Full_Join=empDf.join(depDf,empDf.Department == depDf.ID,'full')
display(Full_Join)

# COMMAND ----------

# DBTITLE 1,LEFT SEMI JOIN
print("Matching columns from the Left table from Emp table we have only department colun matched with right table")
display(empDf.join(depDf, empDf.Department == depDf.ID, 'leftsemi'))

# COMMAND ----------

# DBTITLE 1,LEFT ANTI JOIN
print(" Left Anti will retuen Non matching row from right table")
display(empDf.join(depDf, empDf.Department == depDf.ID, 'leftanti'))

# COMMAND ----------

# DBTITLE 1,Self Join
data =[(1,'sakthi',0),(2,'Siva',1),(3,'Surya',2)]
schema=['id','name','ManagerId']
df=spark.createDataFrame(data,schema)
display(df)

# COMMAND ----------

from pyspark.sql.functions import col
df.alias('EmpData').join(df.alias('MgrData'),\
    col('EmpData.ManagerId') == col('MgrData.id')\
    ,'left').show()