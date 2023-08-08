from rest_framework.decorators import api_view
from rest_framework.response import Response

#@api view - convert a function into api view json drf response

# serializer -serializer is a concept that converts a query set into json format and viceversa
#and save a data into database is called deserializer.class which helps you to serialize the data in the form
#queryset to json response and viceversa 

#most use serializer is model view serializer


@api_view(['GET','POST','PUT'])
def index(request):
    courses={
            'course_name':'Python',
            'learn':['flask','django'],
            'course_provider':'Coursera',
        }
    if request.method=="GET":
        print(request.GET.get('search'))
        print('You Hit a GET Method')
        return Response(courses)
    elif request.method=="POST":
        data=request.data
        print(data)
        print('You Hit a POST Method')
        return Response(courses)
    elif request.method=="PUT":
        print('You Hit a PUT Method')
        return Response(courses)


# Create your views here.
