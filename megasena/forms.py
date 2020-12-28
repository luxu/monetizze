from django import forms


class MegasenaForm(forms.Form):
    cartelas = forms.IntegerField(
        label='Cartelas'
    )
    dezenasPorCartela = forms.IntegerField(
        min_value=6, max_value=10,
        label='Dezenas por Cartela'
    )

    def clean(self):
        pass
