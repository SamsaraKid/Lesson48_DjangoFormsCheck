from django import forms
from django.core.validators import ValidationError, RegexValidator

class UserFormComment(forms.Form):
    name = forms.CharField(label='Имя', max_length=10)
    email = forms.EmailField(label='Почта', required=False)
    comm = forms.CharField(label='Комментарий', widget=forms.Textarea)


class UserFormErrors(forms.Form):
    name = forms.CharField(error_messages={'required': 'требуется заполнить'})
    num = forms.IntegerField(error_messages={'invalid': 'нецелое число', 'required': 'требуется заполнить'})
    agree = forms.BooleanField(error_messages={'required': 'поставьте галочку'})



#проверки
def p1(value):
    if value[0] != 'A':
        raise forms.ValidationError('не начинается на A')

def p2(value):
    if value[-1] != 'z':
        raise forms.ValidationError('не оканчивается на z')

class UserFormValidator(forms.Form):
    name = forms.CharField()
    code = forms.CharField(validators=[p1, p2])
    tel = forms.CharField(validators=[RegexValidator('[+7][0-9]{9}', message='неправильный телефон')])