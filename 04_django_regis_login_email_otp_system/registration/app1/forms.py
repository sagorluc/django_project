from django import forms

class HomeForm(forms.Form):
    id = forms.IntegerField(label= 'ID')
    name = forms.CharField(label="UserName ")
    from_email = forms.EmailField(label="Email your email ")
    message = forms.CharField(widget= forms.Textarea(attrs= {'placeholder': 'Write your message here..'}))
    