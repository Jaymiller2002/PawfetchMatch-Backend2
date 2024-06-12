from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True)  # Optional bio field
    image = models.ImageField(upload_to='images/', blank=True, null=True)  
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listing')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recieved_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'Message from {self.sender.username} to {self.receiver.username} at {self.timestamp}'


