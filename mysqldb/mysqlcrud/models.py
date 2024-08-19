from django.db import models

# Create your models here.

class registerform(models.Model):
    Name=models.CharField(max_length=20,default='')
    Age=models.IntegerField(default='')
    Address=models.CharField(max_length=50,default='')
    Contact=models.CharField(max_length=50)             
    Email=models.EmailField()                       

    class Meta:
        db_table='datas'


# ! Type in Terminal !

# python manage.py makemigrations mysqlcrud - it can create a database model (0001_init_.py) file in migration folder  

# python manage.py migrate - it add the content in a database in django database in http://localhost/phpmyadmin/  