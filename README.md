
## LA-DAT-08 Course Repository

Course materials for [General Assembly LA's Data Science
course](https://generalassemb.ly/education/data-science?where=los-angeles)
in Los Angeles, CA (August 24 - November 9, 2015). View student work in
the [student
repository](https://github.com/ga-students/DAT-LA-08-STUDENTS).

**Instructor:** Dan Wilhelm.

**Office hours:** TBD. 

**Project Info:** [Course Project information](project.md) | [Project Ideas](project-ideas.md)

**Resources:** [Recommended Course Books](books.md)


Week | Monday | Wednesday
--- | --- | ---
1 | 8/24: [Introduction](#class-1-introduction) | 8/26: [Command-Line Tools](#class-2-command-line-tools-for-data-science)
2 | 8/31: [Python](#class-3-python) | 9/02: [Git & Python: Problem Solving](#class-4-git-and-python-problem-solving)
3 | 9/07: No Class (Labor Day) | 9/09: [APIs & Web Scraping](#class-5-apis-and-web-scraping)<br>**Homework:** [HW1](./hw/hw1.pdf) due
4 | 9/14: [Statistics & k-NN from Scratch](#class-6-statistics-and-knn)<br>**Milestone:** Know Your Question and Data Set | 9/16: [NumPy & Linear Regression from Scratch](#class-7-numpy-and-linear-regression)
5 | 9/21: [Data Exploration with Pandas](#class-8-data-exploration-with-pandas) | 9/23: [scikit-learn & k-Means Clustering](#class-9-scikit-learn-linear-regression)<br>**Homework:** [HW2](./hw/hw2.pdf) due
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
