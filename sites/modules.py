#coding: utf-8
from flask import *

def ReturnJSON(data):
	return Response(json.dumps(data),mimetype='application/json')
