from django.db import models


# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=25)
    dep_des=models.TextField(max_length=500)
    def __str__(self):
        return self.dep_name
    class Meta:
        verbose_name="Departments"
        verbose_name_plural="Departments"
class Doctor(models.Model):
    doc_name=models.CharField(max_length=25)
    doc_dep=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_pic=models.ImageField(upload_to='doctors/')
    doc_face_book=models.URLField(null=True,blank=True)
    doc_twitter=models.URLField(null=True,blank=True)
    doc_insta=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.doc_name
    class Meta:
        verbose_name="Doctors"
        verbose_name_plural="Doctors"
class Booking(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booked=models.DateField()
    time=models.TimeField()
    desc=models.TextField(max_length=500)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Bookings"
        verbose_name_plural="Bookings"
class Feedback(models.Model):
    cus_name=models.CharField(max_length=25)
    cus_job=models.CharField(max_length=50)
    cus_desc=models.TextField(max_length=500)
    cus_pic=models.ImageField(upload_to="customer_pic/")
    def __str__(self):
        return self.cus_name
    class Meta:
        verbose_name="feedbacks"
        verbose_name_plural="feedbacks"
class blog(models.Model):
    title=models.CharField(max_length=35)
    desc=models.CharField(max_length=500)
    blog_pic=models.ImageField(upload_to='blog/')
    date=models.DateField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Blogs"
        verbose_name_plural="Blogs"
class contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    message=models.TextField(max_length=500)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Contacts"
        verbose_name_plural="Contacts"
class Support(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    message=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Supports"
        verbose_name_plural="Supports"
from django.db import models

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    class Meta:
        verbose_name="NewsletterSubscriber"
        verbose_name_plural="NewsletterSubscribers"
class Patient(models.Model):
    pic=models.ImageField(upload_to='patient_pic/')
    name=models.CharField(max_length=25)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    address=models.CharField(max_length=100)
    disease=models.FileField(max_length=50)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booked=models.DateField()
    time=models.TimeField()
    sex=models.CharField(max_length=10)
    age=models.IntegerField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Patients"
        verbose_name_plural="Patients"