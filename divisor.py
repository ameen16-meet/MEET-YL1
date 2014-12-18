n= input("enter your number")

def divfunc(n): 
	i=1
	while (i<int(n)+1):
	    
	    if (int(n)%i==0):
	    	print(i)
	    i=i+1

divfunc(n)