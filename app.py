#coding:utf-8
from flask import *
import sys,os,time,random
import hashlib,re
reload(sys)
sys.dont_write_bytecode = True
sys.setdefaultencoding('utf-8')
workpath = os.path.dirname(os.path.abspath('app.py'))
sitespath = os.path.join(workpath,'sites')
if sitespath not in sys.path:
	sys.path.insert(0,sitespath)
import sites

app = Flask("intsearch")

@app.route('/',methods=['GET','POST'])
def Index():
	return sites.index.Run()

app.secret_key = '你知道也没事反正我不用这个'
if __name__ == "__main__":
	app.run()
