import requests
import os
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
            # Utiliser l'URL de production si disponible, sinon localhost
            student_service_url = os.environ.get(
                'STUDENT_SERVICE_URL', 
                'http://localhost:8081'
            )
            url = f"{student_service_url}/api/students/{obj.student_id}"
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                return response.json()
            return {"error": "Student not found"}
        except requests.exceptions.Timeout:
            return {"error": "Student service timeout"}
        except requests.exceptions.ConnectionError:
            return {"error": "Student service unavailable"}
        except Exception as e:
            return {"error": f"Error: {str(e)}"}