from django.shortcuts import render, redirect
from .forms import DoctorRegistrationForm, PatientRegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import ItemForm
from .models import Form, UserAccount,Doctor, Patient
from django.db.models import Max
import pdfkit
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def startPage(request) : 
    return render(request, "proxymodelapp/start.html" )

def doctor_registration(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = Doctor.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Dodaj dodatkową logikę lub przekierowanie
            return redirect('login-user') 
    else:
        form = DoctorRegistrationForm()
    
    return render(request, 'proxymodelapp/doctor_registration.html', {'form': form})


def patient_registration(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = Patient.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            # Dodaj dodatkową logikę lub przekierowanie
            return redirect('login-user')
    else:
        form = PatientRegistrationForm()
    
    return render(request, 'proxymodelapp/patient_registration.html', {'form': form})

@login_required
def new_form(request):
    max_pseudo_id = Form.objects.all().aggregate(Max('pseudo_id'))['pseudo_id__max'] or 0
    patient = request.user 

    if request.method =="POST":
        name=request.POST.get("name"),
        surname=request.POST.get("surname","")
        date_of_birth=request.POST.get("date_of_birth","")
        pesel=request.POST.get("pesel","")        
        sex=request.POST.get("sex","")
        phone_number=request.POST.get("phone_number","")
        height=request.POST.get("height","")
        postal_code=request.POST.get("postal_code","")
        city=request.POST.get("city","")
        street=request.POST.get("street","")

        name_to_contact=request.POST.get("name_to_contact","")
        surname_to_contact=request.POST.get("surname_to_contact","")
        phone_number_to_contact=request.POST.get("phone_number_to_contact","")
        connection_with_patient=request.POST.get("connection_with_patient","")

        illness=request.POST.get("illness","")
        allergies=request.POST.get("allergies","")
        addiction=request.POST.get("addiction","")

        had_covid19=request.POST.get("had_covid19","")
        date_of_covid19=request.POST.get("date_of_covid19","")
 
        covid19_vaccinated=request.POST.get("covid19_vaccinated","")
        date_of_covid19_vaccinated=request.POST.get("date_of_covid19_vaccinated","")

        name_of_drug=request.POST.get("name_of_drug","")
        drug_dose=request.POST.get("drug_dose","")
        m_a_e_drug_dose=request.POST.get("m_a_e_drug_dose","")
        date_of_covid19=request.POST.get("date_of_covid19","")

        extra_informations=request.POST.get("extra_informations","")

        form=Form(
            patient=patient,  
            name=name, 
            pseudo_id=max_pseudo_id + 1,
            surname=surname, 
            date_of_birth=date_of_birth,
            pesel=pesel,
            sex=sex,
            phone_number=phone_number,
            height=height,
            postal_code=postal_code,
            city=city,
            street=street,
            name_to_contact=name_to_contact,
            surname_to_contact=surname_to_contact,
            phone_number_to_contact=phone_number_to_contact,
            connection_with_patient=connection_with_patient,
            illness=illness,
            allergies=allergies,
            addiction=addiction,
            had_covid19=had_covid19,
            date_of_covid19=date_of_covid19,
            covid19_vaccinated=covid19_vaccinated,
            date_of_covid19_vaccinated=date_of_covid19_vaccinated,
            name_of_drug=name_of_drug,
            drug_dose=drug_dose,
            m_a_e_drug_dose=m_a_e_drug_dose,
            extra_informations=extra_informations)
            
        form.save()
        return redirect('newform')
    return render(request,'formapp/newform.html')

@login_required
def list_pdfs(request):
    if request.user.is_authenticated:
        if request.user.type == UserAccount.Types.DOCTOR:
            forms = Form.objects.all()
        else:
            forms = Form.objects.filter(patient=request.user)
        context_dict = {'user': request.user,'forms':forms,'type': request.user.type}
    else:
        context_dict= {'user': request.user,'forms':forms}

    if request.method == 'POST':
        return redirect('logout-user')
    
    return render(request,'formapp/list.html',context_dict)

@login_required
def delete_form(request,id):
    form=Form.objects.get(id=id)
    profiles = Form.objects.all()

    if request.method=='POST':
        form.delete()
        return redirect('list')
    return render(request,'formapp/delete.html')

@login_required
def view_form(request,id):
    user_profile = Form.objects.get(pk=id)
    return render(request,'formapp/generatedfile.html',{'user_profile':user_profile})

@login_required
def download_form(request,id):
    user_profile = Form.objects.get(pk=id)
    template = loader.get_template('formapp/generatedfile.html')
    html=template.render({'user_profile':user_profile})
    options={
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    
    config = pdfkit.configuration(wkhtmltopdf=r'C:/Users/wwyle/OneDrive/Pulpit/wkhtmltox/bin/wkhtmltopdf.exe')
 
    pdf = pdfkit.from_string(html,False,options=options,configuration=config)
    response = HttpResponse(pdf,content_type='proxymodel/proxymodelapp')
    response['Content-Disposition'] ='attachment;filename=formularz.pdf'
    return response

def login_admin(request):
    return render(request,'/admin.html')