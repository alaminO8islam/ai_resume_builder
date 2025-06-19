from flask import Blueprint, render_template, request, send_file
import io
from xhtml2pdf import pisa

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate():
    # Extract data from form
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    address = request.form.get('address')
    summary = request.form.get('summary')
    education = request.form.get('education')
    experience = request.form.get('experience')
    skills = request.form.get('skills')

    # Render result page with form data
    return render_template('result.html', name=name, email=email, phone=phone,
                           address=address, summary=summary, education=education,
                           experience=experience, skills=skills)

@main.route('/download')
def download_pdf():
    # For simplicity, reusing the result.html template. You can create a separate one for PDF styling.
    rendered = render_template('result.html',
        name=request.args.get('name'),
        email=request.args.get('email'),
        phone=request.args.get('phone'),
        address=request.args.get('address'),
        summary=request.args.get('summary'),
        education=request.args.get('education'),
        experience=request.args.get('experience'),
        skills=request.args.get('skills')
    )
    pdf = io.BytesIO()
    pisa_status = pisa.CreatePDF(rendered, dest=pdf)

    if not pisa_status.err:
        pdf.seek(0)
        return send_file(pdf, mimetype='application/pdf', as_attachment=True, download_name='resume.pdf')
    else:
        return "Error generating PDF", 500
