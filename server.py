from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'the secret is between us'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    print('Request form - ', request.form)
    print('Hobbies - ', request.form.getlist('hobby'))
    session['name'] = request.form['name']
    session['gender'] = request.form['gender']
    session['hobby'] = request.form.getlist('hobby')
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')


@app.route('/results')
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)
