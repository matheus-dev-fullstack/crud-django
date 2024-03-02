from django import forms

from exemplo.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente 
        fields = '__all__'