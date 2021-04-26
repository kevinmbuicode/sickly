from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#a in this functionalities represent "act or action" in full thus a1 means act 1 or action 1
def index(request):
	return render(request, "superbody/base.html", {})

def a1(request):
	return HttpResponse("This is the other page for confirmation")

def diet(request):
	return render(request, "superbody/diet.html", {})

def contact(request):
	return render(request, "superbody/contact.html", {})

def about(request):
	return render(request, "superbody/about.html", {})

def thankyou(request):
	return render(request, "superbody/thankyou.html", {})