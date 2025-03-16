from django.urls import path
from. import views

urlpatterns = [
    path('',views.index,name="index"),
    path("contact/",views.contact,name="contact"),
    path("appointment/",views.appointment,name="appointment"),
    path("service/",views.service,name="service"),
    path("doctor/",views.doctor,name="doctor"),
    path("about/",views.about,name="about"),
    path("testimonial/",views.testimonial,name="testimonial"),
    path("readmore/",views.readmore,name="readmore"),
    path("cardiology/",views.cardiology,name="cardiology"),
    path("done/",views.done,name="done"),
    path("ent/",views.ent,name="ent"),
    path("Gastroenterology/",views.Gastroenterology,name="Gastroenterology"),
    path("General Surgery/",views.General_Surgery,name="General Surgery"),
    path("Neurology/",views.Neurology,name="Neurology"),
    path("Paediatrics/",views.Paediatrics,name="Paediatrics"),
    path("support/",views.support,name="support"),
    path("terms/",views.terms,name="terms"),
    path("feature/",views.feature,name="feature"),
    path("blog/",views.blog,name="blog"),
    # path("blog/<int:id>",views.blog,name="blog"),
    path("chatbot/",views.chatbot,name="chatbot"),
    path('newsletter/',views. newsletter_signup, name='newsletter_signup'),
    path("patient/",views.patient,name="patient"),
    path("chatbot/",views.chatbot_response, name="chatbot_response"),
]










    



    



    
    

    








