import requests
from rest_framework import serializers
from .models import Course, StudentCourse


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentCourseSerializer(serializers.ModelSerializer):
    student_details = serializers.SerializerMethodField()

    class Meta:
        model = StudentCourse
        fields = ['id', 'student_id', 'course', 'student_details']

    def get_student_details(self, obj):
        try:
            url = f"http://localhost:8081/api/students/{obj.student_id}"
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            return {"error": "Student not found"}
        except:
            return {"error": "Spring Boot service unavailable"}
