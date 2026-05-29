from django import forms

class PredictionForm(forms.Form):
    lag_1 = forms.FloatField()
    lag_2 = forms.FloatField()
    lag_3 = forms.FloatField()
    lag_6 = forms.FloatField()
    lag_12 = forms.FloatField()
    lag_24 = forms.FloatField()
    rolling_mean_3 = forms.FloatField()
    rolling_mean_6 = forms.FloatField()
    rolling_mean_12 = forms.FloatField()
    rolling_std_3 = forms.FloatField()
    rolling_std_6 = forms.FloatField()
    momentum_3 = forms.FloatField()
    month = forms.IntegerField()
    year = forms.IntegerField()