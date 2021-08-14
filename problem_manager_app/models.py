from django.db import models
from users.models import CustomUser
# import users.models.CustomUser as CustomUser


class Platform(models.Model):
    platform_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.platform_name}'


class Tag(models.Model):
    tag_name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'{self.tag_name}'


class Problem(models.Model):
    linked_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    link = models.CharField(max_length=120)
    title = models.CharField(max_length=150)
    tags = models.ManyToManyField(Tag)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    notes = models.TextField()
    solved = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.id}-{self.title}'



class SolvedProblem(models.Model):
    linked_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    solved_problems = models.ManyToManyField(Problem)
    solved_count =  models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.linked_user.email} - {self.solved_count}'



class UnsolvedProblem(models.Model):
    linked_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    unsolved_problems = models.ManyToManyField(Problem)
    unsolved_count =  models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.linked_user.email} - {self.unsolved_count}'