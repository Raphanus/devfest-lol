
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG=True
    ))
app.config.from_envvar('DEVFEST_SETTINGS', silent=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
