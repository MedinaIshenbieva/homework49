from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import IssueTrackerForm
from webapp.models import IssueTracker


class IndexView(View):
    def get(self, request, *args, **kwargs):
        issue_tracker = IssueTracker.objects.order_by("updated_at")
        return render(request, 'index.html', {'issue_tracker': issue_tracker})


class CreateIssueTrackerView(View):
    def get(self, request, *args, **kwargs):
        form = IssueTrackerForm()
        return render(request, 'issue_tracker_create.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = IssueTrackerForm(data=request.POST)
        if form.is_valid():
            summary = form.cleaned_data.get('summary')
            status = form.cleaned_data.get('status')
            type = form.cleaned_data.get('type')
            new_issue_tracker = IssueTracker.objects.create(summary=summary, status=status, type=type)
            return redirect("issue_tracker_view", pk=new_issue_tracker.pk)
        return render(request, 'issue_tracker_create.html', {"form": form})


class IssueTrackerView(TemplateView):
    # template_name = "article_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = get_object_or_404(IssueTracker, pk=kwargs.get("pk"))
        type = get_object_or_404(IssueTracker, pk=kwargs.get("pk"))
        context['status', 'type'] = status, type
        return context


class IssueTrackerUpdateView(View):
    def get(self, request, *args, **kwargs):
        issue_tracker = get_object_or_404(IssueTracker, pk=kwargs.get("pk"))
        form = IssueTrackerForm(initial={
            'summary': issue_tracker.summary,
            'status': issue_tracker.status,
            'type': issue_tracker.type
        })
        return render(request, 'issue_tracker_update.html', {"issue_tracker": issue_tracker, "form": form})

    def post(self, request, *args, **kwargs):
        form = IssueTrackerForm(data=request.POST)
        issue_tracker = get_object_or_404(IssueTracker, pk=kwargs.get("pk"))
        if form.is_valid():
            issue_tracker.summary = request.POST.get('summary')
            issue_tracker.status = request.POST.get('status')
            issue_tracker.type = request.POST.get('type')
            issue_tracker.save()
            return redirect("issue_tracker_view", pk=issue_tracker.pk)
        return render(request, 'issue_tracker_update.html', {"issue_tracker": issue_tracker, "form": form})


class IssueTrackerDeleteView(View):
    def get(self, request, *args, **kwargs):
        issue_tracker = get_object_or_404(IssueTracker, pk=kwargs.get("pk"))
        return render(request, 'issue_tracker_delete.html', {'issue_tracker': issue_tracker})

    def post(self, request, *args, **kwargs):
        issue_tracker = get_object_or_404(IssueTracker, pk=kwargs.get("pk"))
        issue_tracker.delete()
        return redirect("index")

