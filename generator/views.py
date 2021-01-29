from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.


def home(request):
	return render(request, 'generator/index.html', {'Name' : 'Ramshiv'})

def password(request):

	pwd_len = int(request.GET.get('length'))

	if  int(pwd_len) != 0 :
		pwd_len = int(request.GET.get('length'))
	else:
		pwd_len = random.randint(8,15)


	pwd = ''
	low_char = string.ascii_lowercase
	up_char = string.ascii_uppercase
	sp_char = string.punctuation

	meth = random.randint(0,2)

	print(pwd_len)

	for _ in range(1,pwd_len):

		if meth == 0:
			pwd+= random.choice(low_char) + random.choice(up_char) + random.choice(sp_char)
		elif meth == 1:
			pwd+= random.choice(up_char) + random.choice(sp_char) + random.choice(low_char)
		elif meth == 2:
			pwd+= random.choice(up_char) + random.choice(sp_char) + random.choice(low_char)
		else:
			pwd+= random.choice(sp_char) + random.choice(up_char) + random.choice(low_char)

	if pwd_len != len(pwd):
		pwd = pwd[0:pwd_len]
	else:
		pass

	return render(request, 'generator/password.html', {'password': pwd , 'pwd_len': pwd_len})

def about(request):

	return render(request, 'generator/aboutme.html')
