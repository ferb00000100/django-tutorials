from django.shortcuts import render, get_object_or_404, redirect
# from django.forms import modelform_factory
# from .models import rest_tut
# from django.conf import settings
import requests
import json

def home(request):
	count = 0
	endpoint = 'https://console.rumble.run/api/v1.0/org/assets?search=3389'
	headers = { 'Content-Type':'application/json', 'Authorization': 'Bearer OTD4FCB9535F2F4841A1DDAB1F952A'}
	response = requests.get(endpoint, headers=headers)
	instance_data = json.loads(response.text)
	# print(instance_data[0]['addresses'])
	results = {}
	count	 = 0
	try:
		while True:
			# return render(request, 'rest_tut/searchResults.html',
			results = {
				'id':instance_data[count]['id'],
				'addresses': instance_data[count]['addresses'],
				'detected_by': instance_data[count]['detected_by'],
				'names': instance_data[count]['names'],
				'services': instance_data[count]['services']
			}
			count +=1
			# })
	except:
		print('ERROR')
	
	return render(request, 'rest_tut/searchResults.html',{'results': results})
