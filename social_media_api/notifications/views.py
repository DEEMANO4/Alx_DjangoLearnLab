from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from .models import Post, Like, Notification

# Create y our views here 
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_orcreate(user=request.user, post=post)

    if created and post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb= 'liked',
            target=post
        )
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def unlike_post(request,pk):
    post = get_object_or_404(Post, pk=pk)

    Like.objects.filter(user=request.user, post=post).delete()

    content_type = ContentType.objects.get_for_model(post)
    Notification.objects.filter(
        actor=request.user,
        verb='liked',
        target_content_type=content_type,
        target_object_id=post.id
    ).delete()

    return redirect(request.META.get('HTTP_REFERER', 'home'))



#  Like.objects.filter(user=request.user, post=post).delete()
#  Notification.objects.create

