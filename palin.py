import time

def ispalindrome(n):
	s = list(str(n))
	l = len(s)
	i = 0
	
	while True:
		if i >= l - 1 - i:
			break
		elif s[i] != s[l - 1 - i]:
			return False
		i += 1
	return True

t = int(input())
ip = []
for i in range(t):
	ip.append(int(input()) + 1)

start = time.time()

for n in ip:
	while True:
		if ispalindrome(n):
			print(n)
			break
		else:
			n += 1

end = time.time()
print(f"Execution Time: {(end - start)*1000} ms")