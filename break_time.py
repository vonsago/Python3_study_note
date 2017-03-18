import time
import webbrowser

total_break = 3
break_count = 0

print("Start")
while (break_count<total_break):
	time.sleep(2)
	webbrowser.open("https://github.com")
	break_count+=1