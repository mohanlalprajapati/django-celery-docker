from django import forms
from .tasks import add
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class AdditionForm(forms.Form):
    a = forms.FloatField()
    b = forms.FloatField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
      #  self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        #self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))

    def submit(self):
        # send email using the self.cleaned_data dictionary
        a = self.cleaned_data.get('a')
        b = self.cleaned_data.get('b')
        return add.delay(a, b)
