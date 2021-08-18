from flask import Flask, render_template, request
import my_functions


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/recreation')
def recreation():
    return render_template('recreation.html')

@app.route('/reminders')
def reminders():
    return render_template('reminders.html')

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')

if __name__ == '__main__':
    app.run(debug=True)