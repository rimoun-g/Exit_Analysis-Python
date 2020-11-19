# Exit Analysis
## Introduction:
- There is XYZ company that have monthly records of employees who leave monthly. The Analysis is made in a form of questions and answers. The questions were provided from the company side.
The folder contains many notebooks for different stages of the analysis.

**Libraries used in the project:** Pandas, matplotlib.pyplot, seaborn, numpy, and sklearn
#### ![Project plan](https://i.imgur.com/TMXz6lJ.jpg "Analysis plan")
## Data:
- At the beginning the data was collected from word files. After making the first analysis, the company was interested in more analysis and provided more data with more features. The data provided  by the company but not allowed to be published. However, the results were published as a demonstration for analysis.
## Stages as per each folder:
### First:
- Extracted the first version of data from the word files and made the proper analysis
### Second:
- The company found valuable insights and they wanted more accuracy so the data which the company provided from its system is analyzed and answered the questions similar to the analysis in First stage with some additional in-depth insights.
### Third:
- The company provided some assumptions and the inferential statistics is used to answer them.
### Fourth:
- Created a basic Linear Regression Model to predict the service period of employee based on previous observations.
### Fifth:
- Created an application `User interface` using tkinter to use it with the model to estimate the service period for an employee before joining.  
User interface options
#### ![User interface1](https://i.imgur.com/F3iDE2O.jpg "Application user interface")  
The Results
- The company was able to pinpoint the hot jobs and take the correct actions to recrute 
#### ![User interface2](https://i.imgur.com/RiuWdJB.jpg "Application prediction")  


## Final Results:
- The company was able to pinpoint the hot jobs and take the correct actions to recruit the employees without a drop in the business flow. Also, answered many questions regarding the active jobs, departments, and the demographics of the employees.
- The company was able to identify the gaps and fill them properly.
- The company used the results of the inferential statistics to make sure of their assumptions. Besides, predict and estimate the employees' service period before joining.

## How to Run the application:
In the application path use bash or conda cmd to run the following command:  
```conda env create -f environment.yml```  
After that activate the enviroment:```conda activate my_env```   
and run the script: `python "main panel.py" `
