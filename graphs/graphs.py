import pygal
from bugs.models import Bug
from features.models import Feature
from pygal.style import Style

def bug_bar_chart():
    
    """A bar chart showing the 5 most upvoted bugs in descending order"""

    bugs = Bug.objects.order_by('-upvotes')[:5]
    bar_chart = pygal.Bar(
        show_minor_y_labels=False,
        print_values=True,
        print_zeroes=False,
    )

    for bug in bugs:
        bar_chart.add(bug.name, bug.upvotes)

    return bar_chart.render()

def BugBarChart():
    
    """Enable importing the graph into a view"""
    
    chart = bug_bar_chart()
    return chart