from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/admin')
def admin_login():
    return render_template('admin_login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        model = request.form['model']
        image = request.files['image']
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Later we'll save this to MongoDB
        return redirect(url_for('dashboard'))
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)
