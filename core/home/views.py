from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','PUT'])
def index(request):
    courses={
        'course_name':'Python',
        'learn':['flask','django'],
        'course_provider':'Coursera',
    }
    return Response(courses)

# Create your views here.
