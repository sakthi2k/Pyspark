# Databricks notebook source
df=spark.range(1,5+1)
df.show()
#date default format  yyyy-mm-dd

from pyspark.sql.functions import current_date,date_format, lit, to_date
df1=df.withColumn('CurrentDate', current_date());
df1.show()

# COMMAND ----------

# DBTITLE 1,Date Format
# Convert the date format
df2=df1.withColumn('CurrentDate', date_format(df1.CurrentDate, 'dd-MM-yyyy'))
df2.show()
df2.printSchema()

# COMMAND ----------

# DBTITLE 1,To Date
df3=df2.withColumn('CurrentDate', to_date(df2.CurrentDate,'dd-MM-yyyy'))
df3.show()

# COMMAND ----------

# DBTITLE 1,Date Diff()
from pyspark.sql.functions import datediff, months_between, add_months,date_add, year, month
date_fun=spark.createDataFrame([('2026-02-14','2026-03-14')],['d1','d2'])
date_fun.show()



# COMMAND ----------

# DBTITLE 1,Date_Diff
print("Date Difference")
date_fun.withColumn('Date_Diff', datediff(date_fun.d2,date_fun.d1)).show()



# COMMAND ----------

# DBTITLE 1,Months_Between
print('Months between')
date_fun.withColumn('Months_Between', months_between(date_fun.d2,date_fun.d1)).show()



# COMMAND ----------

# DBTITLE 1,Add Months
print("Add_months")
date_fun.withColumn('Add_Months',add_months(date_fun.d2, 3)).show()

# COMMAND ----------

# DBTITLE 1,Subract Months
print("Sub_months")
date_fun.withColumn('Sub_Months',add_months(date_fun.d2, -3)).show()

# COMMAND ----------

# DBTITLE 1,Date_Add
print("Date_Add")
date_fun.withColumn('Date_Add',date_add(date_fun.d2, 3)).show()

# COMMAND ----------

# DBTITLE 1,Year And Month
date_fun.withColumn('Year',year(date_fun.d2)).show()
date_fun.withColumn('Month',month(date_fun.d2)).show()

# COMMAND ----------

# DBTITLE 1,Month
