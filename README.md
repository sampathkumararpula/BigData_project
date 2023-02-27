# BigData_project 
**# COVID-19 Tweets Analysis**


**Project Goal:**

The goal of this project is to download tweets from Twitter and extract only hashtags and urls from the tweets and perform a wordcount on Hadoop and Apache Spark. This implementation is only the phase one of the project. 

**Major Components**

The project is implemented after installing and configuring Hadoop(version- 22.04) and Spark(version- 2.2.0)

**Environment**

Ubuntu 22.04

Hadoop 2.8.2

Spark 2.2.0

Python 

**Implementation**

The  tweets out.json file is extracted using python. The program to extract the "urls" and "hastags" is in the file "Bigdata.py"


**Execution in Hadoop**


We ran wordcount on the extracted "urls" and "hashtags" on hadoop using the  command 
$ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.1.jar wordcount /ska/input.txt /ska/hadoopoutput. we got two files Success file and the output file, the same is uploaded in the repository as "part-r-00000"


**Execution in  Spark**

we  ran wordcount on the extracted "urls" and "hashtags" on Spar using the  command and saved in the file Spark_output.txt 
 *$SPARK_HOME/bin/spark-submit run-example JavaWordCount /home/sampath/hadoop-2.8.1/input.txt > Spark_output.txt*
The file is uploaded in repository as "Spark_output.txt"

 **Log Files**

 Log files which are generated after executing worcount on Hadoop and spark are uploaded in repository as "Log_Files" and "Spark_logfile"
 
 **Conclusion**
We were able to successfully run wordcount on extracted hastags and urls on hadoop and spark and the output files for the same has been uploaded. 

**Future Scope**

We may develop interesting analytics use cases to explore and Use Spark SQL queries or machine learning tasks. We may even perform setiment analsysis of Twitter data.





NOTE: Please note that, out.json file we were unable to upload.

