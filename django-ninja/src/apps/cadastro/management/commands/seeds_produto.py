# ./src/cadastro/management/commands/seeds_produto.py

from django.core.management.base import BaseCommand
from ...models.produto import Produto

class Command(BaseCommand):
    help = 'Cria seeds para a entidade Produto'

    def handle(self, *args, **kwargs):
        Produto.objects.get_or_create(nome='Fumo Superbom', defaults={'preco': 8.8, 'quantidade': 15, 'ativo': True})
        Produto.objects.get_or_create(nome='Leite de morcego', defaults={'preco': 15.21, 'quantidade': 11, 'ativo': True})
        Produto.objects.get_or_create(nome='Biscoito', defaults={'preco': 11.24, 'quantidade': 154, 'ativo': True})
        Produto.objects.get_or_create(nome='Velho Barreiro', defaults={'preco': 9.25, 'quantidade': 145, 'ativo': True})

        self.stdout.write(self.style.SUCCESS('Seeds para Produto criados com sucesso!'))