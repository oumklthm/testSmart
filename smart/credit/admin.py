from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(DemandeDePret)
admin.site.register(Bank)
admin.site.register(Client)
admin.site.register(Account)
admin.site.register(Withdraw)
admin.site.register(Deposit)