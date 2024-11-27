from django.shortcuts import render,redirect
from RestoApp.models import Food_Db
from RestoApp.models import FoodItems_DB
from WebApp.models import Contact_DB
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
# Create your views here.
def Index_page(re):
    x = Food_Db.objects.count()
    y = FoodItems_DB.objects.count()
    return render(re,"Index.html",{'x':x,'y':y})
def add_food(r):
    return render(r,"AddFood.html")
def save_food(req):
    if req.method == "POST":
        cat = req.POST.get('categoryname')
        des = req.POST.get('desc')
        im = req.FILES['Catimg']
        obj = Food_Db(Category_Name=cat,Description=des,Category_Image=im)
        obj.save()
        return redirect(add_food)

def display_food(req):
    data = Food_Db.objects.all()
    return render(req,"DisplayFood.html",{'data':data})
def edit_food(req,fud_id):
    data = Food_Db.objects.get(id=fud_id)
    return render(req,"EditFood.html",{'data':data})
def update_food(re,fud_id):
    if re.method=="POST":
        cat = re.POST.get('categoryname')
        des = re.POST.get('desc')
        try:
            img =re.FILES['Catimg']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Food_Db.objects.get(id=fud_id).Category_Image
        Food_Db.objects.filter(id=fud_id).update(Category_Name=cat,Description=des,Category_Image=file)
        return redirect(display_food)
def delete_food(re,fud_id):
    x=Food_Db.objects.filter(id=fud_id)
    x.delete()
    return redirect(display_food)

# Drinks
def add_food_items(re):
    data = Food_Db.objects.all()
    return render(re,"AddFood_Items.html",{'data':data})
def save_food_items(req):
    if req.method == "POST":
        cat = req.POST.get('category')
        name = req.POST.get('foodname')
        Mrp = req.POST.get('mrp')
        desc = req.POST.get('fuddesc')
        imga = req.FILES['img1']
        imgb = req.FILES['img2']
        imgc = req.FILES['img3']
        obj = FoodItems_DB(category=cat,Food_Name=name,Price=Mrp,Food_Description=desc,Food_Imagea=imga,
                           Food_Imageb=imgb,Food_Imagec=imgc)
        obj.save()
        return redirect(add_food_items)
def display_food_items(re):
    data = FoodItems_DB.objects.all()
    return render(re,"DisplayFood_Items.html",{'data':data})
def edit_food_items(re,fud_id):
    item = FoodItems_DB.objects.get(id=fud_id)
    data = Food_Db.objects.all()

    return render(re,"EditFood_Items.html",{'item':item,'data':data})
def update_food_items(re,fud_id):
    if re.method=="POST":
        cat = re.POST.get('category')
        name = re.POST.get('foodname')
        Mrp = re.POST.get('mrp')
        desc = re.POST.get('fuddesc')
        try:
            img1 = re.FILES['img1']
            fs = FileSystemStorage()
            file1 = fs.save(img1.name,img1)
        except MultiValueDictKeyError:
            file1 = FoodItems_DB.objects.get(id=fud_id).Food_Imagea
        try:
            img2 = re.FILES['img2']
            fs = FileSystemStorage()
            file2 = fs.save(img2.name,img2)
        except MultiValueDictKeyError:
            file2 = FoodItems_DB.objects.get(id=fud_id).Food_Imageb
        try:
            img3 = re.FILES['img3']
            fs = FileSystemStorage()
            file3 = fs.save(img3.name,img3)
        except MultiValueDictKeyError:
            file3 = FoodItems_DB.objects.get(id=fud_id).Food_Imagec
        FoodItems_DB.objects.filter(id=fud_id).update(category=cat,Food_Name=name,Price=Mrp,Food_Description=desc,Food_Imagea=file1,
                           Food_Imageb=file2,Food_Imagec=file3)
        return redirect(display_food_items)
def delete_food_items(re,fud_id):
    x = FoodItems_DB.objects.filter(id=fud_id)
    x.delete()
    return redirect(display_food_items)


def admin_login(re):
    return render(re,"Admin_login.html")
def admin_loginfn(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswrd = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pswrd)
            if user is not None:
                request.session['username']=un
                request.session['password']=pswrd
                login(request,user)
                messages.success(request,"Welcome")

                return redirect(Index_page)
            else:
                messages.warning(request,"Please check your Password")

                return redirect(admin_login)
        else:
            messages.warning(request,"Invalid Username")

            return redirect(admin_login)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Log Out successfully")
    return redirect(admin_login)
def contact_det(request):
    con = Contact_DB.objects.all()
    return render(request,"Contact_data.html",{'con':con})
def Dele_contact(re, con_id):
    obj = Contact_DB.objects.filter(id=con_id)
    obj.delete()
    return redirect(contact_det)
