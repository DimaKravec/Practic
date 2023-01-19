def whos_first(P1, P2):
	shoot = P1.find('Bang!') - P2.find('Bang!')
	if shoot < 0:
		return 'P1 wins'
	elif shoot > 0:
		return 'P2 wins'
	else:
		return 'tie'
P1 = input("Activate shot P1:")
P2 = input("activate shot P2:")
print(whos_first(P1,P2))