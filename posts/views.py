from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from posts.models import Post, Comment, Like
from posts.forms import PostCreateForm, CommentCreateForm, LikeForm
# Create your views here.


def home_view(request):
    object_post = Post.objects.all().order_by('-created')
    object_comment = Comment.objects.all()
    users = User.objects.all()
    context = {
        'posts': object_post,
        'comments': object_comment,
        'users': users,
    }

    return render(request, 'posts/home_view.html', context=context)


def post_view(request, id):
    user = request.user
    user_like = Like.objects.filter(post=id).filter(user=user.id)
    user_comment_owner = Comment.objects.filter(post=id).filter(user=user.id)
    comment_form = CommentCreateForm(request.POST or None)
    like_form = LikeForm(request.POST or None)
    post_object = get_object_or_404(Post, id=id)
    id_comment = request.POST.get('comment_id')
    confirm_delete = request.POST.get('confirm-delete')
    context = {
        'post_object': post_object,
        'comment_form': comment_form,
        'like_form': like_form,
        'user_like': user_like.exists(),
        'user_comment_owner': user_comment_owner,

    }

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post_object
        comment.save()
        return redirect(post_object.get_absolute_url())

    elif confirm_delete == 'confirm':
        Comment.objects.get(id=id_comment).delete()
        return redirect(post_object.get_absolute_url())

    elif like_form.is_valid():
        user = request.user
        user_like = Like.objects.filter(post=id).filter(user=user.id)
        if user_like.exists():
            user_like.delete()

        else:
            like = like_form.save(commit=False)
            like.user = user
            like.post = post_object
            like.save()

        return redirect(post_object.get_absolute_url())

    return render(request, 'posts/detail.html', context=context)


@login_required
def create_view(request):
    form = PostCreateForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url())


    return render(request, 'posts/create.html', context=context)


def profile_view(request, username):
    user_profile = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user_profile.id).order_by("-created")
    # delete_post_or_comment =


    context = {
        'posts': posts,
        'user_profile': user_profile,
    }

    return render(request, 'posts/profile.html', context=context)
