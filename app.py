
from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from main import getPrediction
import os

# Save images to the 'static' folder as Flask serves images from this directory
UPLOAD_FOLDER = 'static/images/'

# Create an app object using the Flask class. 
app = Flask(__name__, static_folder="static")

# Add reference fingerprint. 
# Cookies travel with a signature that they claim to be legit. 
# Legitimacy here means that the signature was issued by the owner of the cookie.
# Others cannot change this cookie as it needs the secret key. 
# It's used as the key to encrypt the session - which can be stored in a cookie.
# Cookies should be encrypted if they contain potentially sensitive information.
app.secret_key = "secret key"

# Define the upload folder to save images uploaded by the user. 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the route to be home. 
# The decorator below links the relative route of the URL to the function it is decorating.
# Here, index function is with '/', the root directory. 
# Running the app sends to index.html.

@app.route('/')
def index():
    return render_template('index.html')

#Add Post method to the decorator to allow for form submission. 
        
@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        img = request.files['file']
        if img.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if img:
            img_path = "static/images/" + img.filename
            img.save(img_path)


            label = getPrediction(img_path)
            flash(label)

            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
            flash(full_filename)

            return redirect('/')     


if __name__ == "__main__":
    app.run()