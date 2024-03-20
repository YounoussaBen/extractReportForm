from django.db import models

class Application(models.Model):
    # User details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    # Reason for applying
    reason = models.TextField()

    # Choices for reason (optional)
    REASON_CHOICES = (
        ('employment', 'Employment Background Check'),
        ('visa', 'Visa Application'),
        ('volunteer', 'Volunteer Work'),
        ('other', 'Other'),
    )
    reason_type = models.CharField(max_length=20, choices=REASON_CHOICES, blank=True)

    # Optional file upload
    documents = models.FileField(upload_to='uploads/', blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Application for {self.get_reason_display()}"
