from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        username = "hradmin"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email="Arshsidhu0404@gmail.com",
                password="Arsh##@0404"
            )
