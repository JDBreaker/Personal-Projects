from flask import Flask, request, render_template, send_file
from PyPDF2 import PdfReader, PdfWriter
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    password = request.form['password']
    new_filename = request.form['new_filename']

    if file and password and new_filename:
        reader = PdfReader(file)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        output_path = os.path.join('protected_pdfs', new_filename + '.pdf')
        with open(output_path, 'wb') as f:
            writer.write(f)

        return send_file(output_path, as_attachment=True)

    return 'Missing file, password, or new filename', 400

if __name__ == '__main__':
    if not os.path.exists('protected_pdfs'):
        os.makedirs('protected_pdfs')
    app.run(debug=True)
