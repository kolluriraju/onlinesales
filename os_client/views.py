import random

from django.shortcuts import render
from .models import Client, Complaint
from django.contrib import messages
from os_agent.models import Property,PropertyBlocked

def clienthome(request):
    request.session['status'] = False
    return render(request, "os_client_template/os_client_home.html")


def register(request):
    name = request.POST.get("c1")
    cont = request.POST.get("c2")
    adds = request.POST.get("c3")
    photo = request.FILES["c4"]
    uname = request.POST.get("c5")
    upass = request.POST.get("c6")
    otp = 1234
    Client(name=name,c_no=cont,adress=adds,photo=photo,client_uname=uname,password=upass,otp=otp).save()
    messages.success(request,name+" is Registred")
    qs=Client.objects.all()
    return render(request, "os_client_template/os_client_home.html",{"data":qs})


def login(request):
    if request.method == "POST":
        ausername = request.POST.get("c5")
        apassword = request.POST.get("c6")

        try:
            result = Client.objects.get(client_uname=ausername,password=apassword)
            otp = random.randint(100000, 999999)
            result.otp = otp
            result.save()
            message = "Hello Client This is Your One time Password :"+str(otp)
            #d1 = sendMessage.sendACASMS(ausername,message)

           # import json
            #dd = json.loads(d1)

            #if dd["return"]:
            if True:
                request.session['username'] = ausername
                return render(request,"os_client_template/os_client_otp.html")
            else:
                messages.error(request,"Sorry Unable to send OTP")
                return render(request, "os_client_template/os_client_home.html")

        except:
            messages.error(request,"Invalid user")
            return render(request, "os_client_template/os_client_home.html")

    else:
        return render(request, "os_client_template/os_client_home.html")


def clientotpcheck(request):
    if request.method == "POST":
        otp = request.POST.get("client_otp")
        try:
            result = Client.objects.get(otp=otp)
            request.session['status'] = True
            return render(request, "os_client_template/os_client_welcome.html")
        except:
            messages.error(request, "Invalid OTP")
            return render(request, "os_client_template/os_client_home.html")
    else:
        return render(request, "os_client_template/os_client_home.html")


def viewProperty(request):
    qs = Property.objects.filter(status="post")
    return render(request,"os_client_template/os_client_property.html",{"data":qs})


def blockProperty(request):
    uname = request.GET.get("uname")
    no = request.GET.get("no")
    # qs = BlockProperty.objects.filter(property_no_id=no)
    # print(uname)
    # print(qs)

    qs = PropertyBlocked.objects.filter(client_uname_id=uname,p_no_id=no)

    if qs:
        messages.info(request,"Blocked Property")
        qs = Property.objects.all()
        return render(request, "os_client_template/os_client_property.html", {"data": qs})
    else:
        PropertyBlocked(client_uname_id=uname,p_no_id=no).save()
        ws = PropertyBlocked.objects.filter(client_uname_id=uname)
        return render(request, "os_client_template/os_client_blocked.html", {"data": ws})


def blockedProperty(request):
    uname = request.session['username']
    ws = PropertyBlocked.objects.filter(client_uname_id=uname)
    return render(request, "os_client_template/os_client_blocked.html", {"data": ws})


def unblockProperty(request):
    uname = request.GET.get("uname")
    no = request.GET.get("no")
    PropertyBlocked.objects.filter(client_uname_id=uname, p_no_id=no).delete()
    ws = PropertyBlocked.objects.filter(client_uname_id=uname)
    return render(request, "os_client_template/os_client_blocked.html", {"data": ws})


def complaint(request):
    # uname = request.session['username']
    cont=request.POST.get("cont")
    comm = request.POST.get("comment")
    Complaint(comment=comm,cont=cont).save()
    return render(request,"os_client_template/os_client_complaint.html")