#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
__title__ = 'UrlManager'
__author__ = 'Mr.X'
__mtime__ = '2017/8/11'
'''


class UrlManager(object):
	def __init__(self):
		self.newPages = set()
		self.oldPages = set()
		self.newItems = set()
		self.oldItems = set()
		self.newImages = set()
		self.oldImages = set()

	def HasNewPageUrl(self):
		return len(self.newPages) != 0

	def GetNewPageUrl(self):
		if self.HasNewPageUrl():
			pageUrl = self.newPages.pop()
			return pageUrl
		else:
			return None

	def AddNewItemUrl(self, link):
		if link is None:
			return
		if link not in self.newItems and link not in self.oldItems:
			self.newItems.add(link)

	def AddOldPageUrl(self, pageUrl):
		if pageUrl is None:
			return
		if pageUrl not in self.newPages and pageUrl not in self.oldPages:
			self.oldPages.add(pageUrl)

	def HasNewItemUrl(self):
		return len(self.newItems) != 0

	def GetNewItemUrl(self):
		if self.HasNewItemUrl():
			itemUrl = self.newItems.pop()
			return itemUrl
		else:
			return None

	def AddNewImageUrl(self, link):
		if link is None:
			return
		if link not in self.newImages and link not in self.oldImages:
			self.newImages.add(link)

	def AddOldItemUrl(self, itemUrl):
		if itemUrl is None:
			return
		if itemUrl not in self.newItems and itemUrl not in self.oldItems:
			self.oldItems.add(itemUrl)

	def HasNewImageUrl(self):
		return len(self.newImages) != 0

	def GetNewImageUrl(self):
		if self.HasNewImageUrl():
			imageUrl = self.newImages.pop()
			return imageUrl
		else:
			return None

	def AddOldImageUrl(self, imageUrl):
		if imageUrl is None:
			return
		if imageUrl not in self.newImages and imageUrl not in self.oldImages:
			self.oldImages.add(imageUrl)
