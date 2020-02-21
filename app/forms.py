from django import forms
from .models import Complaint,Consumer,Feedback

class ConsumerForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Consumer
        fields = ('first_name','last_name','email','address','country','state','city')

class ComplaintForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Complaint
        fields = ('title','description','consumer','category','open','authority')

class FeedbackForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Feedback
        fields = ('comment','email','created_on','type',)
         
