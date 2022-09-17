R = "\033[1;41m"
w = "\033[0m"
try:
		num=eval(input("Enter number:"))
		duration =eval(input("Enter duration:"))
		for i in range (duration+1):
			if i == 0:
				continue
			print (num,"x",i,"=",num*i)
except Exception as e:
		print (R+"ERROR!!",w,e)
		