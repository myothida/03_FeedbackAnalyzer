from rest_framework import serializers 
from .model import feedback 

class feedbackSerializers(serializers.ModelSerializer): 
    class meta: 
        model=feedback 
        fields='__all__'