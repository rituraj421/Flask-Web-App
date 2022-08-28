from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):   #in wtforms we use class attribute
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')
