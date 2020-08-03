from django import forms


class countryEnterForm(forms.Form):
    countryName = forms.CharField(max_length=30, label="Country Name",widget=forms.TextInput(attrs={'placeholder': 'enter country name'}))
