import os
from flask import Flask, render_template, request, redirect
from flask.helpers import flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/Silvak/Desktop/Program/javascript/nova_imageUp/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))

        if request.files:
            image = request.files['image']
            image.save(os.path.join(app.config['IMAGES_UPLOADS'], image.filename))
            print('Image saved') # mandar valor en % a el template en ves del texto
            print(image)
            return redirect(request.url)

    return render_template('index.html', msm= 'aaaa')



if __name__ == '__main__':
    app.run(debug=True, port=4000)