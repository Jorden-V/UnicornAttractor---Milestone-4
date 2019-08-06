from django.shortcuts import render
from .graphs import BugBarChart

def graphs(request):
    """A view that displays the graphs page"""
    return render(request, "graphs.html", {'bug_bar_chart': BugBarChart})