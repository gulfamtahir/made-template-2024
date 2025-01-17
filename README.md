# US Crimes and Mass Shootings Analysis


### Description

This project analyzes the intersection of mass shootings and overall crime trends in the United States, focusing on geospatial, temporal, and demographic patterns. Using datasets on U.S. crime and the history of mass shootings, the data pipeline processes, cleans, and integrates the information to uncover key insights. The analysis highlights regional hotspots, trends over time, and correlations between crime rates and mass shooting incidents. The findings aim to inform policymakers and law enforcement by providing actionable insights for targeted interventions and preventive measures.

### Features 
- **Relevance** : Both datasets are from the USA details , which made them highly relevant for  this project needs.
- **Coverage Period** : As both data do contains the relevant time frame which I need to pluck out the information and going to use for the analysis (2017 - 2022).
- **Open Data** :  Both of the datasets are the publicly available.


# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU. This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester. Before you begin, make sure you have Python and Jayvee installed. We will work with Jupyter notebooks. The easiest way to do so is to set up VSCode with the Jupyter extension.

To get started, please follow these steps:

1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. Do not rename the repository during the semester.
2. Setup the exercise feedback by changing the exercise badge sources in the `README.md` file following the patter `![](https://byob.yarr.is/<github-user-name>/<github-repo>/score_ex<exercise-number>)`. For example, if your user is myuser and your repo is myrepo, then update the badge for exercise 1 to `![](https://byob.yarr.is/myrepo/myuser/score_ex1)`. Proceed with the remaining badges accordingly.


### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions → Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
