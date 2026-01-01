import pywhatkit as kit
import time

# Configuración
telefono = "+51943639137"  # Incluye código de país
mensaje = "Tu mensaje aquí"
hora = 21  # 11 PM
minuto = 37


# Enviar
kit.sendwhatmsg(telefono, mensaje, hora, minuto)