from django.shortcuts import render
import requests
import json



def show_data(request):

    url = 'https://data.tampere.fi/data/api/action/datastore_search?resource_id=0747926f-1593-423f-b351-5fa2ae477eb4'
       
    response = requests.get(url)
    fielddata = response.json()
    fielddata = fielddata['result']
    fielddata = fielddata['records']
    data = []

    for field in fielddata:
        data.append(field)
    return render(request, 'kirjastot.html', {'fielddata' : data})
 

# Create your views here.
