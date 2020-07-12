from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=9ED3DE96-A3D5-4C5D-BDA4-543738589646")

	try:
		api=json.loads(api_request.content)
	except Exception as e:
		api= "Error"
	return render(request,'home.html',{'api':api})


def about(request):
	return render(request,'about.html',{})