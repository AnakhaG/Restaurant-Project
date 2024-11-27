from django.shortcuts import render,redirect
from RestoApp.models import FoodItems_DB,Food_Db
from WebApp.models import Contact_DB,Signup_DB,Cartdb,OrderDb
from django.contrib import messages
import razorpay
# Create your views here.
def homepagefn(re):
    fooditem = Food_Db.objects.all()
    Foodproduct=FoodItems_DB.objects.all()
    return render(re,"Home.html",{'fooditem':fooditem,'Foodproduct':Foodproduct})
def menu_fn(req):
    fooditems = Food_Db.objects.all()
    Foodpro=FoodItems_DB.objects.all()
    return render(req,"Menu.html", {'fooditems':fooditems,'Foodpro':Foodpro})
def about_page(re):
    return render(re,"About.html")
def service_pg(re):
    return render(re,"Services.html")
def contact_pg(re):
    return render(re,"Contact.html")
def save_contact(request):
    if request.method == "POST":
        n = request.POST.get('name')
        m = request.POST.get('email')
        s = request.POST.get('sub')
        me = request.POST.get('msg')
        obj =Contact_DB (Name=n, Email=m, Subject=s, Message=me)
        obj.save()
        return redirect(contact_pg)
def products_filtered(re,fud_name):
    data = FoodItems_DB.objects.filter(category=fud_name)
    return render(re,"Products_filtered.html",{'data':data})


def singlepg(re,fud_id):
    data = FoodItems_DB.objects.get(id=fud_id)
    return render(re,"Single.html",{'data':data})
def Signupp(re):
    return render(re,"Signup.html")
def save_signup(request):
    if request.method == "POST":
        n = request.POST.get('name')
        m = request.POST.get('email')
        mo = request.POST.get('mobile')
        p = request.POST.get('pass')
        rp = request.POST.get('re_pass')
        obj = Signup_DB(Name=n,Email=m,Mobile_Number=mo,Pass_word=p,Re_pass=rp)
        if Signup_DB.objects.filter(Name=n).exists():
            messages.warning(request,"User already exists..!")
        elif Signup_DB.objects.filter(Email=m).exists():
            messages.warning(request,"Email already exits..!")
        obj.save()
        return redirect(Signupp)
def loginpg(request):
    return render(request,"Login.html")
def userlo(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('passw')
        if Signup_DB.objects.filter(Name=un, Pass_word=pwd).exists():
            request.session['Name']=un
            request.session['Pass_word']=pwd
            messages.success(request,"Welcome")

            return redirect(homepagefn)
        else:
            messages.warning(request,"Please check your password")

            return redirect(loginpg)
    else:
        messages.warning(request,"Invalid username")

        return redirect(loginpg)
def userlogout(request):
    del request.session['Name']
    del request.session['Pass_word']
    messages.success(request, "LogOut successfully...!")

    return redirect(loginpg)
def Save_cart(request):
    if request.method == "POST":
        e = request.POST.get('uname')
        f = request.POST.get('fname')
        g = request.POST.get('price')
        h = request.POST.get('quantity')
        i = request.POST.get('total')
        obj=Cartdb(Username=e,FudName=f,Price=g,Quantity=h,TotalPrice=i)

        obj.save()
        messages.success(request, "Ordered successfully...!")
        return redirect(homepagefn)
def ur_order(re):
    cart_data = Cartdb.objects.filter(Username=re.session['Name'])
    Subtotal = 0
    Delivercrg = 0
    TotalAmount = 0
    for i in cart_data:
        Subtotal = Subtotal + i.TotalPrice
        if Subtotal >= 500:
            Delivercrg = 20
        else:
            Delivercrg = 50
        TotalAmount = Delivercrg + Subtotal

    return render(re,"Your_Orders.html",{'cart_data':cart_data,'Subtotal':Subtotal,
                                         'Delivercrg':Delivercrg,'TotalAmount':TotalAmount })

def decart_item(req,d_id):
    x = Cartdb.objects.filter(id=d_id)
    x.delete()
    return redirect(ur_order)
def payment(req):
    #Retrieve the data from OrderDb with the specifed id
    customer = OrderDb.objects.order_by('-id').first()

    #get the payment amount of the specified customer
    payy = customer.TotalPrice

    #Convert the amount into paisa (smallest currency unit)
    amount = int(payy*100)    #Assuming the payment amount in rupees

    payy_str = str(amount)

    for i in payy_str:
        print(i)
    if req.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_KBP3j6TlRjNrTj','LAn1pJFAOydXnsfTtQQhL6Dg'))
        payment = client.order.create({'amount':amount,'currency':order_currency})

    return render(req,"Payment.html",{'customer':customer,'payy_str':payy_str})

def propay(re):
    cart_data = Cartdb.objects.filter(Username=re.session['Name'])
    Subtotal = 0
    Delivercrg = 0
    TotalAmount = 0
    for i in cart_data:
        Subtotal = Subtotal + i.TotalPrice
        if Subtotal >= 500:
            Delivercrg = 20
        else:
            Delivercrg = 50
        TotalAmount = Delivercrg + Subtotal


    return render(re,"ProceedPay.html",{'cart_data':cart_data,'Subtotal':Subtotal,'Delivercrg':Delivercrg,'TotalAmount':TotalAmount})
def SaveOrder(re):
    ab=re.POST.get('Name')
    ij=re.POST.get('Place')
    bc=re.POST.get('Email')
    cd=re.POST.get('Phone')
    ef=re.POST.get('Address')
    fg=re.POST.get('TotalAmount')
    gh=re.POST.get('Messages')
    obj1=OrderDb(Name=ab,Place=ij,Email=bc,Mobile=cd,Address=ef,TotalPrice=fg,Message=gh)
    obj1.save()
    return redirect(payment)