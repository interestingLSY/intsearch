#coding:utf-8
from flask import *

def Run():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		return redirect('https://cn.bing.com/search?q=%s'%request.form['q'])
