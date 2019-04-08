from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import PostCreateForm, FileFormset
from .models import Post


class PostList(generic.ListView):
    model = Post


def add_post(request):
    form = PostCreateForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        formset = FileFormset(request.POST, files=request.FILES, instance=post)  # 今回はファイルなのでrequest.FILESが必要
        if formset.is_valid():
            post.save()
            formset.save()
            return redirect('app:index')

        # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
        else:
            context['formset'] = formset

    # GETのとき
    else:
        # 空のformsetをテンプレートへ渡す
        context['formset'] = FileFormset()

    return render(request, 'app/post_form.html', context)


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostCreateForm(request.POST or None, instance=post)
    formset = FileFormset(request.POST or None, files=request.FILES or None, instance=post)
    if request.method == 'POST' and form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        # 編集ページを再度表示
        return redirect('app:update_post', pk=pk)

    context = {
        'form': form,
        'formset': formset
    }

    return render(request, 'app/post_form.html', context)
