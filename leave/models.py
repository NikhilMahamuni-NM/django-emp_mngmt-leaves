from django.db import models

from django.contrib.auth.models import User

#Email Field
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

#First_Name Field
User._meta.get_field('first_name').blank = False
User._meta.get_field('first_name').null = False

#Last_Name Field
User._meta.get_field('last_name').blank = False
User._meta.get_field('last_name').null = False


# Create your models here.
class Profile(models.Model):
    emp = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank = True)
    gender = models.CharField(max_length=50, blank = True, choices=(
        ('Male', 'Male'),
        ('Female', 'Female')
    ))
    mob_no = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=200, blank=True)
    leaves_avai = models.CharField(max_length=2)


    def __str__(self):
        return str(self.emp)

class Leave(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = None)
    full_name = models.CharField(max_length=100)
    leaves_avai = models.CharField(max_length=2)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    total = models.CharField(max_length=2)
    description = models.TextField()
    applied_on = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    approval = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=120, blank=True, null=True)
    approval_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.full_name) + " | " + str(self.start_date)
    

