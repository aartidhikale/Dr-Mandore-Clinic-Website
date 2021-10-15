from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from myapp.models import Consult1
from myapp.models import Item1,Contact,FAQ
from django.core.files.storage import FileSystemStorage
#from django.contrib.messages import constants as messages
from django.contrib import messages
# Create your views here.
from myapp.models import Register

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
      messages.success(request,'Consulation send  successfully')
      
      
      return render(request, 'about-us-page.html')
     
      
   else :
      return render(request, 'consult-page.html')
      
    


def diagnosis(request):
   return render(request, 'diagnosis-page.html')
   
      

   # return HttpResponse("index page ")
      


def faq(request):
   products1 = FAQ.objects.all()
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
        messages.success(request,'Feedback send successfully !!!!')
      
        return render(request, 'contact-us-page.html')
   return render(request, 'contact-us-page.html')

def user(request):
    
     
    if request.method=='GET' :
        
         User2 = Register.objects.all()
        
            
         for  p in User2:
                       
                            context={"p":p}
         return render(request,'user-profile.html',context)
                           
                        
                            
                                
                                
                           
        
        
                            
                            
    else:
       
       return render(request,"login.html")
           





def login(request):
    if request.method=='POST':
        
        user_name=request.POST['username']
        password1=request.POST['password']
        
        user=auth.authenticate(username=user_name,password=password1)
        if user is not None:
            auth.login(request,user)
          
            User2 = Register.objects.all()
            print(User2)
            
            for  p in User2:
                        if(p.username==user_name and p.password==password1):
                            context={"p":p}
            #return render(request,'user-profile.html',context)       
            messages.success(request,'Login successfully')
            return redirect('/user/',context)
        else:  
            messages.error(request,'Invalid credentials')     
            return render(request,'login.html')

    
    else:
        return render(request,'login.html')
        

def register2(username,password,email,first_name,last_name):
        user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
         #reg=Register.objects.create_user(mobile=mobile,gender=gender,city=city,Birthdate=birthdate,image=image)
        user.save()
         #user.save() 

   
def register(request):
    if request.method=='POST':
        reg=Register()
        reg.Birthdate=request.POST['DOB']
        reg.Email=request.POST['email']
        reg.City=request.POST['city']
        reg.Mobile=request.POST['mobile']
        reg.Gender=request.POST['gender']
        reg.firstname=request.POST['first_name']
        reg.lastname=request.POST['last_name']
        reg.username=request.POST['username']
        reg.password=request.POST['password']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        

        if len(request.FILES) != 0:
            reg.imageuser = request.FILES['image']
       
        #prod3=Item2()
        #if len(request.FILES)!=0:
            #prod3.image=request.FILES['image']
            #prod3.save()
        if User.objects.filter(email=email).exists():
         messages.error(request,'Email already exist')
         return render(request,'login-signup.html')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username already existes')
            return render(request,'login-signup.html')
        else:
         #user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
         #reg=Register.objects.create_user(mobile=mobile,gender=gender,city=city,Birthdate=birthdate,image=image)
         print("register")
         reg.save()
         register2(username,password,email,first_name,last_name)
         #user.save()
         messages.success(request,'Registration form submitted successfully! kindly login')
         return render(request,'login-signup.html')
       
    else:
        return render(request, 'login-signup.html')
        #return redirect('/')
       
        #if User.objects.filter(username=username).exists():
              
             # return redirect('login-signup')
       # elif  User.objects.filter(email=email).exists():
             #messages.info(request,'Email already exist')
       
            

    






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