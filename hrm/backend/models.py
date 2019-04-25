from django.db import models

# Create your models here.
class Designation(models.Model):
    designation_name = models.CharField(max_length=50, unique=True)
    designation_status = models.BooleanField(max_length=10)

    def __str__(self):
        return self.designation_name

class Department(models.Model):
    department_name = models.CharField(max_length=50, unique=True)
    department_status = models.BooleanField(max_length=10)

    def __str__(self):
        return self.department_name
class Religion(models.Model):
    religion_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.religion_name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    father_name = models.CharField(max_length=255)
    Mother_name = models.CharField(max_length=255)
    date_of_birth= models.DateTimeField()
    gender = models.CharField(max_length=255)
    nationality = models.CharField(max_length=55)
    national_id = models.IntegerField()
    blood_group = models.CharField(max_length=25)
    religion    = models.ForeignKey(Religion,on_delete=models.CASCADE)
    marital_status = models.BooleanField(max_length=10)
    photo = models.ImageField(upload_to = 'employee/%Y/%m/%d/', default = 'employee/None/no-img.jpg')
    
    def __str__(self):
       return self.name

class EmployeeContactDetail(models.Model):
    Employee= models.ForeignKey(Employee,on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=125)
    present_address = models.CharField(max_length=255)
    permanent_address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
     
class EmployeeBankDetail(models.Model):
    Employee= models.ForeignKey(Employee,on_delete=models.CASCADE)
    account_no = models.IntegerField()
    bank_name = models.CharField(max_length=155)
    branch_name = models.CharField(max_length=155)
    
