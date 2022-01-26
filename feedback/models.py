from django.db import models
from django.contrib.auth import get_user_model

class Feedback(models.Model) :
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now = True, auto_now_add = False)
    updated = models.DateTimeField(auto_now = False, auto_now_add = True)
    author = models.ForeignKey(get_user_model(), default = name, on_delete = models.CASCADE)

    def __str__(self) :
        return self.name


