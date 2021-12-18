from django.shortcuts import render, redirect, get_object_or_404
from .forms import ManagerAppForm, ManagerAppFormset
from .models import AppPost
from django.views import View


class ManagerAppView(View):
    def get(self, request, *args, **kwargs):
        post_data = AppPost.objects.all()

        return render(request, 'app/post_list.html', {
            'post_data': post_data
        })


class ManagerAppAddView(View):
    def get(self, request, *args, **kwargs):
        form = ManagerAppForm(request.POST or None)
        formset =ManagerAppFormset(request.POST or None)

        return render(request, 'app/post_form.html', {
            'form': form,
            'formset': formset
        })

    def post(self, request, *args, **kwargs):
        form = ManagerAppForm(request.POST or None)
        formset = ManagerAppFormset(request.POST or None)

        if form.is_valid():
            post = AppPost()
            formset = ManagerAppFormset(request.POST or None, instance=post)
            if formset.is_valid():
                post.title = form.cleaned_data['title']
                post.save()
                formset.save()

                post_data = AppPost.objects.all()

                return render(request, 'app/post_list.html', {
                    'post_data': post_data
                })

            return render(request, 'app/post_form.html', {
                'form': form,
                'formset': formset
            })

        return render(request, 'app/post_form.html', {
            'form': form,
            'formset': formset
        })


class ManagerAppEditView(View):
    def get(self, request, *args, **kwargs):
        post_data = AppPost.objects.get(id=self.kwargs['pk'])

        formset =ManagerAppFormset(
            request.POST or None,
            instance= post_data
        )

        form = ManagerAppForm(
            request.POST or None,
            initial = {
                'title': post_data.title
            }
        )

        return render(request, 'app/post_form.html', {
            'form': form,
            'formset': formset
        })

    def post(self, request, *args, **kwargs):
        post_data = AppPost.objects.get(id=self.kwargs['pk'])
        
        formset = ManagerAppFormset(
            request.POST or None,
            instance= post_data
        )

        form = ManagerAppForm(
            request.POST or None,
            initial = {
                'title': post_data.title
            }
        )

        if form.is_valid():
            if formset.is_valid():
                post_data.title = form.cleaned_data['title']
                post_data.save()
                formset.save()

                post_data = AppPost.objects.all()

                return render(request, 'app/post_list.html', {
                    'post_data': post_data
                })

            return render(request, 'app/post_form.html', {
                'form': form,
                'formset': formset
            })

        return render(request, 'app/post_form.html', {
            'form': form,
            'formset': formset
        })