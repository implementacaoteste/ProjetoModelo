from django.core.management.base import BaseCommand
from django.core.management import call_command
from time import sleep

class Command(BaseCommand):
    help = 'Run the server with automatic migrations'

    def add_arguments(self, parser):
        # Adicione os argumentos do runserver
        parser.add_argument('addrport', nargs='?', default='8000',
                            help='Optional port number, or ipaddr:port')

    def handle(self, *args, **options):
        from django.conf import settings

        # Obtenha a lista de aplicativos do settings.py e remova o prefixo 'apps.' apenas dos aplicativos personalizados
        custom_apps = [app.split('apps.')[1] for app in settings.INSTALLED_APPS if app.startswith('apps.')]
        sleep(20)
        self.stdout.write('Iniciando as migrações...')
        call_command('makemigrations', *custom_apps)
        self.stdout.write('Makemigrations concluído.')
        call_command('migrate')
        self.stdout.write('Migrate concluído.')

        # Inicia o servidor
        addrport = options['addrport']
        call_command('runserver', addrport)
