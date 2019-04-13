from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class WordForm(FlaskForm):
    word = StringField('Word', validators=[DataRequired()])
    definition = TextAreaField('Definition', validators=[DataRequired()])
    submit = SubmitField('Add')
