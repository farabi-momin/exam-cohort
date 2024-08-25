from dataclasses import fields
from rest_framework import serializers
from cohort.models import cohort, cohortInfos, ExamInfo, QuesModel
from django.contrib.auth.models import User
from site import USER_BASE 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

class CohortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cohort
        fields = ('CohortID', 'CohortName','Admin') 


class cohortInfosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cohortInfos
        fields = ('id', 'cohort', 'Member', 'MemberStatus')

