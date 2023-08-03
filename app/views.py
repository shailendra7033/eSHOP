from django.shortcuts import render,redirect;
from .models import Customer,Cart,OrderPlaced,Product;
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View;
from .forms import AddressForm
from datetime import date
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

def home(request):
 hoddie= Product.objects.filter(category='CAP' ) |Product.objects.filter(category='HOD' )  |Product.objects.filter(category='JKT' ) 
 tshirt =Product.objects.filter(category='TS')   |Product.objects.filter(category='JNS')    
 return render(request, 'app/home.html',{'hoddie':hoddie,'tshirt':tshirt})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetail(View):
    def get(self, request, id):
        product = Product.objects.get(pk=id);
        
        return render(request, 'app/productdetail.html',{'product':product})


def add_to_cart(request):
 if request.user.is_authenticated:
    usr=request.user;
    productid=request.GET.get('product_id')  ;
    print(productid)
    products=Product.objects.get(id=productid) ;
    item_add=Cart(user=usr,product=products);
    item_add.save();
    return redirect('/show_cart')
 return redirect('/')


# there is a problem while implementing show cart and add to cart , same product baar baar
#cart me add ho jaa raha tha jiiti baar refresh kar rahe the shyad esliye qki add to cart k views funstion me hmm save to cart wala function likhe the esliye

#cart show function


def show_cart(request):
    if request.user.is_authenticated:
        usr=request.user;
        print(usr);
        cart=Cart.objects.all().filter(user=usr);
        sum=0;
        if not cart:
          count=0;  
          return render(request,'app/emptycart.html',{'count':count});
        count=0; 
        for cart_item in cart:
            x=cart_item.product.discount_price;
            sum=sum+x;
            count=count+1;
        print(sum);
        with_delivery_charge=sum+70;
        return render(request,'app/addtocart.html',{'cart':cart,'total':sum,'with_delivery_charge':with_delivery_charge,'count':count})
    return render(request,'app/addtocart.html')



def remove_from_cart(request):
    product_id=request.GET.get('product_id')  ;
    print(product_id);
    cart_product=Cart.objects.get(id=product_id);
    cart_product.delete();
    return redirect('/show_cart');



def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

#class based view for profile and taking details of customer

class ProfileView(View): 
    def get (self, request):
        form=AddressForm()
        return render(request,'app/profile.html',{'form':form});

    def post (self, request):
        form=AddressForm(request.POST)
        if form.is_valid():
            usr=request.user
            name =form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state= form.cleaned_data['state']
            pincode=form.cleaned_data['pincode']

            form1data=Customer(user=usr,name=name,locality=locality,city=city,state=state,pincode=pincode)
            form1data.save()
            form2=AddressForm()
            return render(request,'app/profile.html',{'form':form2});




def address(request):
    usr=request.user;
    addresses=Customer.objects.filter(user=usr);
    return render(request, 'app/address.html',{'address':addresses})

def orders(request):
 usr=request.user;
 order_placed=OrderPlaced.objects.all().filter(user=usr)
 return render(request, 'app/orders.html',{'order_placed':order_placed})

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')



def login(request):
    if request.user.is_authenticated:
        return redirect('/profile');  


    if request.method=="POST":
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        print(Username,Password);
        user = authenticate(request, username=Username, password=Password)
        print(Username,Password);
        if user is not None:
            auth_login(request,user)
            return redirect('/profile');
            return render(request,'app/home.html');
        else:
            print("error in login");

    return render(request,'app/login.html');


# def login(request):
#  return render(request, 'app/login.html')

# registration function
def customerregistration(request):
    if request.user.is_authenticated:
        return redirect('/profile'); 

#form for registering the user

    if request.method == "POST":
     fm = UserCreationForm(request.POST)
     if fm.is_valid():
        fm.save()
        messages.success(request, 'Account created successfully')
        return render(request,'app/login.html')
    else:
        fm=UserCreationForm()

    return render(request,'app/customerregistration.html',{'form':fm});




# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

def checkout(request):
 usr=request.user;
 cart_items=Cart.objects.all().filter(user=usr);
 address_cart=Customer.objects.all().filter(user=usr)
 return render(request, 'app/checkout.html',{'cart_list':cart_items,'address_cart':address_cart})



def payment(request):
    customer_id=request.GET.get('address');

    # print(customer_id," hii hello \n \n")
    # customer_id=10;
    usr=request.user
    customer=Customer.objects.get(id=customer_id)
    print(customer_id," hii hello \n \n")
    dates=date.today()
    # print(dates)
    cart_items=Cart.objects.all().filter(user=usr)
    for items in cart_items:
        place_order=OrderPlaced(user=usr,product=items.product,customer=customer,ordered_date=dates,quantity=items.quantity)
        place_order.save();
        items.delete()
    return render(request,'app/payment.html');


def logout(request):
    auth_logout(request)
    return redirect('/');





        # # if request.method =="POST":
        #     form=AddressForm(request.POST);
        #     if form.is_valid():
        #         form.save()
        # # else:
        # #     form=AddressForm()

        # return render(request,'app/profile.html',{'form':form});
