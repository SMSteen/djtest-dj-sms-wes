from django.db import models

# Create your models here.
class PersonManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name):
        return self.get(first_name=first_name, last_name=last_name)

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    objects = PersonManager()

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

    def natural_key(self):
        return(f'{self.first_name} {self.last_name}')

    # class Meta:
    #     unique_together = (('first_name', 'last_name'),)


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default='')
    assigned = models.ManyToManyField(Person, related_name='tasks')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Task {self.id} - {self.title}'

