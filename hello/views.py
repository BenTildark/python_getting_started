import os
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
	# first_name = input("Please enter your first name: ")

	# times = int(os.environ.get('TIMES',3))
	# return HttpResponse('Hello {}, welcome to python.'.format('Michael') * times)

	# r = requests.get('http://httpbin.org/status/418')
	# print(r.text)
	# return HttpResponse('<pre>' + r.text + '</pre>')
	return render(request, 'python_twitter_tweets.html')	
    #return HttpResponse('Hello from Python!')
    #return render(request, 'ash.html')
    #return render(request, 'index.html')
    # return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

