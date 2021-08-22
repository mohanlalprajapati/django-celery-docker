from django.shortcuts import render
from .forms import AdditionForm
from django.views import View
from django.urls import reverse
from celery.result import AsyncResult


def show_task_results(request, task_id):
    #get task results
    res = AsyncResult(task_id)
    return render(request, 'core/results.html', {'task_result': res.result})


class AdditionView(View):
    form_class = AdditionForm
    initial = {'a': '', 'b': ''}
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            result = form.submit()
            return render(request, 'core/working_progress.html',
                          context={'task_id': result.task_id,
                                   'redirect_url': reverse('core:show_task_result',
                                                           kwargs={"task_id": result.task_id})})

        return render(request, self.template_name, {'form': form})
