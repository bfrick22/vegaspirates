# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.views import generic

from .models import Choice, Question
from .forms import PollForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class VoteView(generic.edit.FormView):
    template_name = 'polls/vote.html'
    form_class = PollForm
    model = Choice
    success_url = "../results"

    def get_initial(self, **kwargs):
        initial = super(VoteView, self).get_initial(*kwargs)
        initial['question_id'] = self.kwargs.get("question_id")
        return initial

    def get_context_data(self, **kwargs):
        context = super(VoteView, self).get_context_data(**kwargs)
        context['question_id'] = self.kwargs.get("question_id")
        return context

    def form_valid(self, form):
        choices = form.data.get('choices')
        if choices:
            choice_id = reduce(lambda x: x, choices)
            self.model.vote(choice_id)
        return super(VoteView, self).form_valid(form)
