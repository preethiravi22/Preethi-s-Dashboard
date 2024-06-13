from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)


def dashboard():

     df = pd.read_csv("C:\\Users\\preet\\OneDrive\\Desktop\\Preethi's Dashboard\\employee_timesheet_status.csv")

#KPIs
total_hours= df['TotalHoursWorked'].sum()



if __name__ == '__main__':
    app.run(debug=True)