#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
__title__ = 'Main.py'
__author__ = 'Mr.X'
__mtime__ = '2017/8/11'
'''
import HtmlDownloader
import HtmlOutputer
import HtmlParser
import UrlManager


class MainSearcher(object):
	def __init__(self):
		# 爬取深度(页数)
		self.maxPageDeep = 1
		# 地址管理器
		self.UrlsManager = UrlManager.UrlManager()
		# 下载器
		self.Downloader = HtmlDownloader.HtmlDownloader()
		# 解析器
		self.Parser = HtmlParser.HtmlParser()
		# 输出器
		self.Outputer = HtmlOutputer.HtmlOutputer()

	def craw(self, root_url):
		curPageDeep = 1

		# 下载根节点 解析页地址
		# try:
		self.UrlsManager.newPages.add(root_url)
		htmlCode = self.Downloader.DownloadHtmlCode(root_url)
		Pages = self.Parser.ParsePages(htmlCode)
		self.UrlsManager.newPages = Pages
		# except:
		#	print('下载或解析根节点失败')

		# 下载页节点 解析项目地址
		try:
			while self.UrlsManager.HasNewPageUrl():
				pageUrl = self.UrlsManager.GetNewPageUrl()
				htmlCode = self.Downloader.DownloadHtmlCode(pageUrl)
				itemLinks = self.Parser.ParseItems(htmlCode)
				for link in itemLinks:
					self.UrlsManager.AddNewItemUrl(link)
				self.UrlsManager.AddOldPageUrl(pageUrl)
				curPageDeep += 1
				if curPageDeep >= self.maxPageDeep:
					break
		except:
			print('下载页节点或解析项目节点失败')

		# 下载项目页 解析图片地址
		try:
			while self.UrlsManager.HasNewItemUrl():
				itemUrl = self.UrlsManager.GetNewItemUrl()
				print(itemUrl)
				htmlCode = self.Downloader.DownloadHtmlCode(itemUrl)
				imageLinks = self.Parser.ParseImages(htmlCode)
				if imageLinks is not None:
					for link in imageLinks:
						self.UrlsManager.AddNewImageUrl(link)
					self.UrlsManager.AddOldItemUrl(itemUrl)
		except:
			print('下载项目节点或解析图片地址失败')

		# 下载图片
		try:
			counter = 0
			number = len(self.UrlsManager.newImages)
			while self.UrlsManager.HasNewImageUrl():
				counter += 1
				imageUrl = self.UrlsManager.GetNewImageUrl()
				print('No. %d of %d :' % (counter, number))
				self.Downloader.DownloadImage(imageUrl)
				counter += 1
				self.UrlsManager.AddOldImageUrl(imageUrl)
		except:
			print('下载图片失败')

		# 输出爬取结果
		self.Outputer.Output()


if __name__ == "__main__":
	root_url = "http://www.mimihhh.com/forumdisplay.php?fid=46"
	obj_searcher = MainSearcher()
	obj_searcher.craw(root_url)
