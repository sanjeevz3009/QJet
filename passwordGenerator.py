import string
import random

def pw_gen(size, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(8))