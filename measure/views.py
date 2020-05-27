from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def measure(request):
    return render(request, "measure/measure.html")

def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        longitud = request.GET['longitud']
        latitud = request.GET['latitud']
        area = request.GET['area']


        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'cm', 'value': value,'longitud':longitud,'latitud':latitud,"area":area}
            response = requests.post('http://pi1-eafit-jmesapa1.azurewebsites.net/ultrasonic/', args) 

            # Convierte la respuesta en JSON
            measure_json = response.json()

            	
            print(measure_json)

    # Realiza una petición GET al Web Services
    response = requests.get('http://pi1-eafit-jmesapa1.azurewebsites.net/ultrasonic/')
    
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})