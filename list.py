def reverse_iter(lst):
	ans = []
	for x in lst:
		ans = [x] + ans
	return ans

def reverse_recursive(lst):
	if not lst:
		return []
	return [lst[-1]] + reverse_recursive(lst[:-1])

def add_chars(w1,w2):
	if len(w1) == 0:
		return w2
	if w1[0] == w2[0]
		return add_chars(w1[1:],w2[1:])
	else:
		return w2[0] + add_chars(w1,w2[1:])

def riffle(deck):
    m = len(deck) // 2
    return [deck[k//2 + m * (k%2)] for k in range(len(deck))]
