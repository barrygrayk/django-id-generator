from django import forms
from .models import Person
from .idgenerator import get_control_digit

class CreatePerson(forms.Form):

    name = forms.CharField()
    date_of_birth =  forms.DateField()
    gender = forms.CharField()
    country = forms.CharField()
    race = forms.CharField()

class VerifyID (forms.Form):
    id = forms.CharField(max_length=13)

    def clean_id(self):
        check_sa_id = self.cleaned_data.get("id")
        if len(str(check_sa_id)) == 13:
            sliced_id =check_sa_id[:len(str(check_sa_id))-1]
            control_id =sliced_id +str(get_control_digit(sliced_id))
            if control_id == str(check_sa_id):
                raise forms.ValidationError("This is a valid ID")
            else:
                raise forms.ValidationError("This is not a valid ID")
        else:
            raise forms.ValidationError("Your id must always be 13 digits long")
        return check_sa_id

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        super(VerifyID, self).__init__(*args, **kwargs)

class DateInput(forms.DateInput):
    input_type = 'date'

class PersonModelForm (forms.ModelForm):
    # category =forms.CharField(required=False, validators=[validate_catergories])
    class Meta:
        model = Person
        fields = [
            'name',
            'date_of_birth',
            'gender',
            'country',
            'race',
        ]
        widgets = {
            'date_of_birth': DateInput(),
        }

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        super(PersonModelForm, self).__init__(*args, **kwargs)