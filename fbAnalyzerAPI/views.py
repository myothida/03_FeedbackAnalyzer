from django.shortcuts import render

from .forms import feedbackForm 
from rest_framework import viewsets 
from rest_framework.response import Response 
from rest_framework import status 
from .model import feedback 
from .serializer import feedbackSerializers 

import pickle
import numpy as np 
from googletrans import Translator
from django.shortcuts import render 

class feedbackView(viewsets.ModelViewSet): 
    queryset = feedback.objects.all() 
    serializer_class = feedbackSerializers 

def status(df):
    try:        
        input_file = './models/model_C=1.0.bin'
        with open(input_file, 'rb') as f_in: 
            cls = pickle.load(f_in)               
        y_class = cls.predict([df]) 
        y_predProb = cls.predict_proba([df]) 
        return y_class, y_predProb
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 

def FormView(request):
    if request.method=='POST':
        form=feedbackForm(request.POST or None)

        if form.is_valid():
            language = form.cleaned_data['language']
            if (language =='Burmese'):
                translator = Translator()
                Feedback_MM = form.cleaned_data['text'] 
                Feedback = translator.translate(Feedback_MM, src='my', dest='en')
            else:
                Feedback = form.cleaned_data['text']            
            y_class, y_predProb = status(Feedback)
            y_predProb = np.round(y_predProb[0][0],3)
            print("Data:",  Feedback)  # Debug output
            print("Confidence:", y_predProb)  # Debug output
            return render(request, 'form.html', {'form':form, 
                                                 "data":y_class[0].title(), "confidence":y_predProb}) 
            
    form=feedbackForm()
    return render(request, 'form.html', {'form':form})