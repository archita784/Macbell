from django.shortcuts import render,redirect,reverse
from .models import Signup,Login
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')
def custreg(request):
    username=request.POST['username']
    emailaddress = request.POST['emailaddress']
    password=request.POST['password']
    iam=request.POST['iam']
    profile=request.POST['profile']
    if 'profilepic' in request.POST:
        profilepic = request.POST.get('profilpic')
        Signup.profilepic.url = profilepic

    lookingfor=request.POST['lookingfor']
    address=request.POST['address']
    contactno=request.POST['contactno']
    country=request.POST['country']
    city=request.POST['city']
    li = Signup(username=username,emailaddress=emailaddress, password=password,iam=iam,profile=profile,profilepic=profilepic,lookingfor=lookingfor,address=address,contactno=contactno,country=country,city=city)
    li.save()
    ai = Login(userid=emailaddress, password=password)
    ai.save()
    return render(request, 'signup.html',)
def validateuser(request):
   userid=request.POST['userid']

   try:
       V=Login.objects.get(userid=userid)
       if V is not None:
           return redirect(reverse('userhome'))
   except ObjectDoesNotExist:
           return redirect(reverse('login'))
def userhome(request):
    return render(request,'userhome.html')