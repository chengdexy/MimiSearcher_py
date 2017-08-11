#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
__title__ = 'HtmlDownloader'
__author__ = 'Mr.X'
__mtime__ = '2017/8/12'
'''
from os.path import basename
from urllib import request

import sys

import os


class HtmlDownloader(object):
	def DownloadHtmlCode(self, url):
		if url is None:
			return
		response = request.urlopen(url)
		if response.getcode() != 200:
			return None
		return response.read()

	def DownloadImage(self, url):
		if url is None:
			return
		filename = basename(url)
		if not os.path.exists('images'):
			os.mkdir('images')
		try:
			response = request.urlopen(url)
			buffer = response.read()
			f = open('images\\'+filename, 'wb')
			f.write(buffer)
			print('已下载:%s' % filename)
		except:
			print('Pass a bad image url: %s' % url)
