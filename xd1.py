import pyautogui
import time
import webbrowser

def enviar_mensaje(telefono, mensaje):
    # Abrir WhatsApp Web
    webbrowser.open(f"https://web.whatsapp.com/send?phone={telefono}&text={mensaje}")
    
    # Esperar que cargue
    print("⏳ Esperando 15 segundos para que cargue...")
    time.sleep(15)
    
    # Presionar Enter
    pyautogui.press('enter')
    print("✅ Mensaje enviado")

# Usar
enviar_mensaje("51943639137", "Tu mensaje")