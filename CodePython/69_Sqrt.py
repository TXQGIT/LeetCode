
def mySqrt(x):
	r = x
	while int(r)*int(r) > x:
	    r = (r + x/r) / 2
	return int(r)

if __name__=='__main__':
	print(mySqrt(5))
	print(mySqrt(8))
	print(mySqrt(17))