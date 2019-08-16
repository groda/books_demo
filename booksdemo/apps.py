from django.apps import AppConfig
 
 
class BooksdemoConfig(AppConfig):
    name = 'booksdemo'
    verbose_name = 'Books Application'
 
    def ready(self):
        print("app ready")

