from django import forms
from .models import Doctor, Patient
from .models import Form

class DoctorRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Doctor
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class PatientRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Patient
        fields = ['email', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

# ====================================================================================================

class ItemForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['patient','pseudo_id','name','surname','date_of_birth','pesel','sex','phone_number','height','postal_code','city','street',
                  'name_to_contact','surname_to_contact','phone_number_to_contact','connection_with_patient',
                  'illness','allergies','addiction','had_covid19','date_of_covid19','covid19_vaccinated','date_of_covid19_vaccinated','date_of_covid19_vaccinated',
                  'name_of_drug','drug_dose','m_a_e_drug_dose',
                  'extra_informations']