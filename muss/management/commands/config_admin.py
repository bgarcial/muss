from shutil import copyfile

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from muss.utils import create_folder, exists_folder


class Command(BaseCommand):
    help = "Create data for admin-interface."

    def handle(self, *args, **options):
        # Load fixture theme
        call_command(
            'loaddata', 'conf/theme.json',
            app_label='admin_interface'
        )

        # Create media folder if this not exists
        media_folder = settings.MEDIA_ROOT + "/"
        if not exists_folder(media_folder):
            create_folder(media_folder)

        # Create admin-interface folder if this not exists
        media_folder_admin = media_folder + "admin-interface/"
        if not exists_folder(media_folder_admin):
            create_folder(media_folder_admin)

        # Create logo folder if this not exists
        media_folder_admin_logo = media_folder_admin + "logo/"
        if not exists_folder(media_folder_admin_logo):
            create_folder(media_folder_admin_logo)

        # Copy logo admin
        logo_name = "muss.png"
        src_file = settings.STATICFILES_DIRS[0] + "/img/" + logo_name
        copyfile(src_file, media_folder_admin_logo + logo_name)

        self.stdout.write("Finished work.")
