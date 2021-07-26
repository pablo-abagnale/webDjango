from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail 
from django.conf import settings

# Create your views here.


def inicio(request):
    if request.method == "POST":
        
        asunto = request.POST['asunto']
        mensaje = request.POST['nombre'] + '  ' + request.POST['mensaje'] + '  ' + request.POST['mail']
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = ['pablo.e.abagnale@gmail.com'] 
        send_mail(asunto,mensaje,email_from,recipient_list)
        return render(request, 'saludo.html')
    
    return render (request,'index.html')
def barra(request):
    return render (request,'barra.html')
def saludo(request):
    return render (request,'index.html')
