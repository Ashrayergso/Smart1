from django.db import models

class SmartsheetData(models.Model):
    name = models.CharField(max_length=200)
    sign_on_date = models.DateField()
    sign_off_date = models.DateField()

    def __str__(self):
        return self.name

class ExcelData(models.Model):
    name = models.CharField(max_length=200)
    sign_on_date = models.DateField()
    sign_off_date = models.DateField()

    def __str__(self):
        return self.name
