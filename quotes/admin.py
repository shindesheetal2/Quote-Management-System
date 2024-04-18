from django.contrib import admin
from .models import Quotes, Author

# Register your models here.

admin.site.register([Quotes, Author])
