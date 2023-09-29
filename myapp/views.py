from django.http import HttpResponse

# Create your views here.

# Primera funcion para mandar un hello world al front
# desde aqui hariamos las funciones para llamar a AFIX y mostrar la respuesta al front
def hello(request):
    return HttpResponse("<h1>Hello World<h1>")

def about(request):
    return HttpResponse("<h1>About<h1>")