import math
import random
import time

start = time.time()

alph     = 'абвґгдеєжзиіїйклмнорпстуфхцчшщьюя'
word     = 'індеферентність'

position = [alph.find(i) + 1 for i in word]

GCD      = lambda a, b: a if b == 0 else GCD(b, a % b)
toBinary = lambda x:    list(str(bin(x)))[2:][::-1] if x > 0 else list(str(bin(x)))[3:][::-1]
eiler    = lambda p, q: (p - 1) * (q - 1)

def randPrime(left, right):
	num = random.randint(left, right)
	for i in range(0, int(10 * math.log(num) + 3)):
		if isPrime(num):
			return num
		else:
			num += 1

def modPower(a, n, m):
	binX      = toBinary(n)
	binLength = len(binX)
	modd      = []
	result    = 1
	for i in range(1, binLength + 1):
		if i == 1:
			modd.append(a % m)
		else:
			modd.append((modd[i - 2] ** 2) % m)
	for i in range(0, binLength):
		if int(binX[i]) == 1:
			result *= modd[i]
	return result % m

def isPrime(n):
	for i in range(500):
		a = random.randint(1, n - 2)
		if GCD(a, n) != 1:
			return False
		if modPower(a, n-1, n) != 1:
			return False
	return True

def openKey(p, q):
	phi = eiler(p, q)
	t   = random.randint(round(phi/1048000), round(phi/8))
	if GCD(t, phi) == 1:
		return t
	return openKey(p, q)

def extEuclid(e, phi):
	a, b           = phi, e
	x0, x1, y0, y1 = 1, 0, 0, 1
	while b > 0:
		q      = math.floor(a / b)
		a, b   = b, a - b * q
		x0, x1 = x1, x0 - x1 * q
		y0, y1 = y1, y0 - y1 * q
	return abs(y0)

def init(left, right):
	p = randPrime(left, right)
	while 1:
		q = randPrime(left, right)
		if q != p:
			break
	n   = p * q
	phi = eiler(p, q)
	e   = openKey(p, q)
	d   = extEuclid(e, phi)
	while (e * d) % phi != 1:     
		e   = openKey(p, q)
		d   = extEuclid(e, phi)
	return n, e, d

def code(e, n):
	result = []
	for k in position:
		result.append(modPower(k, e, n))
	return result

def decode(d, n, coded):
	result = []
	for k in coded:
		result.append(modPower(k, d, n))
	return result

(n, e, d) = init(10**6, 10**7)
s         = 'N = \n{0}\nE = \n{1}\nD = \n{2}'.format(n,e,d)
coded     = code(e, n)
decoded   = [num for num in decode(d, n, coded)]
print(s, '\n\nOriginal: ', position, '\n\nCoded:')
for num in coded:
	print(num)
print('\nDecoded: ', decoded)

finish = time.time()
print('\n', finish-start)