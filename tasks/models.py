from django.db import models
from django.contrib.auth.models import User

class MyModel(models.Model):
    # Определение поля id типа AutoField как первичного ключа
    id = models.AutoField(primary_key=True)
    # Определение поля phone типа CharField с максимальной длиной в 20 символов
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.phone
    
class Task(models.Model):
    
    title = models.CharField(max_length=200)
    
    STATUS_CHOICES =[
        ('new', '🆕New🆕'),
        ('in_progress', '👨‍💻In Progress👨‍💻'),
        ('closed', '🔒Closed🔒'),
        ('waiting', '💤Waiting💤')
    ]
    
    PRIORITY_CHOICES =[
        ('critical', '🔥Critical🔥'),
        ('high', '🫨Important🫨'),
        ('medium', '🍃Medium🍃'),
        ('low', '🤓Low🤓')
    ]
    status = models.CharField(choices=STATUS_CHOICES, default="New")
    
    description = models.CharField(blank=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, default="medium")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    