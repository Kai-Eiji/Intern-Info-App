from django.db import models

class Interns(models.Model):
    YEARS = (("N/A", "N/A"), ("Freshman", "Freshman"), ("Sophmore", "Sophmore"), ("Junior", "Junior"), ("Senior", "Senior"), ("Master", "Master"), ("PhD", "PhD"))
    post_date = models.DateField(auto_now_add=True)
    salary = models.FloatField()
    university = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=30, default="N/A")
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    grade_year = models.CharField(max_length=20, choices=YEARS, default="N/A")
    gpa = models.FloatField(blank=True, null=True)
    jobs_applied = models.CharField(max_length=20, blank=True)
    job_role = models.CharField(max_length=30, default="Software Engineer")
    housing = models.CharField(max_length=30, default="No Housing Support")
    housing_amount = models.IntegerField(default=0, blank=True, null=True)
    prev_exp_num = models.CharField(max_length=10)
    prev_exp_detail = models.TextField(max_length=300, blank=True)
    comment = models.TextField(max_length =1500, blank=True)
    
class Company(models.Model):
    cp = models.IntegerField()
