from django import forms

from .models import Choice


class PollForm(forms.Form):
    choices = forms.ChoiceField(widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)
        question_id = self.initial['question_id']
        qs = Choice.objects.filter(question__id=question_id)
        choices = [(i.id, i.choice_text) for i in qs]
        self.fields['choices'].choices = choices
        self.fields['choices'].label = ""
