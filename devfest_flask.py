from data import *
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
#from flask.ext.restful import reqparse

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG=True
    ))
app.config.from_envvar('DEVFEST_SETTINGS', silent=True)

#parser init
#parser = reqparse.RequestParser()
#parser.add_argument('summoner', type=str, required=True, help="Summoner cannot be blank")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['GET'])
def lookup():
    #if a get request is received, parse out the summoner from the url and return the record
    if request.method == 'GET':
        summ = request.args.get('summoner')
        return rec_gms_to_kda(summ)
    #args = parser.parse_args()
    #print args['summoner']
    #return rec_gms_to_kda(request.form['summoner'])
    return rec_gms_to_kda('lexwraith')
    #return render_template('lookup.html', records=test)


if __name__ == '__main__':
    app.run()
