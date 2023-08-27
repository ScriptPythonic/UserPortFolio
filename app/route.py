from flask import Flask,Blueprint,render_template

routes= Blueprint('routes', __name__)


@routes.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@routes.route( '/project', methods =["GET"])
def project():
    return render_template("project.html")

@routes.route( '/about', methods =["GET"])
def about():
    return render_template("about.html")
@routes.route( '/blog', methods =["GET"])
def blog():
    return render_template("blog.html")