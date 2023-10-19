from rest_framework import serializers 
from .models import feedback 

class feedbackSerializers(serializers.ModelSerializer): 
    class meta: 
        model=feedback 
        fields='__all__'