from flask import render_template, request, Blueprint

from lightning_flask.contact.forms import ContactForm

contact = Blueprint('contact', __name__)

@contact.route("/contact",  methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():  # if method == 'POST'
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash(f'Your email has been sent!', 'success')
    # generate the URL for the the login view and 
    # generate the redirect response to the generated URL
        return redirect(url_for('contact.login')) 
    return render_template('contact.html', title='Contact', form=form)
