from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm

# Added by Karthika V
from django.shortcuts import render ,redirect


def search_author(request):
    if request.method == "POST":
        searched = request.POST['searched']
        # print(searched)
        # Doing DB search here
        authors = NewsStory.objects.filter(author__username__contains = searched)
        return render(request,'news/search_by_author.html',{'searched':searched,'authors':authors})
        
    else:
        return render(request,'news/search_by_author.html',{})

def post_delete(request,pk):
    story = NewsStory.objects.get(id=pk)
    
    if request.method == "POST":
        story.delete()
        return redirect('news:index')
    
    return render(request,'news/post_delete.html',{'story':story})

def post_edit(request,pk):
    story = NewsStory.objects.get(id=pk)
    form = StoryForm(instance=story)

    if request.method == "POST":
        
        form = StoryForm(request.POST,instance=story)
        if form.is_valid():
            form.save()
            
            return redirect('news:index')

    return render(request,'news/post_edit.html',{'form':form})

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MyStoriesView(generic.ListView):
    template_name ='news/myStories.html'

    def get_queryset(self):
        return NewsStory.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_stories'] = NewsStory.objects.filter(author=self.request.user)
        return context
