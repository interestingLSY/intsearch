#coding: utf-8
from flask import *
import modules

def Search(q):
	ret = [
		{
			"title": "NOIp爆零记 - Doc_wu的博客 - CSDN博客",
			"description": "2017-6-3 · day 0 上午起来，眼睛一睁开就想起来要出发了，心里默默念：相信自己，相信自己... 早上不想颓，于是起来写板子，写着写着就发现近几年的",
			"link": "https://blog.csdn.net/Doc_wu/article/details/84194823"
		},
		{
			"title": "NOIp爆零记 - 社会稽 - 博客园",
			"description": "2019-3-6 · NOIp爆零记 这次NOIp又是一次伤心的回忆。。。全世界就我没AK。。。估计是个三等奖吧。 Day0 晚上到考场那边，复习了会儿图论，打了一点玄学数学就睡了。",
			"link": "https://www.cnblogs.com/shehuiji/p/10485804.html"
		},
		{
			"title": "元首NOIP爆零了！_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili",
			"description": "2018-4-1 · 最弱！毋庸置疑！但有时会做点小东西；不善交往，但还是很喜欢友谊魔法；迫切的想扩列，QQ：1830500378这回是真的",
			"link": "https://www.bilibili.com/video/av21511483"
		}
	]
	return modules.ReturnJSON(ret)
