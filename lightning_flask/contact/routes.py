from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_mail import Message

from lightning_flask import mail
from lightning_flask.contact.forms import ContactForm
from lightning_flask.contact.utils import send_contact_email

contact = Blueprint('contact', __name__)

@contact.route("/contact",  methods=['GET', 'POST'])
def email():
    form = ContactForm()
    if form.validate_on_submit():  
        send_contact_email(form)
        flash(f'Your email has been sent!', 'success')
        return redirect(url_for('contact.email')) 
    return render_template('contact.html', title='Contact', form=form)
