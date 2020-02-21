from django.contrib import admin
from .models import Consumer,Category,Authority,Complaint,Feedback,Officer,Response

# Register your models here.

admin.site.register(Consumer)
admin.site.register(Category)
admin.site.register(Authority)
admin.site.register(Complaint)
admin.site.register(Feedback)
admin.site.register(Officer)
admin.site.register(Response)



