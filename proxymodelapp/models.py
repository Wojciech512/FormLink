from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

class UserAccountManager(BaseUserManager):
	def create_user(self , email , password = None):
		if not email or len(email) <= 0 :
			raise ValueError("Email field is required !")
		if not password :
			raise ValueError("Password is must !")
		
		user = self.model(
			email = self.normalize_email(email) ,
			type=type or UserAccount.Types.PATIENT
		)
		user.set_password(password)
		user.save(using = self._db)
		return user
	
	def create_superuser(self , email , password):
		user = self.create_user(
			email = self.normalize_email(email) ,
			password = password
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using = self._db)
		return user
	
class UserAccount(AbstractBaseUser):
	class Types(models.TextChoices):
		PATIENT = "PATIENT" , "patient"
		DOCTOR = "DOCTOR" , "doctor"
	
	type = models.CharField(max_length = 8 , choices = Types.choices ,
							# Default is user is PATIENT
							default = Types.PATIENT)
	email = models.EmailField(max_length = 200 , unique = True)
	is_active = models.BooleanField(default = True)
	is_admin = models.BooleanField(default = False)
	is_staff = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)
	
	# special permission which define that
	# the new user is doctor or patient
	is_patient = models.BooleanField(default = False)
	is_doctor = models.BooleanField(default = False)
	
	USERNAME_FIELD = "email"
	
	# defining the manager for the UserAccount model
	objects = UserAccountManager()
	
	def __str__(self):
		return str(self.email)
	
	def has_perm(self , perm, obj = None):
		return self.is_admin
	
	def has_module_perms(self , app_label):
		return True
	
	def save(self , *args , **kwargs):
		if not self.type or self.type == None :
			self.type = UserAccount.Types.DOCTOR
		return super().save(*args , **kwargs)
	
# ================================================================

class PatientManager(models.Manager):
	def create_user(self , email , password = None):
		if not email or len(email) <= 0 :
			raise ValueError("Email field is required !")
		if not password :
			raise ValueError("Password is must !")
		email = email.lower()
		user = self.model(
			email = email
		)
		user.set_password(password)
		user.save(using = self._db)
		return user
	
	def get_queryset(self , *args, **kwargs):
		queryset = super().get_queryset(*args , **kwargs)
		queryset = queryset.filter(type = UserAccount.Types.PATIENT)
		return queryset	
		
class Patient(UserAccount):
    class Meta:
        proxy = True
    objects = PatientManager()

    def save(self, *args, **kwargs):
        if not self.id or self.id is None:
            self.type = UserAccount.Types.PATIENT
        return super().save(*args, **kwargs)

	
class DoctorManager(models.Manager):
	def create_user(self , email , password = None):
		if not email or len(email) <= 0 :
			raise ValueError("Email field is required !")
		if not password :
			raise ValueError("Password is must !")
		email = email.lower()
		user = self.model(
			email = email
		)
		user.set_password(password)
		user.save(using = self._db)
		return user
		
	def get_queryset(self , *args , **kwargs):
		queryset = super().get_queryset(*args , **kwargs)
		queryset = queryset.filter(type = UserAccount.Types.DOCTOR)
		return queryset
	
class Doctor(UserAccount):
    class Meta:
        proxy = True
    objects = DoctorManager()

    def save(self, *args, **kwargs):
        if not self.id or self.id is None:
            self.type = UserAccount.Types.DOCTOR
        return super().save(*args, **kwargs)
    
# ================================================================

from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Form(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    pseudo_id = models.IntegerField(default=0)
    name=models.CharField(max_length=100,blank=True)
    surname=models.CharField(max_length=100,blank=True)
    date_of_birth=models.CharField(max_length=12, blank=True)
    pesel=models.CharField(max_length=12, blank=True)
    sex = models.CharField(max_length=15, blank=True)

    phone_regex = RegexValidator(regex=r'\b\d{2}\s\d{3}-\d{3}-\d{3}\b', message="Phone number must be entered in the format: '+48 999-999-999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    height=models.CharField(max_length=5, blank=True)
    
    postal_code_regex = RegexValidator(regex=r'\b\d{2}-\d{3}\b', message="Postal code must be entered in the format: '42-600'.")
    postal_code = models.CharField(validators=[postal_code_regex], max_length=6, blank=True)

    city_regex = RegexValidator(regex=r'^[A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż ]+(?:[\s-][A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż ]+)*$', message="Incorrect city format.")
    city = models.CharField(validators=[city_regex], max_length=100, blank=True)

    street_regex = RegexValidator(regex=r'^[A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż ]+\s\d+[A-Z]?\/?\d*\b', message="Incorrect street format.")
    street = models.CharField(validators=[street_regex], max_length=100, blank=True)
    
    name_to_contact=models.CharField(max_length=30, blank=True)
    surname_to_contact=models.CharField(max_length=30, blank=True)
    phone_number_to_contact = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    connection_with_patient=models.CharField(max_length=30, blank=True)

    illness=models.CharField(max_length=200, blank=True)
    allergies=models.CharField(max_length=200, blank=True)
    addiction=models.CharField(max_length=200, blank=True)

    had_covid19 = models.CharField(max_length=5, blank=True)
    date_of_covid19=models.CharField(max_length=15, blank=True)

    covid19_vaccinated = models.CharField(max_length=5, blank=True)
    date_of_covid19_vaccinated=models.CharField(max_length=15, blank=True)

    name_of_drug=models.CharField(max_length=30, blank=True)
    drug_dose=models.CharField(max_length=10, blank=True)
    m_a_e_drug_dose = models.CharField(max_length=15, blank=True)

    extra_informations=models.CharField(max_length=1000, blank=True)


