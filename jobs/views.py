from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DayArchiveView
from django.urls import reverse_lazy
from .models import Job,Application
from .forms import Jobform

class JobListView(ListView):
  model=Job
  template_name='jobs/job_list.html'
  context_object_name='all_jobs'

class JobDetailsView(DetailView):
    model = Job
    template_name = 'jobs/job_details.html'
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['already_applied'] = False

        if self.request.user.is_authenticated:
            context['already_applied'] = Application.objects.filter(
                job=self.object,
                applicant=self.request.user,
            ).exists()

        return context




