#-*- coding=utf-8 -*-
#下载一张图片

# with open as 的详细教程可参考
# http://www.cnblogs.com/ymjyqsx/p/6554817.html
'''
import urllib.request

request = urllib.request.Request('http://placekitten.com/g/500/600')

response = urllib.request.urlopen(request)

cat_image = response.read()

#见上文注释， 打开文件，并写入
with open('cat_500*600.jpg', 'wb') as f:
	f.write(cat_image)
'''


#-------------------------------------------

import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容:')

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'
#添加header 参数，模仿浏览器访问
header = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
data = {
	'i':content,
	'type':'AUTO',
	'smartresult':'dict',
	'doctype':'json',
	'xmlVersion':'1.6',
	'ue':'UTF-8',
	'typoResult':'true'
}
data = urllib.parse.urlencode(data).encode('utf-8')
# 3个参数， URL， 请求参数， header参数
response = urllib.request.urlopen(url, data, header)
html = response.read().decode('utf-8')

# print (html)
#得到的是json 字符串， 通过 loads方法
#将json字符串转成 字典
resultDic = json.loads(html)
finalResult = resultDic['translateResult'][0][0]['tgt']
print ('翻译结果: %s' %finalResult)


