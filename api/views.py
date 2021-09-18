from django.shortcuts import render
from rest_framework import response
# Create your views here.


from djangochannelsrestframework.generics import GenericAsyncAPIConsumer


class UserConsumer(GenericAsyncAPIConsumer):
    # permission_classes = (permissions.IsAuthenticated,)
    pass
