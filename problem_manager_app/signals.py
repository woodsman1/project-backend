from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Problem, SolvedProblem, UnsolvedProblem

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
            p.save()
        else:
            p = UnsolvedProblem.objects.get(linked_user=user)
            if p is None:
                p = UnsolvedProblem.objects.create(linked_user=user, unsolved_count=0)
            p.unsolved_problems.add(problem)
            p.unsolved_count += 1       
            p.save()

@receiver(post_save, sender=Problem)
def updated_problem(sender, instance, created, **kwargs):
    if created == False:
        problem = instance
        user = problem.linked_user
        p = None
        if(problem.solved):
            p = SolvedProblem.objects.get(linked_user=user)
            up = UnsolvedProblem.objects.get(linked_user=user)
            if p is None:
                p = SolvedProblem.objects.create(linked_user=user, solved_count=0)
            up.unsolved_problems.remove(problem)
            up.unsolved_count -= 1
            up.save()
            p.solved_problems.add(problem)
            p.solved_count += 1
            p.save()
        else:
            p = UnsolvedProblem.objects.get(linked_user=user)
            sp = SolvedProblem.objects.get(linked_user=user)
            if p is None:
                p = UnsolvedProblem.objects.create(linked_user=user, unsolved_count=0)
            sp.solved_problems.remove(problem)
            sp.solved_count -=1
            sp.save()
            p.unsolved_problems.add(problem)
            p.unsolved_count += 1
            p.save()