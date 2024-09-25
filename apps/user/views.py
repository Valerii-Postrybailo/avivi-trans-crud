from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse


from .models import TelegramUser
from .forms import TelegramUserForm


class TelegramUserView(View):
    template_users_list = 'tg_users.html'

    def get(self, request):
        tg_users_list = TelegramUser.objects.all()

        return render(request, self.template_users_list, {'tg_users_list': tg_users_list})

    def post(self, request):
        form = TelegramUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('tg_users_list'))

        return render(request, self.template_users_list, {'form': form})

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        telegram_user = get_object_or_404(TelegramUser, telegram_id=user_id)
        telegram_user.delete()

        return HttpResponse(status=204)

