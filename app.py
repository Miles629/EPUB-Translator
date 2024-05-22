from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # 设置上传文件夹
app.config['ALLOWED_EXTENSIONS'] = {'epub'}  # 允许的文件扩展名

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        epub_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(epub_path)
        # temp_dir = request.form['temp_dir']
        # output_path = request.form['output_path']
        # write = True if request.form.get('write') == 'on' else False

        # 构造命令并运行Python脚本
        cmd = f"python your_script.py '{epub_path}' '{temp_dir}'  True"
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        return f"Result: {result.stdout}"
    else:
        return 'Invalid file type'

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
