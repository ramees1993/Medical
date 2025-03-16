from django import forms
from . models import Booking,Support,contact,NewsletterSubscriber
from django . forms import TextInput,Select,Textarea


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=["name","email","phone","doctor","booked","time","desc"]
        widgets ={
            "name": TextInput(attrs={
            "type":"name",
             "class":"form-control border-0",
             "placeholder":"Your Name",
             "style":"height: 55px;"    
            }),
            "email": TextInput(attrs={
            "type":"email",
            "class":"form-control border-0",
             "placeholder":"Your Email",
               "style":"height: 55px;"    
            }),
            "phone": TextInput(attrs={
            "type":"phone",
             "class":"form-control border-0", 
            "placeholder":"Your Mobile", 
            "style":"height: 55px;"    
            }),
            "doctor": Select(attrs={
            "class":"form-select border-0",
            "style":"height: 55px;"
                
            }),
            "booked": TextInput(attrs={
            "type":"date",
            "class":"form-control border-0",
            "style":"height: 55px;" 
            }),
            "time": TextInput(attrs={
            "type":"time",
            "class":"form-control border-0",
            "style":"height: 55px;" 
            }),
             "desc": Textarea(attrs={
            "type":"textarea",
             "class":"form-control border-0", 
            "placeholder":"Describe your problem", 
            "rows":"5"
            }),
            
        }
class SupportForm(forms.ModelForm):
    class Meta:
        model=Support
        fields=["name","email","phone","message"]
        # widgets ={
        #     "name": TextInput(attrs={
        #     "type":"name",
        #      "class":"form-control border-0",
        #      "placeholder":"Your Name",
        #      "style":"height: 55px;"    
        #     }),
        #     "email": TextInput(attrs={
        #     "type":"email",
        #     "class":"form-control border-0",
        #      "placeholder":"Your Email",
        #        "style":"height: 55px;"    
        #     }),
        #     "phone": TextInput(attrs={
        #     "type":"phone",
        #      "class":"form-control border-0", 
        #     "placeholder":"Your Mobile", 
        #     "style":"height: 55px;"    
        #     }),
        #     "desc": Textarea(attrs={
        #     "type":"textarea",
        #      "class":"form-control border-0", 
        #     "placeholder":"Describe your problem", 
        #     "rows":"5"
        #     }),
            
        # }  
class ContactForm(forms.ModelForm):
    class Meta:
        model=contact
        fields=["name","email","phone","message"]
        widgets ={
            "name": TextInput(attrs={
            "type":"name",
             "class":"form-control border-0",
             "placeholder":"Your Name",
             "style":"height: 55px;"    
            }),
            "email": TextInput(attrs={
            "type":"email",
            "class":"form-control border-0",
             "placeholder":"Your Email",
               "style":"height: 55px;"
            }),
              "phone": TextInput(attrs={
            "type":"phone",
             "class":"form-control border-0", 
            "placeholder":"Your Mobile", 
            "style":"height: 55px;"    
            }),
            
             "desc": Textarea(attrs={
            "type":"textarea",
             "class":"form-control border-0", 
            "placeholder":"Leave a message here", 
            "rows":"5"
            }),
        }
class NewsletterSubscriberForm(forms.ModelForm):
    class Meta:
        model=NewsletterSubscriber
        fields=["email"]
        widgets ={
            "email": TextInput(attrs={
            "type":"email",
            "class":"form-control border-0",
             "placeholder":"Your Email",
               "style":"height: 55px;"
            }),
        }              


            
