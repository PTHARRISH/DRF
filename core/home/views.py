from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST','PUT'])
def index(request):
    courses={
            'course_name':'Python',
            'learn':['flask','django'],
            'course_provider':'Coursera',
        }
    if request.method=="GET":
        print('You Hit a GET Method')
        return Response(courses)
    elif request.method=="POST":
        print('You Hit a POST Method')
        return Response(courses)
    elif request.method=="PUT":
        print('You Hit a PUT Method')
        return Response(courses)


# Create your views here.
