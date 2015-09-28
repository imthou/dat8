#Homework 3b | GA Data Science LA 8#

**Out:** Monday, September 23, 2015. 
**Due (in student repository):** Monday, October 5, 2015.

For this homework, complete either [Homework 3](./hw3.md) or [Homework 3b](./hw3b.md). Homework3b (student logins) is recommended, since it is more straightforward to analyze the data. Submit a Jupyter notebook answering the below questions.

**Dataset: hw3-student-logins.csv**.

+ Each session has a start and end time.
+ Students have multiple sessions and sometimes take different classes.
+ Account created date is an indicator of how long that student has been participating in the online class.

####Questions
1. Create metrics that summarize the data. Make graphs of each column.
<br>

2. Create a new column for the session duration. (Hint: Look up the ```apply``` method.)
<br>

3. Is there data that should not be included in the analysis? Is there data that should be replaced with other data? Defend your decision of what to do with it.
<br>

4. Suppose you are given the data for a student, excluding the session end time. Can you predict the end time (i.e. the session duration)? Using any model of your choice, predict the session duration.
<br>

5. Explain how and why you selected the features for your model.
<br>

6. Argue how well your model performs on this dataset and how well it likely generalizes, e.g. using cross-validation or any other metric.