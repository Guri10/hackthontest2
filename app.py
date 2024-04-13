from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['PROCESSED_FOLDER'] = 'processed/'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)