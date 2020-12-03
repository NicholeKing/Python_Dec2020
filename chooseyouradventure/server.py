from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/one')
def run():
    return render_template('run.html')

@app.route('/two')
def fight():
    return render_template('fight.html')

@app.route('/die')
def die():
    return render_template('death.html')

@app.route('/chase')
def chase():
    return render_template('chase.html')

@app.route('/won')
def won():
    return render_template('won.html')

@app.route('/bite')
def bite():
    return render_template('bite.html')

@app.route('/dinner')
def dinner():
    return render_template('dinner.html')

@app.route('/propose')
def propose():
    return render_template('propose.html')

@app.route('/fall')
def fall():
    return render_template('fall.html')

@app.route('/help')
def help():
    return render_template('help.html')

app.run(debug=True)