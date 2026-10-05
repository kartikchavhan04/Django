from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated


class StudentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        students = Student.objects.all()

        serializer = StudentSerializer(
            students,
            many=True
        )

        return Response(serializer.data)


    def post(self, request):

        print("POST REQUEST DATA:", request.data)

        serializer = StudentSerializer(
            data=request.data
        )

        if serializer.is_valid():

            student = serializer.save()

            print("STUDENT CREATED:", student.id)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        print("VALIDATION ERRORS:", serializer.errors)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class StudentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_student(self, student_id):

        try:

            return Student.objects.get(
                id=student_id
            )

        except Student.DoesNotExist:

            return None


    def get(self, request, student_id):

        student = self.get_student(student_id)

        if student is None:

            return Response(
                {
                    "error": "Student not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StudentSerializer(student)

        return Response(serializer.data)


    def put(self, request, student_id):

        student = self.get_student(student_id)

        if student is None:

            return Response(
                {
                    "error": "Student not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    def delete(self, request, student_id):

        student = self.get_student(student_id)

        if student is None:

            return Response(
                {
                    "error": "Student not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        student.delete()

        return Response(
            {
                "message": "Student deleted successfully"
            },
            status=status.HTTP_200_OK
        )