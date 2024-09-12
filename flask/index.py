from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    tmp = 'index.html'
    if request.method == 'POST':
        name = request.form['name']
        print(name)
    return render_template(tmp)

@app.route('/greeting', methods=['POST'])
def greeting():
    name = request.form['name']
    print(name)
    return render_template('greeting.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
