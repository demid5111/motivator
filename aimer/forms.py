from django import forms

class AimForm(forms.Form):
    aim_name = forms.CharField(label='Your aim', max_length=100)
    aim_description = forms.CharField(label = 'Description', max_length=400)
    aim_bet = forms.IntegerField(label = "Bet")
    aim_type = forms.CharField(label = 'Type', max_length = 20)
    aim_finish = forms.DateTimeField(label = 'Date finish')