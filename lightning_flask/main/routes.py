from flask import render_template, request, Blueprint, url_for
from flask_login import current_user

from lightning_flask.models import Post

main = Blueprint('main', __name__)


# Register the home view function to URL rule "/home". Register this route to Flask.
@main.route("/")
@main.route("/home")
def home():  # AKA view function
    page = request.args.get('page', 1, type=int)  # by default, add a query parameter to this route. It's default value is 1
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=7)
    if current_user:
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('home.html', posts=posts, image_file=image_file)

@main.route("/about")
def about():
    return render_template('about.html', title='About')
