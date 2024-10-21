from rest_framework import serializers
# from django import forms
from .models import SiteUser
from rest_framework.validators import UniqueValidator

from utils.datetime.datetimeutils import *
from utils.validation.stringvalidation import *
from utils.exceptions.fieldvalueexception import *

class SiteUsersSerializer(serializers.ModelSerializer):
    # last_modify = serializers.DateTimeField(source='modified_at') # Working 
    last_modify = serializers.SerializerMethodField('get_last_modify') 
    class Meta:
        model = SiteUser
        # exclude = ('id','password', 'created_at')
        # fields = '__all__'
        fields = ('user_id', 'user_name', 'first_name', 'middle_name', 'last_name', 'full_name', 'is_active', 'last_modify')

        '''extra_kwargs = {
            "user_name": {
                "error_messages": 
                    {"required": "user name required", 'blank': "user name sould not blank"},
                    'validators': [
                        UniqueValidator(queryset=SiteUser.objects.all(), message="user name already exist")
                    ]
                },
            "first_name": {"error_messages": {"required": "first name required", 'blank': "first name sould not blank"}},
            "last_name": {"error_messages": {"required": "last name required", 'blank': "last name sould not blank"}},
            "password": {"error_messages": {"required": "password required", 'blank': "password sould not blank"}},
        }'''

    def get_last_modify(self, obj):
        return DateTimeUtils().date_to_str(obj.modified_at, "%Y-%m-%d")
    
    '''def validate(self, data):
        if StringValidation().name_validation(data.get('first_name').lower()) == False :
            # raise serializers.ValidationError('start date mast be less then end date')
            raise FieldvalueException('please enter valid value', 'first_name')
        return data'''
    

class SiteUsersSerializerFormValidate(serializers.ModelSerializer):
    # last_modify = serializers.DateTimeField(source='modified_at') # Working 
    class Meta:
        model = SiteUser
        # exclude = ('id', 'full_name', 'last_modify', 'created_at')
        # fields = '__all__'
        fields = ('user_name', 'first_name', 'middle_name', 'last_name', 'password', 'is_active')

        extra_kwargs = {
            "user_name": {
                "error_messages": 
                    {"required": "user name required", 'blank': "user name sould not blank"},
                    'validators': [
                        UniqueValidator(queryset=SiteUser.objects.all(), message="user name already exist")
                    ]
                },
            "first_name": {"error_messages": {"required": "first name required", 'blank': "first name sould not blank"}},
            "last_name": {"error_messages": {"required": "last name required", 'blank': "last name sould not blank"}},
            "password": {"error_messages": {"required": "password required", 'blank': "password sould not blank"}},
        }

    def get_last_modify(self, obj):
        return DateTimeUtils().date_to_str(obj.modified_at, "%Y-%m-%d")
    
    def validate(self, data):
        # Check user_name is UNIQUE or not
        if SiteUser.objects.filter(user_name = data.get('user_name').lower()).exists() :
            raise FieldvalueException('user name already exist', 'user_name')
        
        # Name check
        if StringValidation().name_validation(data.get('first_name').lower()) == False :
            # raise serializers.ValidationError('start date mast be less then end date')
            raise FieldvalueException('please enter valid value', 'first_name')
        if StringValidation().name_validation(data.get('last_name').lower()) == False :
            raise FieldvalueException('please enter valid value', 'last_name')
        if data.get('last_name') != None:
            if StringValidation().name_validation(data.get('last_name').lower()) == False :
                raise FieldvalueException('please enter valid value', 'last_name')
        return data
    
    def create(self):
        SiteUser().create(self.data)
    
class SiteUsersSerializerFormValidateForEdit(serializers.ModelSerializer):
    class Meta:
        model = SiteUser
        fields = ('first_name', 'middle_name', 'last_name')

        extra_kwargs = {
            "first_name": {"error_messages": {"required": "first name required", 'blank': "first name sould not blank"}},
            "last_name": {"error_messages": {"required": "last name required", 'blank': "last name sould not blank"}},
        }
    
    def validate(self, data):        
        # Name check
        if StringValidation().name_validation(data.get('first_name').lower()) == False :
            raise FieldvalueException('please enter valid value', 'first_name')
        if StringValidation().name_validation(data.get('last_name').lower()) == False :
            raise FieldvalueException('please enter valid value', 'last_name')
        if data.get('last_name') != None:
            if StringValidation().name_validation(data.get('last_name').lower()) == False :
                raise FieldvalueException('please enter valid value', 'last_name')
        return data