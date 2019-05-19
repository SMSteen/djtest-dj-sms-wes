from django.shortcuts import HttpResponse
from django.core import serializers
from .models import Person, Task

# Create your views here.
def index(request):
    if request.method == 'POST':
        print('trying to create a new task, so figure this out!')
        print(request.POST)
        return HttpResponse('add the task')
    else:  # dealing with a GET, so get the data
        data = serializers.serialize("json", Task.objects.all(), indent=2, use_natural_foreign_keys=True)
        return HttpResponse(data, content_type="application/json", status=200)

def show(request, task_id):
    data = serializers.serialize("json", Task.objects.filter(id=task_id), indent=2, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type="application/json", status=200)