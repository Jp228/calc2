from flask import Flask, render_template, flash

"""Flash Massage"""
app = Flask(__name__)
@app.route('/')
def flash_massage():
    flash("flash test!!")
    return