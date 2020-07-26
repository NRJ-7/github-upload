
t = int(input())
ip = []
for i in range(t):
	ip.append(list(input()))

for algexp in ip:
	length = len(algexp)
	popexp = False
	expstack = []
	rpn = ""
	while True:
		if len(algexp) == 0:
			break

		c = algexp.pop(0)
		if c.isalpha():
			rpn += c
		elif c == '(':
			continue
		elif c == ')':
			rpn += expstack.pop()
		else:
			expstack.append(c)
			popexp = True
	print(rpn)
	