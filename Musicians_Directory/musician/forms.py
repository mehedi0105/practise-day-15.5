from django import forms
from musician.models import Musician


class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        widgets = {
            'First_Name': forms.TextInput(attrs={'class': 'btn-primary'})
        }
        help_texts = {
            'First_Name': 'Write Your First Name: ',
            'Last_Name': 'Write Your First Name: ',
            'Email': 'Write Your Email: ',
            'Phone_Number': 'Write Your Phone Number: ',
            'Instrument_Type': 'Write Your Instrument Type: ',
        }
