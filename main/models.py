from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Client(models.Model):
   
    CONTACT = '1'
    POTENTIAL = '2'
    PAYING = '3'
    LOST = '4'
    CLIENT_STATUS_CHOICES = [
        (CONTACT, 'Contact'),
        (POTENTIAL, 'Potential'),
        (PAYING, 'Paying'),
        (LOST, 'Lost')
    ]


    client_name = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=CLIENT_STATUS_CHOICES, default=CONTACT)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=200)
    position = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    mobile_phone_number = models.CharField(max_length=20)
    website = models.URLField(max_length=200)
    description = RichTextField('Description', default='')
    avatar = models.ImageField(upload_to='avatar/photos', default='')

    def __str__(self):
        return (self.client_name)