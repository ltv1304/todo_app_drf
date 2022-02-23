from django.core.management.base import BaseCommand
from service_user.models import ServiceUser
from django.core.management import call_command
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = '''Создание тестовых пользователей
            для создания одного пользователя вызовите команду без аргументов
            для создания нескольких пользователей вызовите команду с ключем
            -n и параметром с количеством требуемых пользователей
            для создания суперпользователя вызовите команду c ключем -s'''

    def handle(self, *args, **options):
        call_command('makemigrations')
        call_command('migrate')

        for i in range(options.setdefault('users_num', 1)):
            ServiceUser.objects.create(
                                        username = f'test_{i}',
                                        firstname = f'test_first_name_{i}',
                                        lastname = f'test_last_name_{i}',
                                        email = f'test_{i}@mail.ru',
                                        )
        
        if options['users_num']:
            User.objects.create_superuser('root', 'root@root.com', 'root')

    def add_arguments(self, parser):
        parser.add_argument(
                            '-n', 
                            '--users_num',
                            action='store', 
                            default=1,
                            type=int,
                            help='Задать количество создаваемых тестовых пользователей'
                            )
        parser.add_argument(
                            '-s', 
                            '--super',
                            action='store_true', 
                            default=False,
                            help='Cоздать суперпользователя'
                            )
