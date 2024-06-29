from django.db import models

class InsuranceData(models.Model):
    """
    InsuranceData model to store insurance records.
    """
    SEX_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    SMOKER_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    REGION_CHOICES = (
        ('southwest', 'Southwest'),
        ('northwest', 'Northwest'),
    )

    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    bmi = models.DecimalField(max_digits=5, decimal_places=2)
    children = models.IntegerField()
    smoker = models.CharField(max_length=10, choices=SMOKER_CHOICES)
    region = models.CharField(max_length=15, choices=REGION_CHOICES)
    charges = models.DecimalField(max_digits=10, decimal_places=2)
    coverage = models.CharField(max_length=50, default='Standard')

    def __str__(self):
        return f"{self.age}, {self.sex}, {self.region}"

    class Meta:
        verbose_name = 'Insurance Data'
        verbose_name_plural = 'Insurance Data'

