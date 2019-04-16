from flask import url_for, current_app
from flask_mail import Message

from lightning_flask import mail

def send_contact_email(form):
    msg = Message(form.subject.data,
                  sender='contact@example.com',
                  recipients=['jayrey.go@gmail.com'])
    msg.body = f"""From: {form.name.data} {form.email.data}

{form.message.data}
"""
    mail.send(msg)