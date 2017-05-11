# app/home/views.py

from flask import render_template
from flask_login import login_required

from . import home

# Each view handles requests to the specified URL

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/deptdashboard')
@login_required
def deptdashboard():
    """
    Render the deptdashboard template on the /deptdashboard route
    """
    return render_template('home/deptdashboard.html', title="DeptDashboard")

@home.route('/deptreport')
@login_required
def deptreport():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/deptreport.html', title="DeptReport")
