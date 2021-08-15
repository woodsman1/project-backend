from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Problem, SolvedProblem, UnsolvedProblem
from users.models import CustomUser

@receiver(post_save, sender=Problem)
def create_problem(sender, instance, created, **kwargs):
    if created:
        problem = instance
        user = problem.linked_user
        p = None
        if(problem.solved):
            p = SolvedProblem.objects.get(linked_user=user)
            if p is None:
                p = SolvedProblem.objects.create(linked_user=user, solved_count=0)
            p.solved_problems.add(problem)
            p.solved_count += 1
        else:
            p = UnsolvedProblem.objects.get(linked_user=user)
            if p is None:
                p = UnsolvedProblem.objects.create(linked_user, unsolved_count=0)
            p.unsolved_problems.add(problem)
            p.unsolved_count += 1       