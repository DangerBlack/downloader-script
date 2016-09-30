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
name='TUMBLR_NAME'

num = 50
start = 0

def downloader(name,num,start):
	url='http://'+name+'.tumblr.com/api/read?type=photo&num='+str(num)+'&start='+str(start)

	res = requests.get(url)

	pattern = re.compile('<photo\-url max\-width="1280">[A-Za-z:0-9_/\.]*')
	matching = pattern.findall(res.text)
	padding=len('<photo-url max-width="1280">')

	counter=0
	for m in matching:
		img_url=m[padding:]
		img=requests.get(img_url)
		extension=img_url.split('.')[-1]
		urllib.urlretrieve(img_url,FOLDER+str(counter)+'_img_'+str(start)+'.'+extension)
		counter=counter+1
	
	return counter

while(downloader(name,num,start)>0):
	start=start+num
	
