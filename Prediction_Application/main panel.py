import tkinter as tk
from tkinter import ttk
import pickle
import numpy as np
import HelpLib as hl # local help library
import sklearn
from tkinter import messagebox
import sklearn.linear_model
import scipy
import os
import tkcalendar
from datetime import datetime

# lists to be converted to dictionaries
lst_nat = ['Egyptian', 'Filipino', 'Indian','Jordanian','Kenyan','Lebanese','Moroccan','Nepali','Sri Lankan','Tunisian']
lst_job = ['Asst Technician','Driver', 'Helper', 'Merchandiser', 'Sales Executive','Senior Sales Executive','Technician','Technician - Air Cons','Van Salesman','Warehouse Asst']
lst_dept = ['Consumer Electronics & Home Appliances','Consumer Products','General Products','HR & Administration', 'Home Appliances Service Center','Logistics','Office Equipment & Business Solutions','Office Equipment Service Center','Office Furniture & Furnishing']
lst_mart = ['Divorced', 'Married', 'Single', 'Widow']
lst_qual = ['Bachelors','Diploma', 'High School','Information Not Available','Masters','Primary School']

# converting lists to dictionaries  and converting the values to numbers in order to be ready for linear regression model
dict_nat = hl.convert.list_to_dict(lst_nat)
dict_job = hl.convert.list_to_dict(lst_job)
dict_dept = hl.convert.list_to_dict(lst_dept)
dict_mart = hl.convert.list_to_dict(lst_mart)
dict_qual = hl.convert.list_to_dict(lst_qual)

# loading model
path = os.path.realpath("linear model.sav")
model = pickle.load(open(path, 'rb'))


# This function converts the input of comboboxes to numbers based on list_to_dict function in the help library 
# the function converts the decimal input of the prediction to year-month integers
def predict_period(nat, dept, job, mart_status, join_age, qual):
    """This function takes the values and reshape them into the linear model and produces a message box with the result"""
    # shaping the values into one entry
    emp = np.array([nat,dept,job,mart_status,join_age, qual]).reshape(1,-1)
    # saving the result 
    per = model.predict(emp)
    # converting the decimal value of the result to years and months 
    year, month = hl.convert.dec_to_year(per)
    # showing the result as average , +- 1 to produce minmum amd maximum values
    messagebox.showinfo("The prediction", f"The estimated time for this employee is:\nAverage: {year} year(s) and {month} month(s) ± 2 years")


def days_between(d1, d2):
    """This fucntion returns the difference between two dates the input date should be dd/mm/yyyy the output is years """
    d1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%d/%m/%Y")
    diff = abs((d2 - d1).days) 
    # converting days to years
    years = np.round(diff/365,3)
    return years

####################################### Gui Controls #######################################

main_window = tk.Tk()
# getting screen resolution and calculating the window dimensions to open in the centre of the screen
width = (main_window.winfo_screenwidth() /2) - (500/2)
height = (main_window.winfo_screenheight() /2) - (600/2)
main_window.geometry("500x600+"+str(int(width))+"+"+str(int(height)))
# setting the title 
main_window.title('Service Period prediction - By Rimoun George')
# header label
lbl_header = tk.Label(main_window, text="Service Period prediction - By Rimoun George", font=("bold", 12))
lbl_header.grid(rows=1, column=1, padx=40, pady=10,sticky='wne')

# nationality label
lbl_nat = tk.Label(main_window, text="Choose nationality", font=(10))
lbl_nat.grid(rows=2, column=1, padx=10, pady=5, sticky='w')

# Nationality Combobox
cmbx_nat = tk.ttk.Combobox(main_window, values=lst_nat, state='readonly')
cmbx_nat.grid(rows=3, column=0, columnspan=2, padx=10, pady=5, sticky='w')
cmbx_nat.current(0)

# job label
lbl_job = tk.Label(main_window, text="Choose job", font=(10))
lbl_job.grid(rows=4, column=1, padx=10, pady=5, sticky='w')

# Job Combobox
cmbx_job = tk.ttk.Combobox(main_window, values=lst_job, state='readonly')
cmbx_job.grid(rows=5, column=0,columnspan=2, padx=10, pady=5, sticky='w')
cmbx_job.current(0)

# department label
lbl_dept = tk.Label(main_window, text="Choose Department", font=(10))
lbl_dept.grid(rows=6, column=1, padx=10, pady=5, sticky='w')

# Department Combobox
cmbx_dept = tk.ttk.Combobox(main_window, values=lst_dept, state='readonly')
cmbx_dept.config(width=40)
cmbx_dept.grid(rows=7, column=0, columnspan=5, padx=10, pady=5, sticky='w')
cmbx_dept.current(0)

# martial status label
lbl_mart = tk.Label(main_window, text="Choose Martial status", font=(10))
lbl_mart.grid(rows=8, column=1, padx=10, pady=5, sticky='w')

# Martial Status Combobox
cmbx_mart = tk.ttk.Combobox(main_window, values=lst_mart, state='readonly')
cmbx_mart.grid(rows=9, column=0,columnspan=2, padx=10, pady=5, sticky='w')
cmbx_mart.current(0)

# qualificaiton label
lbl_qual = tk.Label(main_window, text="Choose Qualification", font=(10))
lbl_qual.grid(rows=10, column=1, padx=10, pady=5, sticky='w')


# Qualification Combobox
cmbx_qual = tk.ttk.Combobox(main_window, values=lst_qual, state='readonly')
cmbx_qual.grid(rows=11, column=0, columnspan=2, padx=10, pady=5, sticky='w')
cmbx_qual.current(0)

# Birthdate label
lbl_birth = tk.Label(main_window, text="Select birth date", font=(10))
lbl_birth.grid(rows=12, column=1, padx=10, pady=5, sticky='w')

# Birthdate date picker
dp_birth = tkcalendar.DateEntry(main_window, width=12, background='darkblue',foreground='white', borderwidth=2, date_pattern='dd/mm/y')
dp_birth.grid(rows=13, column=0, columnspan=2, padx=10, pady=5, sticky='we')

# joining date label
lbl_birth = tk.Label(main_window, text="Select joining date", font=(10))
lbl_birth.grid(rows=14, column=1, padx=10, pady=5, sticky='w')

# Joining date picker
dp_joining = tkcalendar.DateEntry(main_window, width=12, background='darkblue',foreground='white', borderwidth=2, date_pattern='dd/mm/y')
dp_joining.grid(rows=15, column=0, columnspan=2, padx=10, pady=5, sticky='we')

# calculation button
btn_predict = tk.Button(main_window,text="Calculate the estimated service period", command= lambda: predict_period(dict_nat[cmbx_nat.get()] , dict_dept[cmbx_dept.get()], dict_job[cmbx_job.get()], dict_mart[cmbx_mart.get()], days_between(dp_joining.get(),dp_birth.get()), dict_qual[cmbx_qual.get()] ))
btn_predict.grid(rows=16, column=0, columnspan=2, padx=10, pady=10, sticky='we')

#main loop
main_window.mainloop()