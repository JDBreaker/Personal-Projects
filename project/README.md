# PDF Protector
#### Video Demo:  <https://youtu.be/Wv6T5C-hD7s?si=d-ovtnDwCwIYo9Ru>
#### Description:
Hi, my name is Jose Diego and i made an app to put passwords in PDFs files to increase security in these type of files. I called PDF Protector.

I created this app using three libraries, Flask, to handle web request and responses, PyPDF2, to write and read PDF files and os to interact with the operative system.
The first part, the one who launch the flask app is **app = Flask(__name__)**
I create two differents routes to make this app work:

**@app.route('/')**: This route use the function **render_template** to call an html file, **index.html** in this case, when the root URL is accessed.

**@app.route('/upload', methods=['POST'])**: This route is the one in charge of the file upload and the encryption process. Here i stablish the three main components of this route:

**file = request.files['file']**, this retrieve the uploaded file from the user.

**password = request.form['password']**, this retrieve the password the user put in the form.

**new_filename = request.form['new_filename']**,this retrieve the new name for the new file created from this app.

This three are in charge of get all the important information from the user to make the app work.

We can also check the all the functions i use in this app:

**reader = PdfReader(file)**: This function read the PDF file uploaded.

**writer = PdfWriter()**: This function create a new PDF file.

**for page in reader.pages**: This function loops through each page of the original PDF and adds it to the new one.

**writer.encrypt(password)**: This funtion encrypt the new PDF file with the password provided by the user.

**output_path = os.path.join('protected_pdfs', new_filename + '.pdf')**: This function define the output path for the new PDF file.

**with open(output_path, 'wb') as f**: This function writes the new PDF file encrypted in the specified path.

**return send_file(output_path, as_attachment=True)**: This function send the new encrypted PDF file to the user as a download.

If any of the fields are missing this function **return 'Missing file, password, or new filename', 400** will return an error and a message.

If we look in the main block, we found three important parts:

**if __name__ == '__main__'**: This ensure the codes runs only if the script is executed directly.

**if not os.path.exists('protected_pdfs')**: This check if the protected_pdfs folder exist and creates if it doesn't.

**app.run(debug=True)**: This start the app in debug mode.

This is all about the **app.py**, the core of this app, now let's talk about de HTML file, the **index.html**.

With this HTML file i created a simple form to the user to put the important information and the file necessary to make this app works.

I use the basic structure for a HTML file, **DOCTYPE**, **lang="en"**, **meta**, **title**, etc. I don't know if it's necesary to explain every single part of the HTML file,
but i will do my best to try to explained the most important parts properly:


**meta name="viewport" content="width=device-width, initial-scale=1.0"** is the part of the code who ensure the page of the app is responsive and ajust to different screen sizes.

**form action="/upload" method="post" enctype="multipart/form-data"** creates the form who allowed to the user submit the data to the **/upload** route using the post method and
file uploads.

**label for="file">Choose PDF:</label**:This creates a label for the file input file.

**input type="file" id="file" name="file" accept="application/pdf" required**: This creates an input field to select a PDF file, the **accept** attribute ensures only PDF files can be selected and **requiered** attribute make it mandatory.

**label for="password">Password:</label**: This create a label for the user password.

**input type="password" id="password" name="password" required**: This creates an input to put the password to the new PDF file. The attribute **required** make it mandatory.

**label for="new_filename">New Filename:</label**: This create a label to the user to put the name of the new encrypted file.

**input type="text" id="new_filename" name="new_filename" required**: This creates an input to put the name of the new encrypted PDF file. The attribute **requiered** make it mandatory.

**button type="submit">Protect PDF</button**: This creates a button to send the file and the data from the user to create and encrypt the new PDF file.

This is the final project i build for this course, PDF Protector, and the best i can do at the moment on my own. I will return someday to this project with more experience and maybe i will be able to improve it, i will definitely improve mi skills in python, i found this coding language really funny, but at this moment i'm proud of this small project i made. Thanks for all, CS50, i'll be back with the python course!
