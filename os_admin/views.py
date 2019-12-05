from django.shortcuts import render
from os_admin.models import Admin,Agent

from django.contrib import messages ,sessions
import random
from django.shortcuts import redirect
from onlinesales import sendmessage
from os_agent.models import Property
from os_client.models import Client


def adminlogincheck(request):
    if request.method == "POST":
        ausername = request.POST.get("admin_username")
        apassword = request.POST.get("admin_password")

        try:
            result = Admin.objects.get(c_no=ausername, password=apassword)
            otp = random.randint(100000, 999999)
            result.otp = otp
            result.save()
            message = "Hello Admin This is Your One time Password :" + str(otp)
            d1 = sendmessage.send2sms(ausername,message)
            import json
            dd = json.loads(d1)
            if dd["return"]:
                return render(request, "os_admin_template/admin_otp.html")
            else:
                return render(request, "os_admin_template/os_admin_login.html",
                                  {"error": "Sorry Unable to send OTP"})

        except:
                messages.error(request, "Invalid user")
                return render(request, "os_admin_template/os_admin_login.html")

    else:
        return render(request, "os_admin_template/os_admin_login.html")


def adminotpcheck(request):
    if request.method== "POST":
        otp=request.POST.get("admin_otp")
        request.session["status"] = True
        try:
            Admin.objects.get(otp=otp)
            return render(request,"os_admin_template/os_admin_menu.html")
        except:
            messages.error(request,"Invalid ...OTP..!")
            return render(request,"os_admin_template/admin_otp.html")
def agentsave(request):
    if request.method == "POST":
        idno=request.POST.get("agent_no")
        name=request.POST.get("agent_name")
        uname=request.POST.get("agent_username")
        pword=request.POST.get("agent_password")
        image=request.FILES["photo"]
        address=request.POST.get("agent_address")
        cno=request.POST.get("agent_contact")
        otp=123456
        Agent(no=idno,name=name,agent=uname,password=pword,image=image,address=address,c_no=cno,otp=otp).save()
        qs=Agent.objects.all()
        return render(request,"os_admin_template/os_agent_registration.html",{"data":qs})
    else:
        return render(request,"os_admin_template/os_admin_login.html")

def agentdelete(request):
    idno =request.GET.get("idno")
    Agent.objects.get(no=idno).delete()
    qs = Agent.objects.all()
    return render(request,"os_admin_template/os_agent_registration.html",{"data":qs})


def agentregister(request):
    qs=Agent.objects.all()
    return render(request,"os_admin_template/os_agent_registration.html",{"data":qs})


def adminlogout(request):
    request.session["status"]= False
    return render(request,"os_admin_template/os_admin_login.html")


def agentupdate(request):
    un = request.POST.get("up_id")
    uname = Agent.objects.get(no=un)
    return render(request,"os_admin_template/os_agent_update.html",{"data":uname})
def deleteview(request):
    idno = request.GET.get("idno")
    Agent.objects.filter(no=idno).delete()
    qs = Agent.objects.all()
    return render(request, "os_admin_template/os_admin_agenthome.html", {"data": qs})


def viewallClients(request):
    qs = Client.objects.all()
    return render(request,"os_admin_template/os_client.html",{"data":qs})


def deleteclient(request):
    uname = request.GET.get("idno")
    Client.objects.filter(client_uname=uname).delete()
    qs = Client.objects.all()
    return render(request, "os_admin_template/os_client.html", {"data": qs})


def propertyAll(request):
    qs = Property.objects.filter(status="post")
    return render(request, "os_admin_template/property_all.html", {"data": qs})