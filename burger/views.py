from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.views.generic import ListView

from burger.forms import getInTouchForm
from burger.models import CarouselContent, BestBurger, PresidentBurger, HamburgerClient, \
    OurGallery, BlogPost, SingleBlog, GalleryImage, getInTouch


class HomePage(ListView):
    template_name = 'index.html'
    model = CarouselContent
    context_object_name = 'models'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['best_burgers'] = BestBurger.objects.all()
        context['president_burgers'] = PresidentBurger.objects.all()
        context['hamburger_clients'] = HamburgerClient.objects.all()
        return context


class MenuPage(ListView):
    template_name = 'Menu.html'
    context_object_name = 'best_burgers'
    model = BestBurger

    def get_context_data(self, **kwargs):
        context = super(MenuPage, self).get_context_data()
        context['president_burgers'] = PresidentBurger.objects.all()
        context['hamburger_clients'] = HamburgerClient.objects.all()
        return context


class AboutPageView(ListView):
    template_name = 'about.html'
    context_object_name = 'about_products'
    model = BestBurger

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data()
        context['hamburger_clients'] = HamburgerClient.objects.all()
        context['our_galleries'] = OurGallery.objects.all()
        return context


class BlogView(ListView):
    model = BlogPost
    template_name = 'blog.html'
    context_object_name = 'blog_posts'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        blog_lists = BlogPost.objects.all()
        paginator = Paginator(blog_lists, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)

        context['list_exams'] = file_exams
        return context


def SingleView(request):
    post_lists = SingleBlog.objects.all()
    paginator = Paginator(post_lists, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'post_lists': post_lists,
    }
    return render(request, 'single-blog.html', context)


class Pages(ListView):
    template_name = 'elements.html'
    context_object_name = 'elements'
    model = GalleryImage


def ContactView(request):
    error = ''
    if request.method == 'POST':
        form = getInTouchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('single-blog')
        else:
            error = 'Problems with sending forms'
    form = getInTouchForm()
    data = {
        'form': form
    }
    return render(request, 'contact.html', data)
