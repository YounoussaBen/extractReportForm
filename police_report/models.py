from django.db import models

class Application(models.Model):
    # User details
    name = models.CharField(max_length=100)  # Combining first_name and last_name into a single field
    phone_number = models.CharField(max_length=20)
    occurrence_date_time = models.DateTimeField()
    address = models.TextField()

    # Lost Document details
    DOCUMENT_CHOICES = [
        ('passport', 'Passport'),
        ('drivers_license', "Driver's License"),
        ('ghana_card', 'Ghana Card'),
        ('voter_id_card', 'Voter ID Card'),
    ]
    lost_document = models.CharField(max_length=100, choices=DOCUMENT_CHOICES)
    other_document_details = models.CharField(max_length=100, blank=True)

    # Additional fields for document details
    issue_date = models.DateField()  # Date the document was issued
    expiry_date = models.DateField()  # Date the document expires
    identification_number = models.CharField(max_length=100)  # Unique identification number on the document

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - Application for {self.get_lost_document_display()}"
