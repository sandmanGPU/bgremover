from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from src.bgrem.pipeline.BGREM_pipeline import BG_REMOVER
from src.bgrem import logger
from flask_cors import CORS, cross_origin


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.rembg=BG_REMOVER()

UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

# Function to check if the uploaded file is an allowed image format
def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'mp4', 'avi'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/home')
@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/up', methods=['GET', 'POST'])
@cross_origin()
def upload_image():
    if request.method == 'POST':
        # Check if a file is provided in the POST request
        if 'image' not in request.files:
            return redirect(request.url)

        file = request.files['image']

        # Check if the file is empty
        if file.filename == '':
            return redirect(request.url)

        # Check if the file is allowed
        if file and allowed_file(file.filename):
            # Save the file to the uploads directory
            filename = secure_filename(file.filename)
            filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            file.save(filename)
            return redirect(url_for('show_image', filename=file.filename))

    return render_template('upload.html')

@app.route('/uploads/<filename>')
@cross_origin()
def show_image(filename):
    return render_template('upload.html', filename=filename)


@app.route('/results/<filename>')
@cross_origin()
def show_res(filename):
    savename = os.path.basename(filename).split('.')[0] + '-crop.png'
    return render_template('upload.html', resultname=savename, filename=filename)

@app.route('/process_image/<filename>', methods=['POST'])
@cross_origin()
def processImage(filename):
    if request.method=='POST':
        #Read the image from static upload folder
        inputname = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        #process it
        ff = clApp.rembg.setInput(inputname)
        save_dir = app.config['RESULT_FOLDER']
        os.makedirs(save_dir, exist_ok=True)
        resultname = clApp.rembg.main(save_dir=save_dir)


        return render_template('upload.html',  resultname = resultname, filename=filename, enable_process=True)
    else:
        return redirect(request.url)


if __name__ == '__main__':
    clApp = ClientApp()
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080) #AWS