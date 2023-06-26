from django.forms import ModelForm
from ordenamiento.models import Parroquia, Barrio

# rear formularios basados ​​en los modelos 'Parroquia' y 'Barrio'
#es una clase de formulario que hereda de ModelForm. Se asocia al modelo `Parroquia

class ParroquiaForm(ModelForm): 
    class Meta:
        model = Parroquia
        fields = ['nombre', 'tipo'] 



#los datos del formulario. 

class BarrioForm(ModelForm): 
    class Meta:
        model = Barrio
        fields = ['nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios', 'parroquia'] 

class BarrioEditForm(ModelForm): 
    class Meta:
        model = Barrio
        exclude = ['parroquia']