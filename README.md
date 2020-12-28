# CSE503S Performance Evaluation Study

This repository contains all of the data generated for the Performance Evaluation Study as well as the Bash and Python scripts I created to automate the testing workflow

## Apache Benchmark Output

Apache Benchmark was run at 10 different concurrence levels for each of the 8 instances. Each instance has a directory, e.g. `/t2Micro`. Inside the folder there is a CSV file and TSV file for each concurrency level, which are a result of setting the `-g` and `-i` parameters respectively in AB. Finally, `abOutput.txt` is the output of running AB 10 times. 

## YCSB Output

Inside the directory for each instance, `ycsbOutput.txt` is the output of running YCSB seven times at the specified thread counts. 

## Scripts

Four scripts were used: 

- `abScript` is a Bash script used to repeatedly call Apache Benchmark at increasing concurrence levels. 
- `abScraper.py` is a Python script used to parse the response saved in `abOutput.txt` for each instance. 
- `ycsbScript` is a Bash script used to repeatedly call YCSB at increasing thread count. 
- `ycsbScraper.py` is a Python script used to parse the response saved in `ycsbOutput.txt` for each instance. 

## Other Notes

- Apache Benchmark was initially run with 5,000 requests instead of the 10,000 that were used in the study. `/ab5000Tests` contains the results of these tests. 
- To test the consistency of Apache Benchmark, the same experiment was run three times on a T2.Large instance. The results of this is stored in `/t2Large`,`/t2Large2` ,`/t2Large3` respectively. 
- `ycsbResults.xlsx` and `abResults.xlsx` store the aggregated results of all of the tests. 

