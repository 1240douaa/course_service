import graphene
from graphene_django.types import DjangoObjectType
from courses.models import Course, StudentCourse


class CourseType(DjangoObjectType):
    class Meta:
        model = Course

class StudentCourseType(DjangoObjectType):
    class Meta:
        model = StudentCourse

class Query(graphene.ObjectType):
    # 🔹 Tous les studentCourses
    student_courses = graphene.List(StudentCourseType)

    # 🔹 StudentCourses filtrés par ID du cours
    student_courses_by_course = graphene.List(
        StudentCourseType,
        course_id=graphene.Int(required=True)
    )

    def resolve_student_courses(root, info):
        return StudentCourse.objects.all()

    def resolve_student_courses_by_course(root, info, course_id):
        return StudentCourse.objects.filter(course__id=course_id)

schema = graphene.Schema(query=Query)
