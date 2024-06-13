from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
 
app = Flask(__name__)
 
@app.route('/')
def dashboard():
    # Read CSV data
    df = pd.read_csv("C:\\Users\\preet\\OneDrive\\Desktop\\Preethi's Dashboard\\employee_timesheet_status.csv")

    # Create a bar chart for total hours worked per project
    bar_fig = px.bar(df, x='EmployeeName', y='TotalHoursWorked', color='EmployeeID', title='Total Hours Worked per Project', barmode='group')
    bar_chart = pio.to_html(bar_fig, full_html=False)

    #Creat a pie chart for the distribution of hours per employee
    pie_fig= px.pie(df, names= 'EmployeeName', values= 'TotalHoursWorked', title= 'Distribution of Hours')
    pie_chart= pio.to_html(pie_fig, full_html= False)
    
    # Calculate KPI: total approvals and total pending timesheets


    

    return render_template('column.html',bar_chart=bar_chart, pie_chart= pie_chart)

    

if __name__ == '__main__':
    app.run(debug=True)