from django.db import models
from django.forms import ModelForm

class Customer(models.Model):
    first_name = models.CharField(max_length=50,
                                  help_text="First Name")
    last_name = models.CharField(max_length=50,
                                 help_text="Last Name")
    
    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)

class Suite(models.Model):
    name = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name

class Booking(models.Model):
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    customer = models.ForeignKey(Customer)
    suite = models.ForeignKey(Suite)
    
    def __unicode__(self):
        return u'{} in {} on {}'.format(self.customer, self.suite, self.checkin_date)

class CustomerForm(ModelForm):
    class Meta:
        model = Customer

class SuiteForm(ModelForm):
    class Meta:
        model = Suite

class BookingForm(ModelForm):
    class Meta:
        model = Booking