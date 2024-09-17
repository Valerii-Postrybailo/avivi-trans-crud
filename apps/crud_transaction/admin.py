from django.contrib import admin

from .models import User, Balance, Transaction

admin.site.register(User)
admin.site.register(Balance)
admin.site.register(Transaction)
