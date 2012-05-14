from django.db import models
from django.forms import ModelForm

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50,
                                  help_text="First Name")
    last_name = models.CharField(max_length=50,
                                 help_text="Last Name")
    
    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_Name)

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        