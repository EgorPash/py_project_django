from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import BlogPost
from django.forms import BlogPostForm


class BlogPostListView(ListView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'
    success_url = reverse_lazy('blog:blogpost_list')

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        post.views_count += 1
        post.save()
        return post


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'preview_image', 'is_published']
    template_name = 'blog/blogpost_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.title)
        self.object.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'preview_image', 'is_published']
    template_name = 'blog/blogpost_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:blogpost_detail', args=[self.object.pk])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog:blogpost_list')
