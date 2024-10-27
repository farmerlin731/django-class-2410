# Create your views here.
from django.http import HttpResponse


def message_view(request):
    return HttpResponse("Hello Farmer! :)")


# Url example: http://localhost:8000/say-hello/?name=jack
def say_hello(request):
    get_params = request.GET
    name = get_params.get("name", "unknown")
    return HttpResponse(f"Hello {name}")
