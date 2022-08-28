from app import app, db
# from site import app 
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
from datetime import datetime

import forms


@app.route('/')
@app.route('/index') #this is a router used to route defined templates
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


#for adding Tasks
# @app.route('/')
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        # print('Submitted title', form.title.data)
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Task Added To The DataBase')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


#for editing Tasks
    @app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
    def edit(task_id):
        task = Task.query.get(task_id)
        form = forms.AddTaskForm()

        if task:
            if form.validate_on_submit():
                task.title = form.title.data
                task.data = datetime.utcnow()
                db.session.commit()
                flash('Task Has Been Updated')
                return redirect(url_for('index'))
            form.title.data = task.title
            return render_template('edit.html', form=form, task_id=task_id)
        else:
            flash('Task Not Found')
        return redirect(url_for('index'))

#for deleting note
@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
    def delete(task_id):
        
        task = Task.query.get(task_id)
        form = forms.DeleteTaskForm()

        if task:
            if form.validate_on_submit():
                db.session.delete(task)
                db.session.commit()
                flash('Task Has Been Deleted')
                return redirect(url_for('index'))
            
            return render_template('delete.html', form=form, task_id=task_id, title=task.title)
            
        else:
            flash('Task Not Found')
        return redirect(url_for('index'))
        