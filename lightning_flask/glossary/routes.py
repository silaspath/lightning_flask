from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required

from lightning_flask import db
from lightning_flask.glossary.forms import WordForm
from lightning_flask.models import CWord


glossary = Blueprint('glossary', __name__)

@glossary.route("/glossary/new", methods=['GET', 'POST'])
@login_required
def new_word():
    form = WordForm()
    if form.validate_on_submit():  
        word = CWord(word=form.word.data, definition=form.definition.data)
        db.session.add(word)
        db.session.commit()
        flash('Your word has been added to the Glossary!', 'success')
        return redirect(url_for('main.home'))
    return render_template('add_word.html', title='Add Word',
                           form=form, legend='Add Word')

@glossary.route("/glossary")
@login_required
def show_glossary():
    glossary = CWord.query.all()
    return render_template('glossary.html', title='Glossary', glossary=glossary)
