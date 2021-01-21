import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

UPLOAD_PATH = '/Users/Silvak/Desktop/Program/javascript/nova_imageUp/static/img/uploads'
ALLOWED_EXTENSIONS = {'PNG', 'JPG', 'JPEG', 'GIF'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


def allow_image(filename):
    if not '.' in filename:
        return False
    ext = filename.rsplit('.',1)[1]

    if ext.upper() in app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return True
    else:
        return False


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if request.files:

            image = request.files['image']

            if image.filename == '':
                print('image must have a filename')
                return redirect(request.url)
            
            if not allow_image(image.filename):
                print('that image extension is not allowd')
                return redirect(request.url)

            else:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            print('image saved')
            return redirect(request.url)

    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True, port=4000)