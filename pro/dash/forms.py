from django import forms
from .models import Complaint


class UserForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ['name', 'email', 'branch',
                  'complaint_regarding', 'complaint_message']
