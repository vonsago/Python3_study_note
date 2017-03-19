from urllib.request import urlopen

def read_text():
	quotes = open(r"D:\Python3\myCode\test.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(tex_to_check):
	con = urlopen("http://www.wdylike.appspot.com/?q="+tex_to_check)
	url_output = con.read()
	printf(url_output)
	con.close()

read_text()


