#import library 
import pyshorteners
#creating object
s=pyshorteners.Shortener()
#type the url
url = "https://www.youtube.com/watch?v=mvsiuLzpx2E"
#print the shortend url
print(s.tinyurl.short(url))