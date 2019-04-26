# Generated by Django 2.2 on 2019-04-25 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('Mother_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateTimeField()),
                ('gender', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=55)),
                ('national_id', models.IntegerField()),
                ('blood_group', models.CharField(max_length=25)),
                ('marital_status', models.BooleanField(max_length=10)),
                ('photo', models.ImageField(default='employee/None/no-img.jpg', upload_to='employee/%Y/%m/%d/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Department')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Designation')),
                ('religion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Religion')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(max_length=125)),
                ('present_address', models.CharField(max_length=255)),
                ('permanent_address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeBankDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.IntegerField()),
                ('bank_name', models.CharField(max_length=155)),
                ('branch_name', models.CharField(max_length=155)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Employee')),
            ],
        ),
    ]