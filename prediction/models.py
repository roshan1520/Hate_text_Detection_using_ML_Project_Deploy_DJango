# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    



from django.db import models
from django.utils.timezone import now

class Prediction(models.Model):
    text = models.TextField()                         # Input text
    prediction = models.CharField(max_length=50)      # Predicted label
    confidence = models.FloatField()                  # Confidence score
    created_at = models.DateTimeField(default=now)    # Timestamp

    def __str__(self):
        return f"{self.text} -> {self.prediction} ({self.confidence:.2f})"