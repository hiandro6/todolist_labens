from django.core.management.base import BaseCommand
from tasks.models import Task
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Popula o banco com 15 tarefas'

    def handle(self, *args, **kwargs):
        statuses = ['nova', 'andamento', 'concluida', 'cancelada']

        for i in range(15):
            prazo = date.today() + timedelta(days=random.randint(1, 30))

            # algumas tarefas terão data de conclusão, outras não
            if random.choice([True, False]):
                data_conclusao = prazo + timedelta(days=random.randint(-5, 5))
            else:
                data_conclusao = None

            Task.objects.create(
                titulo=f'Tarefa {i+1}',
                descricao='Descrição automática gerada pelo script',
                prazo=prazo,
                data_conclusao=data_conclusao,
                situacao=random.choice(statuses)
            )

        self.stdout.write(self.style.SUCCESS(' 15 tarefas criadas com sucesso!'))