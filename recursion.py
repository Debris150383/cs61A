from operator import sub,mul
def make_anonymous_factorial():
	return (lambda f: lambda x: f(f,x)) (lambda f,x: 1 if x == 1 else mul(x, f(f, sub(x, 1))


def count_change(total):
	
	def count_partitions(n,m):
		if n == 0
			return 1
		elif n < 0:
			return 0
		elif m == 0:
			return 0
		else:
			return count_partitions(n-m,m) + count_partitions(n,m//2)
	return count_partitions(total,round(math.log2(total)**2)

def composer(func=lambda x: x)
	
	def func_adder(g):
		h = lambda x:func(g(x))
		return composer(h)
	return func,func_adder
