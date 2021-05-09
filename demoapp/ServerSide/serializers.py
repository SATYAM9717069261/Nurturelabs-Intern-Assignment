from rest_framework import serializers
from ServerSide.models import Advisor,User,booking

"""    Advisorid = serializers.IntegerField(read_only=True)
    name=serializers.CharField(required=False, allow_blank=True, max_length=200)
    photourl=serializers.CharField(required=False, allow_blank=True, max_length=200)
    isdelete=serializers.BooleanField(required=False,allow_null=True)
    AssignUser=serializers.CharField(required=False, allow_blank=True, max_length=200)

    def create(self,validated_data):
        return Advisor.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.photourl=validated_data.get('img',instance.photourl)
        instance.isdelete=validated_data.get('isdelete',instance.isdelete)
        instance.AssignUser=validated_data.get('user',instance.AssignUser) """

class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Advisor
        fields=['Advisorid','name','isdelete','AssignUser']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['Userid','name','email','password','isdelete','AssignAdvisor']

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=booking
        order_with_respect_to = 'Advisorid'
        order_with_respect_to = 'Userid'
        fields=['Advisorid','Userid','createdon','modifyon','isdelete','bookingTime']
        



    