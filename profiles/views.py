from django.shortcuts import render, get_object_or_404, reverse
from django.views import View
from django.views.generic.edit import UpdateView
from .models import Profile
from videos.models import Video

# для удаления профиля
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
import os
import shutil


class ProfileView(View):

    def get(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=pk)
        videos = Video.objects.all().filter(uploader=pk).order_by('-date_posted')

        context = {
            'profile': profile,
            'videos': videos,
        }

        return render(request, 'profiles/profile.html', context)


class UpdateProfile(UpdateView):
    model = Profile
    fields = ['name', 'location', 'image']
    template_name = 'profiles/update_profile.html'

    def form_valid(self, form):
        if not form.instance.image:
            form.instance.image = 'uploads/profile_pics/default_user_pics.png'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})


# Delete Profile
def delete_profile(request):
    return render(request, 'profiles/delete_profile.html')


def delete_user_profile(request, username):
    user = get_object_or_404(User, username=username)

    if user == request.user:
        # Получаем профиль пользователя
        user_profile = get_object_or_404(Profile, user=user)

        # Удаляем файлы пользователя
        if os.path.exists(user_profile.name):
            shutil.rmtree(user_profile.name)

        # Удаляем профиль пользователя
        user.delete()

        return redirect('index')
    else:
        return redirect('index')
