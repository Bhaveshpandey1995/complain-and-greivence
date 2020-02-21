from django.shortcuts import render,reverse,redirect
from django.views.generic import CreateView,TemplateView,ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Complaint,Consumer,Feedback
from .forms import ComplaintForm,ConsumerForm,FeedbackForm
from django.contrib.auth import logout

from two_factor.views import OTPRequiredMixin

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class Signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('consumer')
    template_name = "registration/signup.html"

class ConsumerView(OTPRequiredMixin,CreateView):
    model = Consumer
    form_class = ConsumerForm
    success_url = '/complaint'
    template_name = "consumer.html"
    success_message = "consumer details submitted successfully"

    def form_valid(self,form):
        form.save()     
        return super().form_valid(form)

class ComplaintView(CreateView): 
    model = Complaint
    form_class = ComplaintForm
    template_name = "complaint.html"
    success_message = "complaint submitted successfully"
    success_url = '/'
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)


class ComplaintListView(OTPRequiredMixin,ListView):
    model = Complaint
    template_name = "allcomplaints.html"


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "feedback.html"
    success_message = "Feedback submitted successfully"
    success_url = '/'
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')

def profile_view(request):
    # Redirect to a success page.
    return redirect('/')