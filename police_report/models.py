from django.db import models

class Application(models.Model):
    # User details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    reason = models.TextField()

    documents = models.FileField(upload_to='uploads/', blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Application for {self.get_reason_display()}"
