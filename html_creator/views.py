from django.shortcuts import render
from rest_framework import viewsets
from .models import HtmlCreatorModel
from .serializers import HtmlCreatorSerializer
from .filters import HtmlCreatorFilter
from datetime import date
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class HtmlCreatorMVS(viewsets.ModelViewSet):
    queryset = HtmlCreatorModel.objects.all()
    serializer_class = HtmlCreatorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = HtmlCreatorFilter
    def get_queryset(self):
        today = date.today()
        return HtmlCreatorModel.objects.filter(last_updated__date=today)