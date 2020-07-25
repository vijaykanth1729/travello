from django import forms
#from django.forms import ModelForm
from .models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
class ProductForm(forms.ModelForm):
    #email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email Here'}))
    class Meta:
        model = Product
        fields = '__all__'

class OurForum(forms.Form):
    STATES = (
        ('', 'Choose...'),
        ('ap', 'AndhraPradesh'),
        ('ks', 'Karnataka'),
        ('tn', 'TamilNadu'),
    )
    email = forms.EmailField(widget= forms.TextInput(attrs={'placeholder':'Email Here'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}))
    address_1 = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder':'1234 Main St'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Apartment, studio, or floor'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('name', css_class='form-group col-md-6 mb-0'),
                css_class = 'form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'

            ),
            'check_me_out',
            Submit('submit','SendUS', css_class='btn btn-info btn-lg btn-block')

)
