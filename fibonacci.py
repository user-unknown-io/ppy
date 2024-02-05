def Fibonacci(term:int)->list:
	  val = []
	  f_ = 0
	  s_ = 1
	  n_ = f_ + s_
	  val.append(f_)
	  val.append(s_)
	  for i in range(2,term+1):
		    val.append(n_)
		    f_ = s_
		    s_ = n_
		    n_ = f_ + s_
	  return val

if __name__=="__main__":
  	t_ = int(input("Enter Sequence Terms:\n"))
  	r_ = Fibonacci(t_)
  	print(r_)	
