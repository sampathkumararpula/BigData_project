# BigData_project
# COVID-19 Tweets Analysis
Project Goal:
The goal of this project is to extract tweets from Twitter and extract only hashtags and urls from the tweets and perform a wordcount on Hadoop and Apache Spark.
Major Components
The project is implemented after installing and configuring Hadoop(version- 22.04) and Spark(version- )
Environment
Ubuntu22.04](https://ubuntu.com/download/desktop)
[Hadoop 2.8.1] (https://archive.apache.org/dist/hadoop/core/hadoop-2.8.1/hadoop- 2.8.1.tar.gz)
[Spark 2.2.0] (https://archive.apache.org/dist/spark/spark-2.2.0/spark-2.2.0-bin- hadoop2.7.tgz)
[Java] (https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)
Implementation
The extracted tweets json file is extracted using python. The program to extract the “urls” and “hastags” is in the file “Bigdata.py”.
Execution in Hadoop
I have ran wordcount on the extracted “urls” and “hashtags” on hadoop using the command
$ bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.1.jar wordcount /ska/input.txt /ska/hadoopoutput
After I run this file I got two files Success file and the output file, the same is uploaded in the repository as “part-r-00000”
Execution in Spark
I have ran wordcount on the extracted “urls” and “hashtags” on Spar using the command and saved in the file Spark_output.txt
$SPARK_HOME/bin/spark-submit run-example JavaWordCount /home/sampath/hadoop-2.8.1/input.txt > Spark_output.txt
The file is uploaded in repository as “Spark_output.txt”
Log Files
Log files which are generated after executing worcount on Hadoop and spark are uploaded in repository as “Log_Files” and “Spark_logfile”
Conclusion
We were able to successfully run wordcount on extracted hastags and urls on hadoop and spark and the output files for the same has been uploaded.

Contributors:

Rama Pavan Naga Sai Santhosh Katragadda- KRPNSS(github)
