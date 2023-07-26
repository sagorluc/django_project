from django import forms
from django.core import validators

# create form
class Teacher_registration(forms.Form):
    first_name = forms.CharField(label='Enter first name', label_suffix=' ')
    last_name = forms.CharField(label='Enter last name', initial='ahmed')
    email = forms.EmailField(label='Enter email', initial='mdsagorluc@gmail.com', disabled=True)
    password = forms.CharField(widget= forms.PasswordInput)
    repassword = forms.CharField(widget= forms.PasswordInput)
    text_area = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput)
    
    # matching password functionality
    def clean(self):
        cleaned_data = super().clean()
        right_password = self.cleaned_data['password']
        wrong_password = self.cleaned_data['repassword']
        
        if right_password == wrong_password:
           pass
        else:
            #print("Password doesn't matched")
            raise forms.ValidationError(
                f"Passwords don't match. Please try again. "
                
            )
        return cleaned_data
        
    
