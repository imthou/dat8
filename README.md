
## LA-DAT-08 Course Repository

Course materials for [General Assembly LA's Data Science
course](https://generalassemb.ly/education/data-science?where=los-angeles)
in Los Angeles, CA (August 24 - November 9, 2015). View student work in
the [student
repository](https://github.com/ga-students/DAT-LA-08-STUDENTS).

**Instructor:** Dan Wilhelm. **Expert-In-Residence:** Frank Portman

**Office hours:** TBD. 

**Project Info:** [Course Project information](project.md) | [Project Ideas](project-ideas.md)

**Resources:** [Recommended Course Books](books.md)

[HOMEWORK ONE: Python & Linear Regression](./hw/hw1.pdf) - Due Monday, Sep. 14

Week | Monday | Wednesday
--- | --- | ---
1 | 8/24: [Introduction](#class-1-introduction) | 8/26: [Command-Line Tools](#class-2-command-line-tools-for-data-science)
2 | 8/31: [Python](#class-3-python) | 9/02: [Git & Python Techniques](#class-4-git-and-python-techniques)
3 | 9/07: No Class (Labor Day) | 9/09: [Machine Learning & Linear Regression from Scratch](#class-5-machine-learning-and-linear-regression)
4 | 9/14: [APIs & Web Scraping](#class-6-apis-and-web-scraping)<br>**Homework:** [HW1](./hw/hw1.pdf) due | 9/16: [NumPy & k-NN from Scratch](#class-7-numpy-and-k-nn)
5 | 9/21: [Data Exploration with Pandas](#class-8-data-exploration-with-pandas)<br>**Milestone:** Know Your Question and Data Set | 9/23: [scikit-learn & k-Means Clustering](#class-9-scikit-learn-linear-regression)<br>**Homework:** [HW2](./hw/hw2.pdf) due
6 | 9/28: [Linear Regression II & Data Distributions](#class-10-linear-regression-ii-and-data-distributions) | 9/30: [Logistic Regression & AUC](#class-11-logistic-regression-and-auc)
7 | 10/05: [Neural Networks I](#class-12-neural-networks-i) | 10/07: [Complete Data Science Example](#class-13-complete-data-science-example)<br>**Milestone:** Data Analysis and Exploration
8 | 10/12: [Image Data: Neural Networks II](#class-14-image-data-neural-networks-ii) | 10/14: [Feature Selection & Dimensionality Reduction](#class-15-feature-selection-and-dimensionality-reduction)<br>**Homework:** [HW3](./hw/hw3.pdf) due
9 | 10/19: [Text Data: Natural Language Processing](#class-16-text-data-natural-language-processing) | 10/21: [Text Data: Naive Bayes](#class-17-text-data-naive-bayes)<br>**Milestone:** Project Rough Draft Peer Review
10 | 10/26: [Recommendation Systems](#class-18-recommendation-systems) | 10/28: [Deep Learning: Neural Networks III](#class-19-deep-learning-neural-networks-iii)<br>**Homework:** [HW4](./hw/hw4.pdf) due
11 | 11/02: [Decision Trees & Random Forests](#class-20-decision-trees-and-random-forests) | 11/04: [Big Data & Course Review](#class-21-big-data-and-course-review)
12 | 11/09: [Project Presentations](#class-22-project-presentations)<br>**Milestone:** Final Project! | 


### Installation and Setup
* Install the latest [Anaconda distribution](http://continuum.io/downloads) -- **Python 3.4**.
* Install [Git](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and
create a [GitHub](https://github.com/) account.
* Install a text editor ([Sublime Text 3](http://www.sublimetext.com/3)) and IDE ([PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/)).
* Once you receive an email invitation from [Slack](https://slack.com/), join our "DAT-08 team" and add your photo!
* **WINDOWS USERS:** Install [Gow](https://github.com/bmatzelle/gow/wiki). Direct link to installer: [Gow 0.8.0 Installer (EXE)](https://github.com/bmatzelle/gow/releases/download/v0.8.0/Gow-0.8.0.exe)

### Class 1: Introduction
* Introduction to General Assembly
* Course overview: our philosophy and expectations [slides](./slides/01-course-overview.pdf)
* Data science overview [slides](./slides/01-introduction.pdf)

**Post-class:**

* Resolve any installation issues before next class.
* If you are not familiar with the command line:
	* Work through GA's excellent [command line tutorial](http://generalassembly.github.io/prework/command-line/#/). Try this brief [quiz](https://gahub.typeform.com/to/J6xirf) -- submitting your answers is optional!
	* For more practice, here is another [great command-line tutorial](http://seankross.com/notes/cli/cli.html). 
	* Codecademy just released their own [command-line tutorial](https://www.codecademy.com/courses/learn-the-command-line).
	* **WINDOWS USERS**: We will be using [Gow](https://github.com/bmatzelle/gow/wiki) in class to give you access to the same command line tools. After installing Gow, open the standard Windows CLI by pressing Win-R to open a Run... dialog, type *cmd*, then press Enter. Then, follow the tutorials as normal!


### Class 2: Command-Line Tools for Data Science
* **Basic tools:** review of basic commands, nano, curl, wc, head, tail
* **More tools:** grep, uniq, sort, tr, piping and redirection operators
* Introduce regular expressions

**Additional Resources:**
* [Command Line Basics notes](resources/02-command-line-basics.md)
* [List of OS X Commands](resources/02-osx_unix_commands.md)
* Book: ["The Linux Command Line"](http://linuxcommand.org/tlcl.php) <- free PDF!
* Book: ["Data Science at the Command Line"](http://shop.oreilly.com/product/0636920032823.do), by Jeroen Janssens

* In-class examples:
	* **Number of dictionary words that start with a capital
	letter:** ```grep '^[A-Z]' <words | wc -l```
	* **Tweet usernames mentioned:** ```grep -o "@\w* " deuszu_tweets.csv | sort | more```  (NOTE: This only retrieves usernames followed by a space!)
	* **List the most-used words in Huckleberry Finn:** ```tr ' ' '\n' <finn.txt | tr -d ',."' | sort | uniq -c | sort -r | head```


**Post-class:**

* [Command-line tools specific to Mac OS!](http://www.mitchchn.me/2014/os-x-terminal/)
* Do the [Python prework](./hw/03-python-prework.py)
* Try some [Python problems](./hw/02-python-problem-solving.pdf)
* If you need more practice with Python, review the "Python Overview"
section of [A Crash Course in Python](http://nbviewer.ipython.org/gist/rpmuller/5920182), read [Dive into Python 3](http://www.diveintopython3.net/), try some of [Codecademy's Python course](http://www.codecademy.com/en/tracks/python), or work through [Google's Python Class](https://developers.google.com/edu/python/) and its exercises.
* More command-line challenges:
	* Using one ```sort``` command, can you sort 'shopping.lst' by the second column? (Hint: ```man sort```)
	* Look up ```man cut```. Using ```cut```, from 'shopping.lst', make a list of unique products without the quanitites or commas.
	* In 'epa-http.txt', how many unique visitors visited the EPA's servers? (the first column)
	* Using ```tail``` to skip the first few lines, reformat 'primes1.txt' to be a list of primes, one per line.
	* Combine 'primes1.txt' and 'primes2.txt' into a single file with 2 million primes. Figure out how to do this two different ways, with ```cat``` and ```sort```.
	* Our in-class example of tweet mentions only makes a list of usernames followed by a space! (Why?) Can you rewrite it to make a list of all tweet usernames mentioned?
	* In 'epa-http.txt', find all PDFs that people searched for.
	* Look up ```sed``` and rework the Huckleberry Finn example so that "'t" is replaced with " not" throughout the text, so that 't' is not one of the most-used "words"!


### Class 3: Python

* Review Python and problem solving techniques
* Practice writing command-line scripts
* Python group exercises!
* [Slides](./slides/03-intro-python.pdf)

**Post-class:**

* Practice writing functions! Here are some practice problems that lead up to solving Project Euler Problem 3:
	* Look up the modulo operator (%). What does it do? In your head, what is 4 % 3? 10 % 4? 15 % 5? Using the modulo operator, write a function ```is_multiple(n, m)``` which returns True if n is a multiple of m. (A number is a multiple if it divides evenly with 0 remainder. For example, 10 is a multiple of 5. So, ```is_multiple(10, 5)``` will return True.)

	* Write a function ```get_factors(num)``` that returns a list of the factors of num. For example, ```get_factors(30)``` returns [1, 2, 3, 5, 6, 10, 15, 30]. (For each number 1 to 30, test whether 30 is a multiple of it. Bonus: can you write this function as a list comprehension?)

	* Write a function ```is_prime(num)``` that returns True if num is prime. (A number is prime only if it has exactly two factors -- 1 and itself.)

	* [Project Euler Problem 3](https://projecteuler.net/problem=3): The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143? 

	* NOTE: If your code takes too much time, consider whether you need to test all numbers from 1..N to find the factors of N. For example, note that each factor has a pair: 1x60 = 60, 2x30 = 60, 4x15 = 60, 5x12 = 60, and 6x10 = 60. Experiment with this pairing idea -- what are the factors of 36?


### Class 4: Git and Python Techniques

* Python techniques -- zip, files, lists/tuples, sets, exceptions, list comprehensions, string formatting, datetime
* Git intro -- how to clone/pull, how to fork/commit/pull request. See instructions in the [student repository](https://github.com/ga-students/dat-la-07-students).
* [Python Techniques Slides](./slides/04-python-techniques.pdf)

* **Extra Git resources:**
	* [Git - The Simple Guide](http://rogerdudler.github.io/git-guide/)
	* [CodeSchool: Try Git](https://www.codeschool.com/courses/try-git) - A basic, interactive course using GitHub 
	* [Pro Git](https://progit.org/) - THE book to Git. (Free online)
	* [Git Pretty: Flowchart for if you mess up](http://justinhileman.info/article/git-pretty/)
	* [Atlassian Git Tutorial](https://www.atlassian.com/git/tutorials/) - More comprehensive 

* **Post-class:**
	* To prepare for next week, do homework 1.
	* Read [how to derive linear regression](http://isites.harvard.edu/fs/docs/icb.topic515975.files/OLSDerivation.pdf).
	* Try to derive a simpler model than in HW1. For the model **y = mx**, can you derive how to compute **m** which minimizes the sum of squared residuals? This is called linear regression through the origin.

### Class 5: Machine Learning and Linear Regression

* Machine learning
* Simple validation techniques
* Bias/Variance
* Derive linear regression through the origin [exercise](./code/05-basic-regression.py) | [solution](./code/05-basic-regression-complete.py)

* **Post-class:**
	* For a great intro to statistical learning, read chapter 2 of [Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) - PDF is free on their website!
	* Try to re-derive regression through the origin. (y = mx)
	* Try to derive general 2-D linear regression algebraically (y = mx + b) (see [this PDF](http://isites.harvard.edu/fs/docs/icb.topic515975.files/OLSDerivation.pdf))
	* Want more practice with Calculus, Statistics, or Probability? [Brilliant.org](https://brilliant.org) has excellent introductions to each of these, with plenty of practice problems.
	* To be most effective at web scraping, read a basic [CSS selector tutorial](https://css-tricks.com/how-css-selectors-work/), or [this one](http://www.sitepoint.com/web-foundations/css-selectors/).

* **Extra:**
	* Need more Python practice? Try this [code commenting exercise](./code/05-python-exercise.md).
	* A collection of [Euler 8 solutions](./code/05-euler8-solutions.py).
	* Interested in an [Euler 3 solution](./code/05-euler3-solutions.py) from last week's class?

### Class 6: APIs and Web Scraping

* Intro to PyCharm
* Getting data from text files, e.g. CSV
* Calling APIs (using [requests](http://docs.python-requests.org/en/latest/))
* Web scraping (using [requests](http://docs.python-requests.org/en/latest/) and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/))
