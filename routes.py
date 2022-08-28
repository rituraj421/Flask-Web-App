from app import app, db
# from site import app 
from flask import render_template, redirect, url_for
from models import Task
from datetime import datetime

import forms


@app.route('/')
@app.route('/index') #this is a router used to route defined templates
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

# @app.route('/')
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        # print('Submitted title', form.title.data)
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)