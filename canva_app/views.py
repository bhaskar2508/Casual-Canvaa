from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout


# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        messages.success(request, 'Your Registration has been sent Successfully !')  
        return redirect('/')
    else:
        f=UserCreationForm
        context={'form':f}
        return render(request,'register.html',context)


from .models import LoginForm

def login_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        passw=request.POST.get('password')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            login(request,user)
            request.session['uid'] = user.id
            return redirect('/')
        else:
            f=LoginForm
            context={'form':f}
            return render(request,'login.html',context)
    else:
        f=LoginForm
        context={'form':f}
        return render(request,'login.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')


def collections(request):
    return render(request,'collections.html')


from .models import Product,Cart,WomenCart

def men_list(request):
    if request.method == 'POST':
        f = Product(request.POST, request.FILES)
        if f.is_valid():  
            f.save()
    ml = Product.objects.all()
    context = {'ml': ml}
    return render(request, 'mens.html', context)
    


def add_to_cart(request,pid):
    product=Product.objects.get(id=pid)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    c=Cart()
    c.product=product
    c.user=user
    c.save()
    return redirect('/clist')


def cart_list(request):
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    cl=Cart.objects.filter(user=uid)
    wl=WomenCart.objects.filter(user=uid)
    kl=KidsCart.objects.filter(user=uid)
    ll=EndSaleCart.objects.filter(user=uid)
    context={'cl':cl,
             'wl':wl,
             'kl':kl,
             'll':ll}
    return render(request,'cartlist.html',context)

from .models import Women


def women_list(request):
    if request.method == 'POST':
        f = Women(request.POST, request.FILES)
        if f.is_valid():  
            f.save()
    wl = Women.objects.all()
    context = {'wl': wl}
    return render(request, 'womens.html', context)



def contact(request):
    return render(request,'contact.html')

def women(request,wid):
    women=Women.objects.get(id=wid)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    c=WomenCart()
    c.women=women
    c.user=user
    c.save()
    return redirect('/clist')

from .models import Kid,KidsCart

def kids_list(request):
    if request.method == 'POST':
        f=Kid(request.POST,request.FILES)
        if f.is_valid():
            f.save
    kl=Kid.objects.all()
    context={'kl':kl}
    return render(request, 'kids.html',context)

def kids(request,kid):
    kid=Kid.objects.get(id=kid)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    c=KidsCart()
    c.kid=kid
    c.user=user
    c.save()
    return redirect('/clist')
    
def delete(request):
    eid=request.GET.get('id')
    cl=Cart.objects.get(id=eid)
    cl.delete()
    return redirect('/clist')

def women_delete(request):
    wid=request.GET.get('id')
    wl=WomenCart.objects.get(id=wid)
    wl.delete()
    return redirect('/clist')

def kid_delete(request):
    kid=request.GET.get('id')
    kl=KidsCart.objects.get(id=kid)
    kl.delete()
    return redirect('/clist')

from django.conf import settings
import razorpay

from .models import EndSaleCart,EndSale

def end_sale_list(request):
    if request.method=='POST':
        f=EndSale(request.POST,request.FILES)
        if f.is_valid():
            f.save()
    ll=EndSale.objects.all()
    context={'ll':ll}
    return render(request,'end_sale.html',context) 

def endsale(request,lid):
    endsale=EndSale.objects.get(id=lid)
    uid=request.session.get('uid')
    user=User.objects.get(id=uid)
    c=EndSaleCart()
    c.endsale=endsale
    c.user=user
    c.save()
    return redirect('/clist')


def endsale_delete(request):
    endsale=request.GET.get('id')
    ll=EndSaleCart.objects.get(id=endsale)
    ll.delete()
    return redirect('/clist')


def about(request):
    return render(request,'about.html')

from django.shortcuts import render

from django.shortcuts import render

def payment_view(request):
    if request.method == "POST":
        final_total = request.POST.get('final_amount', 0)
        gst_value = round(float(final_total) * 0.18, 2)
        invoice_total = round(float(final_total) + gst_value, 2)

        context = {
            'final_total': final_total,
            'gst_value': gst_value,
            'invoice_total': invoice_total
        }
        return render(request, 'payment.html', context)
    return render(request, 'payment.html')



from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse

def data1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(f"Name: {name}, Email: {email}, Subject: {subject}, Message: {message}")
        
        messages.success(request, 'Your Message has been sent Successfully !')  
        
        return redirect('contact')
    else:
        return render(request, 'contact.html')


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process_payment(request):
    return render(request,'success.html')

