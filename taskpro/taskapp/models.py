from django.db import models

# Create your models here.

class CustomUser(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Mobile = models.CharField(max_length=10)
    ID = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'CustomUser'

    def __str__(self):
        return f'{self.Name} - {self.Email} - {self.Mobile}-{self.ID}'

Task_choice = (
    ("Pending", "pending"),
    ("Done", "done"),
)

class Task(models.Model):
    task_details = models.TextField(max_length=100)
    task_type = models.CharField(max_length=100, choices=Task_choice)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    answer = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return str(self.task_details)
    
    class Meta:
        ordering =['id']

    