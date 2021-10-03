
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from myapp.models import Consult1
from .models import Item1,Contact,FAQ
from django.core.files.storage import FileSystemStorage
from django.core.checks import messages
from django.shortcuts import redirect, render
# Create your views here.


def home(request):
   # return HttpResponse("index page ")
    return render(request, 'home-page.html')


def about(request):
   # return HttpResponse("index page ")
    return render(request, 'about-us-page.html')


def consult(request):
   if request.method == 'POST':
      Firstname=request.POST['fname']
      Lastname=request.POST['lname']
      email=request.POST['email']
      Phone=request.POST['phone']
      Address=request.POST['address']
      birthdate=request.POST['dd']
      birthmonth=request.POST['nn']
      birthyear=request.POST['yyyy']
      hobbies=request.POST['Hobbies']
      work=request.POST['Work']
      diet=request.POST['Diet']
      diagnosis=request.POST['Diagnosis']
      
      a=Consult1(firstname=Firstname,lastname=Lastname,Email=email,phone=Phone,address=Address,Birthdate=birthdate,Birthmonth=birthmonth,Birthyear=birthyear,Hobbies=hobbies,Diagnosis=diagnosis,Work=work,Diet=diet)
      a.save()
      
      
      
      return render(request, 'about-us-page.html')
     
      
   else :
      return render(request, 'consult-page.html')
      
    


def diagnosis(request):
   return render(request, 'diagnosis-page.html')
   
      

   # return HttpResponse("index page ")
      


def faq(request):
   products1 = FAQ.objects.all()
   products2=products1
   
   
   
   context = {'products1':products1}
   return render(request, 'faq-page.html',context)


def portfolio(request):
    products = Item1.objects.all()
    context = {'products':products}
    return render(request, 'portfolio-page.html',context)


def contact(request):
   if request.method == "POST":
        prod1 = Contact()
        prod1.name = request.POST.get('name')
        prod1.phone = request.POST.get('phone')
        prod1.Email = request.POST.get('email')
        prod1.comment = request.POST.get('comment')

        

        prod1.save()
        print("Feedback sent sucessfully ")
      
        return render(request, 'contact-us-page.html')
   return render(request, 'contact-us-page.html')


def login(request):
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        print(username)
        user=auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            print("correct")
            return render(request,"user-profile.html")
        else:
                
            return render(request,'register.html')
    else:

     return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
       
        username=request.POST['username']
        #email=request.POST['email']
        password=request.POST['password']
        print(username)
        if User.objects.filter(username=username).exists():
            #messages.info(request,'Username already exist')
            return render(request, 'login.html')
            print("Username already exist")
        #elif User.objects.filter(email=email).exists():
             #messages.info(request,'Email already exist')
             #return render(request, 'login.html')
             #print("Email already exist")
        else:
          user=User.objects.create_user(username=username,password=password)
          user.save()
          print('user created')
          return render(request,'login.html')
    else:
     
     return render(request, 'register.html')


def user(request):
    # return HttpResponse("index page ")
    return render(request, 'user-profile.html')



def diagnosisInfo(request):
   # return HttpResponse("index page ")
    return render(request, 'diagnosis-info-page.html')

def addProduct(request):
    if request.method == "POST":
        prod = Item1()
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        print("image Added Successfully")
        products = Item1.objects.all()
        context = {'products':products}
        return render(request, 'portfolio-page.html',context)
    return render(request, 'add1')

# def addProduct(request):

#     if request.method == 'POST' and request.FILES['upload']:
#         upload = request.FILES['upload']
#         fss = FileSystemStorage()
#         file = fss.save(upload.name, upload)
#         file_url = fss.url(file)
#         #return render(request, 'portfolio-page.html', {'file_url': file_url})
#     return render(request, 'add1')
def uploadFaq(request):
    if request.method == "POST":
        prod2 = FAQ()
        prod2.question = request.POST.get('question')
        prod2.answer = request.POST.get('answer')
        

       

        prod2.save()
        print("FAQ Added Successfully")
        products1 = FAQ.objects.all()
        context = {'products1':products1}
        return render(request, 'faq-page.html',context)
    return render(request, 'uploadfaq.html')
