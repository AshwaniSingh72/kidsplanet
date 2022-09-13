from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import AdmissionForm, Contact,Feedback,Program_detail,Parent_detail,JobDescription,City_event,Event
# Create your views here.
def home(request):
    event_objects=Event.objects.all()
    event_dict={
    "event_key":event_objects
    }
    return render(request,'planetapp/html/index.html',event_dict)

def aboutus(request):
    return render(request,'planetapp/html/aboutus.html')

def contactus(request):

    if request.method=="GET":
        return render(request,'planetapp/html/contactus.html')

    if request.method=="POST":
        user_name=request.POST["txtname"]    #### request.POST is dictionary and control names are keys here
        user_email=request.POST["txtemail"]
        user_phone=request.POST["txtphone"]
        user_question=request.POST["txtquestion"]
        

        ##  object creation #######
        c=Contact(name=user_name,email=user_email,phone=user_phone,question=user_question)
        c.save()  ## object saving and it will store data into contact table using ORM 
        print("contact saved successfully")
        messages.success(request,"Thank you for contacting us. we will reach you soon.")

        return render(request,'planetapp/html/contactus.html')

   
    
def feedback(request):

    if request.method=="GET":
        program_objects=Program_detail.objects.all()
        program_dict={
             "program_key":program_objects
         }
        return render(request,'planetapp/html/feedback.html',program_dict)

        

    if request.method=="POST":
        FeedbackID=request.POST["txtfeedback"]    #### request.POST is dictionary and control names are keys here
        Name=request.POST["txtname"]
        Email=request.POST["txtemail"]
        Program=request.POST["cmb_name"]
       
        Query=request.POST["txtquery"]
        Rating=request.POST["txtrating"]
        

        ##  object creation #######
        c=Feedback(feedback_id=FeedbackID,name=Name,email=Email,programe_name=Program,feedback_text=Query,rating=Rating)
        c.save()  ## object saving and it will store data into contact table using ORM 
        print("Feedback saved successfully")
        messages.success(request,"Thank you for your feedback.")
        return render(request,'planetapp/html/feedback.html')

def registration(request):
    if request.method=="GET":
        program_objects=Program_detail.objects.all()
        program_dict={
            "program_key":program_objects
        }
        return render(request,'planetapp/html/registration.html',program_dict)

    if request.method=="POST":
        parent_id= request.POST["txtuserid"]
        parent_pass= request.POST["txtuserpass"]
        parent_email= request.POST["txtemail"]
        parent_phone= request.POST["txtphone"]

        p=Parent_detail(id=parent_id,password=parent_pass,email=parent_email,phone=parent_phone)

        p.save()
        print("Parent registratred save successfully")
        messages.success(request,"thank you")
        return render(request,'planetapp/html/registration.html')


def login(request):
    if request.method=="GET":
       return render(request,'planetapp/html/login.html')
    
    if request.method=="POST":
        parent_id=request.POST["userid"]
        parent_password=request.POST["userpass"]

        parent_query_set= Parent_detail.objects.filter(id=parent_id,password=parent_password)
        print(len(parent_query_set))

        if len(parent_query_set)>0:
            request.session["parent_session"]=parent_id  #### builtIn dict
            parent_object={
                "parent_data":parent_query_set
                }
            return render(request,'planetapp/html/parent/home.html',parent_object)
        else:
            messages.error(request,'Invalid Credential')
            return render(request,'planetapp/html/login.html')

def edit_profile(request):

    if "parent_session" not in request.session.keys():
        return redirect("parent_login")


    if request.method=="GET":
        loggedIn_parent_Id=request.session["parent_session"] # feching value from session
        parent_object=Parent_detail.objects.get(id=loggedIn_parent_Id) ## finding the objects
        parent_dict={
            "parent_data":parent_object
        }

        return render(request,'planetapp/html/parent/edit_profile.html',parent_dict)
    
    if request.method=="POST":
        phone=request.POST["txtphone"]
        email=request.POST["txtemail"]
        loggedIn_parent_Id=request.session["parent_session"] # feching value from session
        parent_object=Parent_detail.objects.get(id=loggedIn_parent_Id) ## finding the objects

        parent_object.phone=phone
        parent_object.email=email

        parent_object.save()
        parent_dict={
            "parent_data":parent_object
        }

        messages.success(request,"Profile updated successfully")
        return render(request,'planetapp/html/parent/edit_profile.html',parent_dict)
    
def admission(request):
    if request.method=="GET":
         program_objects=Program_detail.objects.all()
         program_dict={
             "program_key":program_objects
         }
         return render(request,'planetapp/html/parent/admission.html',program_dict)

    if request.method=="POST":
        program_name= request.POST["cmb_name"]
        kid_name= request.POST["txtkid"]
        kid_age= request.POST["txtage"]
        mother_name= request.POST["txtmother"]
        father_name= request.POST["txtfather"]
        phone= request.POST["txtphone"]
        email= request.POST["txtemail"]
        address= request.POST["txtaddress"]
        gender= request.POST["gender"]
        school_name= request.POST["txtschool"]
        transaction= request.POST["txttransaction"]

        a=AdmissionForm(program_name=program_name,kid_name=kid_name,kid_age=kid_age,mother_name=mother_name,father_name=father_name,phone=phone,email=email,address=address,kid_gender=gender,school_name=school_name,transaction_number=transaction)

        a.save()
        print("Admission Form save successfully")
        messages.success(request,"thank you for admission")
        return render(request,'planetapp/html/parent/admission.html')




def parent_logout(request):

    if "parent_session" not in request.session.keys():
        return redirect("login")

    del request.session["parent_session"]  ### it is used to destroy the session
    return redirect("login")

def facilities(request):
    return render(request,'planetapp/html/facilities.html')

def program_detail(request):
    program_obj=Program_detail.objects.all()   ## it return queryset
    program_dict={
        "program_data":program_obj,
    }
    return render(request,'planetapp/html/program_detail.html',program_dict)


def job_detail(request):
    program_obj=JobDescription.objects.all()   ## it return queryset
    program_dict={
        "job_data":program_obj,
    }
    return render(request,'planetapp/html/job.html',program_dict)