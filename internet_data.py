import urllib2


webUrl = urllib2.urlopen("http://joemarini.com")

print("Result code:", str(webUrl.getcode()))
