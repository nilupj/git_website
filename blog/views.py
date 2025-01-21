from django.shortcuts import render

from django.shortcuts import render, reverse

def blog_post_detail(request, slug):
    # ... your existing code to fetch the blog post ...

    context = {
        # ... your existing context variables ...
        'conditions_a_z_url': reverse('conditions_a_z'), 
    }

    return render(request, 'blog/post_detail.html', context)



from django.shortcuts import render
from .models import HealthCondition
from itertools import groupby

def health_topics(request):
    topics = HealthCondition.objects.order_by('name')
    grouped_topics = {
        letter: list(items)
        for letter, items in groupby(topics, key=lambda x: x.name[0].upper())
    }
    return render(request, 'blog/health_topics.html', {'grouped_topics': grouped_topics})

# blog/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Topic  # Assuming you have a Topic model

class TopicDetailView(DetailView):
    model = Topic
    template_name = 'blog/topic_detail.html'  # Specify the template for this view
    context_object_name = 'topic'  # The context variable name that will be used in the template

    # Optionally, you can add a get_queryset method to filter or customize the queryset.
    # def get_queryset(self):
    #     return Topic.objects.all()

