from flask import Blueprint, render_template, request
from .utils import generate_resume

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        skills = request.form['skills']
        resume = generate_resume(name, email, skills)
        return render_template('result.html', resume=resume)
    return render_template('index.html')
