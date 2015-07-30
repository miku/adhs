#!/usr/bin/env python
from flask import Flask, request, render_template
from flask.ext.cors import CORS
import adhocsparql
from adhocsparql.response import get_response
import argparse
import jinja2
import os
import rdflib

# command line parameters
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-p', '--port', default=5000, type=int)
parser.add_argument('-i', '--input', default='guess', choices=[
        'html',
        'hturtle',
        'mdata',
        'microdata',
        'n3',
        'nquads',
        'nt',
        'rdfa',
        'rdfa1.0',
        'rdfa1.1',
        'trix',
        'turtle',
        'xml'
    ], help='Optional input format')

args = parser.parse_args()

# new graph
g = rdflib.Graph()

# parse file into graph
with open(args.file, 'r') as fi:
    if args.input == 'guess':
        fo = rdflib.util.guess_format(args.file)
    else:
        fo = args.input

    g.parse(fi, format=fo)

# set up a micro service using flash
app = Flask(__name__, static_url_path='')
cors = CORS(app)

# allow templates in multiple places
choice_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader([os.path.join(os.path.dirname(adhocsparql.__file__),
                                          'templates')]),
])

app.jinja_loader = choice_loader

@app.route("/sparql", methods=['GET'])
def sparql():
    if 'query' in request.args:
        if 'output' in request.args:
            output = request.args['output']
        else:
            output = 'json'

        query = request.args['query']
        qres = g.query(query)
        return get_response(qres, output)
    else:
        return render_template('sparql.html', src=args.file, port=request.host)

if __name__ == "__main__":
    app.run(port=args.port)

