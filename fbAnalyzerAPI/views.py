from django.shortcuts import render

from .forms import feedbackForm 
from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser 
from .model import feedback 
from .serializer import feedbackSerializers 

import pickle
import json 
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
from django.shortcuts import render, redirect 
from django.contrib import messages 

class feedbackView(viewsets.ModelViewSet): 
    queryset = feedback.objects.all() 
    serializer_class = feedbackSerializers 

def status(df):
    try:        
        input_file = 'model_C=1.0.bin'
        with open(input_file, 'rb') as f_in: 
            model = pickle.load(f_in)       
        y_class = model.predict(df) 
        y_predProb = model.predict_proba(df) 
        result = [y_class, y_predProb]
        return result 
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 

def FormView(request):
    if request.method=='POST':
        form=feedbackForm(request.POST or None)

        if form.is_valid():
            language = form.cleaned_data['language']
            Feedback = form.cleaned_data['text']            
            df=pd.DataFrame({'news':[Feedback]})
            result = status(df)
            return render(request, 'status.html', {"data": result[0]}) 
            
    form=feedbackForm()
    return render(request, 'form.html', {'form':form})