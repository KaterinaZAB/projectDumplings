from django import forms


class contact_form(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder':'Ваше имя'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Ваш email'}
        )
    )
    message = forms.CharField(
        min_length =20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Сообщение'}
        )
    )