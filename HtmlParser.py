#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
__title__ = 'HtmlParser'
__author__ = 'Mr.X'
__mtime__ = '2017/8/12'
'''
import re

from bs4 import BeautifulSoup


class HtmlParser(object):
	# 解析根节点 获取可爬取页地址集合
	def ParsePages(self, html):
		if html is None:
			return
		soup = BeautifulSoup(html, 'html.parser')
		pageUrls = self._getPageUrls(soup)
		return pageUrls

	def ParseItems(self, html):
		if html is None:
			return
		soup = BeautifulSoup(html, 'html.parser')
		itemUrls = self._getItemUrls(soup)
		return itemUrls

	def ParseImages(self, html):
		if html is None:
			return
		soup = BeautifulSoup(html, 'html.parser')
		imageUrls = self._getImageUrls(soup)
		return imageUrls

	def _getPageUrls(self, soup):
		urls = set()
		nodes = soup.find_all('a', class_="p_num")
		for node in nodes:
			pageUrl = node["href"]
			pageFullUrl = "http://www.mimihhh.com/" + pageUrl
			urls.add(pageFullUrl)
		return urls

	def _getItemUrls(self, soup):
		urls = set()
		nodes = soup.find_all('td', class_="f_title")
		for node in nodes:
			checker = node.find('div', class_="right").find('img', alt="本版置顶")
			if checker is None:
				itemNode = node.find('a', href=re.compile(r"viewthread\.php\?tid=\d{1,7}"))
				itemUrl = itemNode["href"]
				itemFullUrl = "http://www.mimihhh.com/" + itemUrl
				urls.add(itemFullUrl)
		return urls

	def _getImageUrls(self, soup):
		urls=set()
		checkNode=soup.find('a',href="http://www.ded22.com")
		if checkNode is not None:
			return
		nodes=soup.find('div',class_="t_msgfont").find_all('img')
		for node in nodes:
			imageUrl=node["src"].split('%')[0]
			urls.add(imageUrl)
		return urls
