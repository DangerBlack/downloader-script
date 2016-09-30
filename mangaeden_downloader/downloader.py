# -*- coding: utf-8 -*-
'''
This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/


    RUNNING:
    python3 downloader.py
'''
import requests
from xml.dom.minidom import parse
import xml.dom.minidom
import re
import urllib


FOLDER='save/'
name='MANGA_NAME'
chapter_max = 84
num_max = 250

def downloader(name,chapter,num):
	url='http://www.mangaeden.com/en/it-manga/'+name+'/'+str(chapter)+'/'+str(num)+'/'

	res = requests.get(url)

	payload=str(res.text)
	init=payload.find('1200: "')+len('"1200": "')
	fine=payload.find('"',init+1)
	img_url = payload[init:fine]
	print(img_url)
	
	img_url = "http://"+img_url
	
	extension = 'jpg'
	
	file_name = FOLDER+name+'-'+str(chapter)+'-'+str(num)+'.'+extension
	with urllib.request.urlopen(img_url) as response, open(file_name, 'wb') as out_file:
		data = response.read() # a `bytes` object
		out_file.write(data)


def downloadALl(name,chapter_max,num_max):
	for chapter in range(83,chapter_max):
		for num in range(1,num_max):
			try:
				print(str(chapter)+" - "+str(num))
				downloader(name,chapter,num)
			except Exception as e :
				print(e)
				pass	


downloadALl(name,chapter_max,num_max)
