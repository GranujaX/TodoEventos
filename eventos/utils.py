# views.py
import requests
from django.http import JsonResponse

def get_data_from_api(request):
    url = "http://34.170.152.87/api/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        return data
    else:
        # Manejar el caso en que la solicitud a la API falla
        return JsonResponse({'error': 'Failed to fetch data from API'}, status=500)
