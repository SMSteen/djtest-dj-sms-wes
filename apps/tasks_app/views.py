from django.shortcuts import HttpResponse
from django.core import serializers
from .models import Person, Task
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.body)
        # POST data from Angular comes in as a bytestring, so we need to decode it, and parse the JSON data
        formData = json.loads(request.body.decode())
        # now we can use the decoded formData just as we would request.POST
        task = Task.objects.create(title=formData['title'], description=formData['description'])
        # and we need to serialize the data and send it back via HTTPResponse
        # serializers only work on iterable datasets (i.e. a queryset) -- since our create method only returns the object, we could
            # 1 - make a new call to our database for the last task that was just created OR
            # 2 - make our task an iterable by wrapping it inside brackets []
        data = serializers.serialize("json", [task], indent=2, use_natural_foreign_keys=True)
        return HttpResponse(data, content_type="application/json", status=200)
    else:  # dealing with a GET, so get the list of tasks, serialize them into JSON and send them back
        data = serializers.serialize("json", Task.objects.all(), indent=2, use_natural_foreign_keys=True)
        return HttpResponse(data, content_type="application/json", status=200)

def show(request, task_id):
    data = serializers.serialize("json", Task.objects.filter(id=task_id), indent=2, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type="application/json", status=200)

def destroy(request, task_id):
    print('hit the destroy method, using a DELETE')
    del_task = Task.objects.get(id=task_id)
    # we need to serialize the task to send back in our response BEFORE we delete the task
    data = serializers.serialize("json", [del_task], indent=2, use_natural_foreign_keys=True)
    # let's clear any relationships before we delete it, just as a precaution
    del_task.assigned.clear()
    # now we can go ahead and delete
    del_task.delete()
    return HttpResponse(data, content_type="application/json", status=200)

def index_people(request):
    data = serializers.serialize("json", Person.objects.all(), indent=2)
    return HttpResponse(data, content_type="application/json", status=200)