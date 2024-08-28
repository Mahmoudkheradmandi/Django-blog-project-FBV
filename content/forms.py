from django import forms
from .models import Contact , NewsLetter
# from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
 

class ContactForm(forms.ModelForm):
    #captcha=CaptchaField()
    #last_name = forms.CharField(max_length=100)
    class Meta:
         
        model = Contact
        fields = '__all__'
    
class NewsLetteForm(forms.ModelForm):
    class Meta:
        model = NewsLetter 
        fields = '__all__'
        
        

    