from django import forms


class CountrySelectForm(forms.Form):
    CHOICES = {"1": "First", "2": "Second"}
    selected_country = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    #selected_country = forms.CharField(label='Select country:', widget=forms.Select(choices={'hel', 'tal'}, )) 


#CHOICES = {"1": "First", "2": "Second"}
#choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)