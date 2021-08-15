from flask import Flask, render_template, request
import randfacts

# Our Functions

def get_fact():
    x = randfacts.getFact(True)
    return x

# Flask-------------

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')


print(get_fact())