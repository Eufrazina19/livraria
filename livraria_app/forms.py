from django.forms import ModelForm
from . models import Publisher


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
