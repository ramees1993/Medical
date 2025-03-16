from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Department,Doctor,blog,Feedback,Patient
from .forms import BookingForm,SupportForm,ContactForm,NewsletterSubscriberForm
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json




def index(request):
    department=Department.objects.all()
    doctor=Doctor.objects.all()
    feed=Feedback.objects.all()
    form=BookingForm()
    if request.method=="POST":
        form=BookingForm(request.POST)
        form.is_valid()
        form.save()
        form=BookingForm()
        return render(request,"done.html")

    contex= {
      "department" :department,
      "doctor": doctor,
      "form":form,
      "feed":feed,
    }
    return render(request,"index.html",contex)
def contact(request):
    form=ContactForm()
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
         form.save()
        form=ContactForm()
        return render(request,"thanks.html")

    contex= {
      

      "form":form,
    
    }
    
    return render(request, 'contact.html',contex)
def appointment(request):
    return render(request, 'appointment.html')
def service(request):
    department=Department.objects.all()
    news=blog.objects.all()
    form=BookingForm()
    if request.method=="POST":
        form=BookingForm(request.POST)
        form.is_valid()
        form.save()
        form=BookingForm()
        return render(request,"done.html")
    contex= {
      "department" :department,
      "form":form,
      "news":news,
    }
    return render(request,"service.html",contex)
def doctor(request):    
    return render(request, 'doctor.html')
def about(request):
    doctor=Doctor.objects.all()
    context={'doctor':doctor}
    return render(request, 'about.html',context)
def readmore(request):  
    return render(request, 'readmore.html')
def cardiology(request):
    doctor=Doctor.objects.filter(doc_dep__dep_name='Cardiology')
    context={'doctor':doctor}
    return render(request, 'cardiology.html',context)
def done(request):
    return render(request, 'done.html')
def ent(request):
    doctor=Doctor.objects.filter(doc_dep__dep_name='ENT')
    context={'doctor':doctor}
    return render(request, 'ent.html',context)
def Gastroenterology(request):
    doctor=Doctor.objects.filter(doc_dep__dep_name='Gastroenterology')
    context={'doctor':doctor}
    return render(request, 'Gastroenterology.html',context)
def General_Surgery(request):
    doctor=Doctor.objects.filter(doc_dep__dep_name='General Surgery')
    context={'doctor':doctor}
    return render(request, 'General Surgery.html',context)
def Neurology(request):
    doctor=Doctor.objects.filter(doc_dep__dep_name='Neurology')
    context={'doctor':doctor}
    return render(request, 'Neurology.html',context)
def Paediatrics(request):
    doctor=Doctor.objects.filter(doc_dep__dep_name='Paediatrics')
    context={'doctor':doctor}
    return render(request, 'Paediatrics.html',context)
def support(request):
    from django.shortcuts import render, redirect
from .forms import SupportForm

def support(request):
   

     form=SupportForm()
     if request.method=="POST":
        form=SupportForm(request.POST)
        if form.is_valid():
         form.save()
        form=SupportForm()
        return render(request,"thanks.html")

     contex= {
      

      "form":form,
    
    }
     return render(request,"support.html",contex)
    
def terms(request):
    return render(request, 'terms.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def department(request):
    return render(request, 'department.html')
def pricing(request):
    return render(request, 'pricing.html')
def team(request):
    return render(request, 'team.html')
def appointment(request):
    department=Department.objects.all()
    form=BookingForm()
    if request.method=="POST":
        form=BookingForm(request.POST)
        form.is_valid()
        form.save()
        form=BookingForm()
        return render(request,"done.html")
    contex= {
      "department" :department,
      "form":form,
    }
    return render(request, 'appointment.html',contex)
def feature(request):
    return render(request, 'feature.html') 
def chatbot(request):
    return render(request, 'chatbot.html')
def thank(request):
    return render(request, 'thank.html')

def newsletter_signup(request):
    if request.method == "POST":
        form = NewsletterSubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'wow.html')


            messages.success(request, "Congratulations  Subscribed successfully!")
            
        else:
            messages.error(request, "Invalid email or already subscribed.")
            return render(request,'sorry.html')
    
    return redirect(request.META.get("HTTP_REFERER", "/"))  # Redirect back to the same page
def patient(request):
    return render(request, 'patient.html',)


openai.api_key = "your_openai_api_key"

@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}]
        )

        bot_reply = response["choices"][0]["message"]["content"]
        return JsonResponse({"reply": bot_reply})
    return JsonResponse({"error": "Invalid request"}, status=400)

  


