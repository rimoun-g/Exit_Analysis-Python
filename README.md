# Exit Analysis

## Understanding the business:
- There is XYZ company that have monthly records of employees who leave on monthly basis. The company is interested in finding answers to many questions and also to get helped in the future in the recruitment process to reduce the drop in business operations that results of changing employees for the same position.

## Understanding the data:
- Identified the related fields and columns and how to utilize them.

## Preparation of data:
- At the beginning the data was collected from word files. After making the first analysis, the company was interested in more analysis and provided more data with more features. The data provided  by the company but not allowed to be published. However, the results were published as a demonstration of analysis. Both datasets are similar and have been cleaned appropriately for the analysis. 

## Modeling:
- The company found valuable insights and they wanted more accuracy so the data which the company provided from its system is analyzed and answered the questions similar to the analysis in First stage with some additional in-depth insights.
The modeling of the data has included several uses of data like explanatory analysis, inferential analysis, and regression analysis. The company provided some assumptions and the inferential statistics is used to answer them. Created a basic Linear Regression Model to predict the service period of an employee based on previous observations.

## Evaluation:
- After finishing all the analysis, the results were consistent and supported the overall trend. Many visualizations and statics have been used to cross-check the results.

## Deployment:
- The results of this analysis have been deployed in form of predictive application for the employees that will join the company. The application has been used in the company to determine the leave date of employees. The application made several accurate predictions as per the feedback received from the company, especially for the top five jobs.

## Final Results:
- The company was able to pinpoint the hot jobs and take the correct actions to recruit the employees without a drop in the business flow. Also, answered many questions regarding the active jobs, departments, and the demographics of the employees.
- The company was able to identify the gaps and fill them properly.
- The company used the results of the inferential statistics to make sure of their assumptions. Besides, predict and estimate the employees' service period before joining.

# Technical aspects:

## **Libraries used in the project:** 
- Pandas
- matplotlib.pyplot
- seaborn
- numpy
- sklearn

## Data:

The Folders include the files as per the following graph:

#### ![Project plan](https://i.imgur.com/TMXz6lJ.jpg "Analysis plan")

### First Dataset
Folder: Descriptive_Analysis_1
The folder contains 
- The first dataset which was collected from the word files.
- Descriptive Analysis and the related reports.

### Second Dataset
Folder: Descriptive_Analysis_2
The folder contains 
- The dataset from the company system.
- Descriptive Analysis and the related reports.

Folder: Inferential_Analysis
The folder contains 
- Inferential analysis and the related reports.
- Regression analysis and the predictive model.

Folder: Prediction_Application
The folder contains 
- The Generated model from the previous step.
- The desktop application for prediction.

## The application:
- Created an application `User interface` using tkinter to use it with the model to estimate the service period for an employee before joining.  
User interface options
#### ![User interface1](https://i.imgur.com/F3iDE2O.jpg "Application user interface")  
The Results
- The company was able to pinpoint the hot jobs and take the correct actions to recrute 
#### ![User interface2](https://i.imgur.com/RiuWdJB.jpg "Application prediction")  

### How to Run the application:
In the application path use bash or conda cmd to run the following command:  
```conda env create -f environment.yml```  
After that activate the enviroment:```conda activate my_env```   
and run the script: `python "main panel.py" `
