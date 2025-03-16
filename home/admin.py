from django.contrib import admin

# Register your models here.
from . models import Department,Doctor,Booking,blog,Feedback,contact,Support,NewsletterSubscriber,Patient

# Register your models here.
admin.site.register(Department)
class DoctorAdmin(admin.ModelAdmin):
    list_display=("doc_name","doc_dep")
admin.site.register(Doctor,DoctorAdmin)
class BookingAdmin(admin.ModelAdmin):
    list_display=("name","email","phone","doctor","booked","time","desc")
admin.site.register(Booking,BookingAdmin)
admin.site.register(Feedback)
admin.site.register(blog)
class contactAdmin(admin.ModelAdmin):
    list_display=("name","email","phone","message")
admin.site.register(contact,contactAdmin)
class SupportAdmin(admin.ModelAdmin):
    list_display=("name","email","phone","message")
admin.site.register(Support)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display=("email","created_at")
admin.site.register(NewsletterSubscriber,NewsletterSubscriberAdmin)
class PatientAdmin(admin.ModelAdmin):
    list_display=("name","email","phone","disease","doctor","booked","time")
admin.site.register(Patient,PatientAdmin)







