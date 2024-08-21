from django.shortcuts import render,redirect
from .forms import myregisterForm
from django.contrib import messages
from .models import registerform

def home(req):
    data=registerform.objects.all()
    if(data!=''):
        return render(req,'home.html',{'data':data})
    else:
        return render(req,'home.html')

def insert(req):
    if req.method=='POST':
        form=myregisterForm(req.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(req,'Registration is successfull')
                return redirect('Home')
            except:
                pass
    else:
        form=myregisterForm()

    form=myregisterForm()
    return render(req,'register.html',{'form':form})

def update(req,id):
    data=registerform.objects.get(id=id)
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        address=req.POST['address']
        contact=req.POST['contact']
        email=req.POST['email']  
        data.Name=name
        data.Age=age
        data.Address=address
        data.Contact=contact
        data.Email=email
        data.save()
        messages.success(req,'Update sucessfully completed')
        return redirect('Home')
    return render(req,'update.html',{'data':data})
