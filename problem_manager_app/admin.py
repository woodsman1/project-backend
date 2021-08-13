from django.contrib import admin
from .models import Platform, Tag, UnsolvedProblem, SolvedProblem, Problem

# Register your models here.
admin.site.register(Platform)
admin.site.register(Tag)
admin.site.register(Problem)
admin.site.register(SolvedProblem)
admin.site.register(UnsolvedProblem)