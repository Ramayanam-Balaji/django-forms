from django import forms
g=[('male','MALE'),('female','FEMALE')]
c=[('telugu','TELUGU'),('hindhi','HINDHI')]
class Signup(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g)
    course=forms.MultipleChoiceField(choices=c)
    #gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    
