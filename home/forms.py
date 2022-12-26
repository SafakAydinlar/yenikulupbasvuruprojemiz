


from django import forms
from .models import Basvuru, Basvuru2, Basvuru3, Basvuru4, Basvuru5


class BasvuruForm(forms.ModelForm):
    class Meta:
        model = Basvuru
        fields = '__all__' 
        

class BasvuruForm2(forms.ModelForm):
    class Meta:
        model = Basvuru2
        fields = '__all__' 


class BasvuruForm3(forms.ModelForm):
    class Meta:
        model = Basvuru3
        fields = '__all__' 


class BasvuruForm4(forms.ModelForm):
    class Meta:
        model = Basvuru4
        fields = '__all__' 


class BasvuruForm5(forms.ModelForm):
    class Meta:
        model = Basvuru5
        fields = '__all__' 
        

