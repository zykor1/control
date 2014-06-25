from django import forms

class DonacionForm(forms.Form):
    metodo = forms.CharField(max_length=30)
    comentario = forms.CharField(widget=forms.Textarea)
    cantidad = forms.DecimalField(max_digits=9, decimal_places=2, localize=True)