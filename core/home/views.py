from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import PeopleSerializer

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
        print(request.GET.get('search'))#search to display the name
        print('You Hit a GET Method')
        return Response(courses)
    elif request.method=="POST":
        data=request.data
        #get the data 
        # from the postman and change the method to post and click raw and click plaintext to json 
        # type the data and click send
        print(data['name'])#get the data key
        print('You Hit a POST Method')
        return Response(courses)
    elif request.method=="PUT":
        print('You Hit a PUT Method')
        return Response(courses)


# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE'])
# Post method two pass value and it wil display and save then GET method get the data from models
def person(request):
    if request.method=='GET':
        objs=Person.objects.all() #fetch all the object from the db
        serializer=PeopleSerializer(objs,many=True)
        # the serializer serialize the object the list contains two or many objects so we use many=True
        return Response(serializer.data)
    elif request.method=='POST':
        data=request.data
        serializer=PeopleSerializer(data=data)
        # if the serializer in post we input the data the value it will check the data is serializedor not
        #whether the data is validated or not to check we use if statement
        if serializer.is_valid():
            # it will check the field is if it is empty it will show required message
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    #PUT,PATCH -Its is used for update the data
    #PUT-doesnt support partial update, you need to pass all data new data will replace the old data
    elif request.method=='PUT':
        data=request.data
        serializer=PeopleSerializer(data=data)
        # if the serializer in put we input the data the value it will check the data is serializedor not
        #whether the data is validated or not to check we use if statement
        if serializer.is_valid():
            # it will check the field is if it is empty it will show required message
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    #Patch -It supports partial updatae in this method .you need to update the particular field will be pass on it
    elif request.method=='PATCH':
        data=request.data
        #get the model id and use as a input on it
        objs=Person.objects.get(id=data['id'])
        serializer=PeopleSerializer(objs,data=data,partial=True)
        # if the serializer in patch we input the data the value it will check the data is serializedor not
        #whether the data is validated or not to check we use if statement
        if serializer.is_valid():
            # it will check the field is if it is empty it will show required message
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # DELETE - It will delete by using ID
    else:
        data=request.data
        #get the model id and use as a input on it
        objs=Person.objects.get(id=data['id'])
        # return Response({objs.id})
        objs.delete()
        return Response({"message :person deleted"})



