from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greeting', methods=['POST'])
def greeting():
    name = request.form['name']
    return render_template('greeting.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
