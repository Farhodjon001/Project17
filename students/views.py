from django.shortcuts import render
from .models import Student
from django.http import JsonResponse
# Create your views here.

def get_all(request):
    if request.method=="GET":
        all_date= Student.objects.all()
        result=[]
        for student in all_date:
             result.append({"id":student.id,"student_name":student.f_name})
        return JsonResponse({"date":result})

def get_by_id(request,student_id):
    if request.method=="GET":
        try:
            date=Student.objects.get(id=student_id)
        except Student.DoesNotExists:
            return JsonResponse({"msg": "NOT FOUND"})
        return JsonResponse({"id":date.id,"student_name":date.f_name})









