from django import template
from arriendo_app.views import user_data_complete  # Importa la función que verifica si los datos están completos

register = template.Library()

@register.filter
def user_data_complete_filter(user):
    return user_data_complete(user)
