from django.shortcuts import render

# Create your views here.
def index(request):
    whatsapp_url = 'https://api.whatsapp.com/send/?phone=%2B523535350783&text&type=phone_number&app_absent=0'
    return render(request, 'index.html', { 'whatsapp': whatsapp_url })
