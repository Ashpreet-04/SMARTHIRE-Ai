from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from django.contrib.auth.models import User
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="hradmin",
                email="Arshsidhu0404@gmail.com",
                password="Arsh##@0404"
            )
