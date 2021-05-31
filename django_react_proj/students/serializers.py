from rest_framework import serializers
from .models import Interns

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interns
        fields = ('pk', 'post_date', 'salary', 'university', 'state', 'country', 'city', 'company', 'grade_year' , 'gpa', 'jobs_applied', 'housing', 'housing_amount', 'job_role', 'prev_exp_num', 'prev_exp_detail', 'comment')

