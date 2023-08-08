from rest_framework import serializers
from .models import person
#import model class u want to serialize

#in this class we use model serializer
class PeopleSerializer(serializers.ModelSerializer):
    #to know which model to serialze we need a class one more class that is called inner class
    # the class name is meta we add a model field which automatically knows 
    # this serializer class is linked to the particular model(person model)
    class Meta:
        #model you need to paste what model to serialize
        model=person
        #the another we need to add in meta class that is what field we need to serialize 
        #if you need to serialize two fields mention the field inside a list
        # eg here we use name, age fields or 
        fields=['name','age']
        # you can type special method name(single quotes must '__all__') it will display all the fields
        # fields='__all__'
        #exclude attribute will helps to display all other fields expect those mentioned fields
        #exclude=['name']
        


