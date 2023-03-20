from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer


# Create your views here.

class TrainerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('homepage')
    permission_required = 'trainer.view_trainer'

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_trainer = form.save(commit=False)  # opresc salvarea in tabela
            new_trainer.first_name = new_trainer.first_name.title()  # modific valoarea completata de utilizator in asa fel incat sa fie salvata format title()
            new_trainer.total = new_trainer.price * new_trainer.hours
            new_trainer.save()  # salvez trainer in tabela trainer_trainer

        return redirect('homepage')


class TrainerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'
    permission_required = 'trainer.view_list_of_trainers'

    def get_queryset(self):
        return Trainer.objects.filter(active=True)


class TrainerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm
    success_url = reverse_lazy('list-of-trainers')
    permission_required = 'trainer.change_trainer'


@login_required()
@permission_required('trainer.inactivate_trainer', raise_exception=True)
def inactivate_trainer(request, pk):
    Trainer.objects.filter(id=pk).update(active=False)
    return redirect('list-of-trainers')


class TrainerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'trainer/delete_trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-of-trainers')
    permission_required = 'trainer.delete_trainer'
