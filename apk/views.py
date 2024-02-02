from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.core.mail import send_mail
from apk.models import *



def main(request):
    return render (request,'main.html')


#######    nav items  ########
def home(request):
    return render (request,'index.html')

def shop(request):    
    data=shirts_men_data.objects.all()
    return render(request,'shop.html',{'data':data})

def about(request):
    return render (request,'about.html')

def blog(request):
    return render (request,'blog.html')

def contact(request):
    return render (request,'contact.html')

def cart(request):
    return render (request,'cart.html')

def checkout(request):
    return render (request,'checkout.html')

def blog_single(request):
    return render (request,'blog-single.html')




def profile(request):
    user=User.objects.get(username=request.user)
    ss=myuser.objects.filter(my_user=user)
    return render (request,'profile.html',{'show':ss})

def logsign(request):
    return render (request,'logsign.html')

def ChangePassword(request):
    return render (request,'ChangePassword.html')

########### nav end ################


def update(request):
    return render (request,'update.html')

######### data start ################
def shoes(request):
    data=man_shoe.objects.all()
    return render (request,'shoes.html',{'data':data})
def mens_shirt(request):
    data=shirts_men_data.objects.all()
    return render (request,'mens_shirt.html',{"data":data})

def product_detail(request,id):
    return render (request,'product_detail.html')

def shirt_product(request,id):
    shirts=shirts_men.objects.get(id=id)
    data=shirts_men_data.objects.filter(man_fks=shirts)
    return render (request,'product-single.html',{'data':data})
def tshirt_product(request,id):
    tshirt=Tshirt_men.objects.get(id=id)
    data=Tshirt_men_data.objects.filter(man_fks=tshirt)
    return render(request,'product-single.html',{"data":data})
    
def show_user_data(request):
    user=User.objects.get(username=request.user)
    ss=myuser.objects.filter(my_user=user)
    return render(request,'profile.html',{'show':ss})

def mens_tshirt(request):
    data=Tshirt_men_data.objects.all()
    return render (request,'mens_tshirt.html',{'data':data})
def mens_jeans(request):
    data=jeans_men_data.objects.all()
    return render (request,'mens_jean.html',{'data':data})
def mens_jacket(request):
    data=jacket_men_data.objects.all()
    return render (request,'mens_jacket.html',{'data':data})





######### signup , login and logout #########
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=name, email=email, password=password)
        
        messages.success(request, 'User has successfully been created')
        
        send_mail(
            "Mail from Anshu Website",
            f"Thanks {name} for Signup with us , our team connect with you with in hour ",
            "anshu93172@gmail.com",
            [email],
            fail_silently=False,
        )
        return redirect('login')
    else:
        return render(request, 'signup.html')
# login here
def login(request):
    
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        my_user=User.objects.get(email=email).username
        user=authenticate(username=my_user,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You have successfully login')           
            return redirect('home')
        else:
            messages.error(request,'invalid id or password')
            messages.error(request, 'Invalid user')
            return redirect('login')
    else:
        return render(request, "login.html")

def user():
    s=User.objects.get(username=s)
    
def Logout(request):
    logout(request)
    messages.success(request,'logout succesfully')
    return redirect('main')



def userdata(request):
    user=User.objects.get(username=request.user)
    if request.method=='POST':
        my_email=request.POST['email']
        my_mobile=request.POST['mobile']
        my_address=request.POST['address']
        myuser.objects.create(my_user=user,email=my_email,mobile=my_mobile,address=my_address)
        return render(request,'update.html')
    else:
        return render(request,'update.html')

  
############# end login signup logout ######



  
def demo(request):
    pass
   