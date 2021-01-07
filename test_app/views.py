from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def orange(request):
	student = {'name1':'''pplies HTML escaping to a string
	 (see the escape filter for de
	 tails). This fil''', 'name2':'y', 'name3':'zaaa'}
	return render(request, 'test.html', {'t':student} )

def apple(request):
	return HttpResponse("Hello, Apple")