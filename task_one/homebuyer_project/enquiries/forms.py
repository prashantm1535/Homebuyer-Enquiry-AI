from django import forms

class PredictForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    age = forms.IntegerField(min_value=18, max_value=100)
    income = forms.IntegerField(min_value=0)
    city = forms.CharField(max_length=100)
    property_type = forms.ChoiceField(choices=[('1BHK','1BHK'),('2BHK','2BHK'),('3BHK','3BHK'),('Villa','Villa')])
    budget = forms.IntegerField(min_value=0)
    followups = forms.IntegerField(min_value=0, max_value=20)
    site_visited = forms.BooleanField(required=False)
