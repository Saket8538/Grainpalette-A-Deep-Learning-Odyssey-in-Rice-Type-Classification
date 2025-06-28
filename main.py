from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from predict import predict_rice_type 

app = Flask(__name__)

# Configure the uploads folder (we store uploaded images in 'static/uploads')
UPLOAD_FOLDER = os.path.join('static', 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
@app.route('/details.html')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if an image file was provided in the POST request
    if 'image' not in request.files:
        flash('No file part in the request')
        return redirect(url_for('index'))
    
    file = request.files['image']
    
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('index'))
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Call the predict function from predict.py
        predicted_label, prediction_probability = predict_rice_type(file_path)
        
        # Create a URL for the uploaded image to display on the result page
        image_url = url_for('static', filename='uploads/' + filename)
        
        # Render result.html with the prediction and image information
        return render_template('result.html', 
                               label=predicted_label, 
                               probability=prediction_probability, 
                               image_url=image_url)
    else:
        flash('File upload failed.')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
