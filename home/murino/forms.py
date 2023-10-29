from django import forms

from .models import Occupant


class OccupantForm(forms.ModelForm):

    class Meta:
        model = Occupant
        fields = ('name', 'nickname', 'page_name', 'age', 'date_of_birth', 'avatar', 'hobbies')
