from flask import Flask, render_template, request
import my_functions
from colorama import Fore, Back, Style


app = Flask(__name__)

print(Fore.GREEN + 'Loading...')
print(Style.RESET_ALL)

my_fact = my_functions.get_fact()
my_quote = my_functions.get_qoute()[0]
author = my_functions.get_qoute()[1]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/recreation')
def recreation():
    link = my_functions.get_youtube_vid()
    return render_template('recreation.html', fact = my_fact, quote = my_quote, source = link)

@app.route('/reminders')
def reminders():
    return render_template('reminders.html')

@app.route('/timetable')
def timetable():
    return render_template('timetable.html')

if __name__ == '__main__':
    app.run(debug=True)
