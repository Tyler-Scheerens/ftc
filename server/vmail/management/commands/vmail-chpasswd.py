"""
Chpasswd command for existing mail users to change their password.
"""

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ValidationError

from vmail.models import MailUser, Domain


class Command(BaseCommand):
    help = ('Reset a mail users password, given their email address\n'
            'and current password. By default the passwords must be\n'
            'supplied in clear-text, and are cryptographically hashed\n'
            'by chpasswd.')
            
    def add_arguments(self, parser):
        parser.add_argument('email', help='email')
        parser.add_argument('password', help='password')
        parser.add_argument('new-password', help='new-password')

    def handle(self, *args, **options):
        email = options['email']
        curr = options['password']
        new = options['new-password']

        try:
            user = MailUser.get_from_email(email)
        except ValidationError:
            raise CommandError('Improperly formatted email address.')
        except Domain.DoesNotExist:
            raise CommandError('Domain does not exist.')
        except MailUser.DoesNotExist:
            raise CommandError('Username does not exist.')

        authorized = user.check_password(curr)
        if not authorized:
            raise CommandError('Incorrect password.')

        user.set_password(new)
        user.save()
        self.stdout.write('Success.\n')
