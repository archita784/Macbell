from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Signup(models.Model):
    username=models.CharField(max_length=50)
    emailaddress = models.EmailField(max_length=50, primary_key=True)
    password = models.CharField(max_length=20)
    iam_choices = (
        (' Entrepreneur   ', 'Entrepreneur'),
        (' Businessman',' Businessman'),
        ('Investor','Investor'),
        ('Freelancers','Freelancers'),
        ('Students','Students'),
        (' student entrepreneur',' student entrepreneur'),
    )
    iam=models.CharField(max_length=50,choices=iam_choices)
    profile_choices=(
        ('  startup idea  , startup , join startup as a cofounder, join startup as a team member ',  'startup idea  , startup , join startup as a cofounder, join startup as a team member' ),
        (' company  /firm , franchisee  , Distributors   , wholesalers  ,  investor ',' company  /firm , franchisee  , Distributors   , wholesalers  ,  investor '),
        ('investor','investor'),
        ('Freelancers','Freelancers'),
        ('Internship/ job seeker  / freelancing work  / all entrepreneur categories ',' Internship/ job seeker  / freelancing work  / all entrepreneur categories '),
        (' all categories of students and entrepreneur ',' all categories of students and entrepreneur'),
    )

    profile=models.CharField(max_length=100,choices=profile_choices)
    lookingfor_choice=(
        (' Entrepreneur   ', 'Entrepreneur'),
        (' Businessman',' Businessman'),
        ('Investor','Investor'),
        ('Freelancers','Freelancers'),
        ('Students','Students'),
        (' student entrepreneur',' student entrepreneur'),
    )
    lookingfor=models.CharField(max_length=50,choices=lookingfor_choice)
    profilepic = models.ImageField(upload_to='images')
    address = models.TextField(max_length=100)
    contactno = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    objects = models.Manager()

class Login(models.Model):
    userid = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=20)
    usertype=models.CharField(max_length=20)
