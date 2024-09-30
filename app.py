from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line
import os

def hello_world(request):
    return HttpResponse("Hello, World!")

urlpatterns = [
    path('', hello_world),
]

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello_world_app.settings")
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])
