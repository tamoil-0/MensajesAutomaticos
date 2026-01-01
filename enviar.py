import pyautogui
import webbrowser
import time
from datetime import datetime
import urllib.parse

# ═══════════════════════════════════════════════════════════
# 🎆 SCRIPT DE ENVÍO AUTOMÁTICO - AÑO NUEVO 2025
# ═══════════════════════════════════════════════════════════

mensajes = {
    "+51925139320": """✨ Feliz Año Nuevo, Dani ✨

Este año tuve la fortuna de conocerte, y sin darme cuenta te fuiste convirtiendo en alguien muy importante para mí. Cada conversación, cada momento compartido y cada risa hicieron que este año sea aún más especial. A veces las personas llegan sin aviso y terminan dejando huellas bonitas, y tú eres una de ellas.

Admiro mucho la persona que eres, tu forma de enfrentar las cosas, tu valentía y todo lo que has logrado hasta ahora. Tal vez no siempre lo notes, pero tienes una fortaleza muy linda y una luz que se siente. Valora todo lo que has conseguido, porque es fruto de tu esfuerzo y de tu corazón.

Deseo de verdad que este nuevo año te regale calma, sonrisas sinceras y momentos que te hagan sentir orgullosa de ti misma. Que sigas creciendo, aprendiendo y rodeándote de cosas bonitas. Y cuando lo necesites, recuerda que no estás sola.

Para cualquier cosa, en cualquier momento, aquí estaré. Para apoyarte, escucharte o simplemente acompañarte. Gracias por llegar a mi vida este año y por hacerlo un poco más bonito.

Te deseo un feliz Año Nuevo, Dani, lleno de paz, ilusión y nuevos comienzos ✨🤍  
Un abrazo grande.""",

    "+51940481218": """✨ Feliz Año Nuevo, Gia ✨

Ya son varios años conociéndonos y, al mirar atrás, solo puedo agradecer por todo lo compartido. Han sido conversaciones, risas, momentos buenos y otros no tanto, pero todos reales y valiosos. Tenerte como amiga ha sido una parte bonita de estos años, y eso no lo doy por sentado.

Admiro tu fortaleza y la forma en que enfrentas la vida. Todo lo que has logrado es resultado de tu esfuerzo, de tu constancia y de esa forma tan tuya de seguir adelante, incluso cuando las cosas se ponen difíciles. Valora cada paso que has dado, porque dice mucho de la persona que eres.

Deseo de corazón que este nuevo año te traiga tranquilidad, oportunidades lindas y muchas razones para sonreír. Que sigas creciendo, cumpliendo tus metas y rodeándote de personas y momentos que te hagan bien. Mereces cosas buenas y un año lleno de luz.

Y recuerda que, como siempre, aquí estaré. Para escuchar, apoyar, reír o simplemente acompañar, sin importar el momento. Gracias por tu amistad y por ser parte de mi camino durante estos años.

Te deseo un feliz Año Nuevo, Gia, con salud, paz y todo lo mejor ✨🤍  
Un abrazo grande.""",

    "+51970596690": """Feliz Año Nuevo, Angie ✨

Quería decirte algo que para mí es importante. Muchas veces dudas de ti y de lo que eres capaz de hacer, pero quiero que sepas que todo lo que has logrado es totalmente merecido. Nada ha sido suerte, todo ha sido por tu esfuerzo, tu constancia y la persona que eres.

Este año fue muy bonito compartirlo contigo. Entre conversaciones, risas y momentos de apoyo te volviste alguien muy importante para mí. Admiro mucho cómo sigues adelante incluso cuando las cosas no son fáciles, aunque a veces no lo veas así.

Deseo de corazón que este nuevo año confíes más en ti, que te valores como mereces y que te sientas orgullosa de cada paso que das. Yo siempre voy a estar orgulloso de ti.

Y para cualquier cosa, de verdad, aquí estaré. Para escucharte, apoyarte o simplemente acompañarte cuando lo necesites.

Te deseo un feliz Año Nuevo, Angie 🤍  
Un abrazo grande.""",

    "+51916035892": """Feliz Año Nuevo, Tefa ✨

Quería desearte lo mejor para este nuevo año. Gracias por los momentos compartidos y por las conversaciones a lo largo de este tiempo. Ha sido bonito coincidir y compartir, incluso en las cosas simples.

Espero que este año venga con tranquilidad, buenas oportunidades y muchas razones para sonreír. Que puedas cumplir tus metas y seguir avanzando en todo lo que te propongas.

Te deseo un feliz Año Nuevo y que venga lleno de cosas buenas.  
Un abrazo.""",

    "+51950350144": """Feliz Año Nuevo, Pabloooooo ✨

Este año nos conocimos y la verdad ha sido muy chévere compartir contigo. Tu forma de ser, tan alegre y tan tú, hace que todo se sienta más ligero. Siempre tienes esa energía que contagia y que hace que los momentos sean más divertidos.

Gracias por las risas, las conversaciones y la buena vibra de este año. Se siente bien tener amistades así, simples y reales. Espero que este nuevo año venga con muchas cosas buenas para ti, con momentos felices y metas cumplidas.

Te deseo de corazón un feliz Año Nuevo. Que no falte la alegría, la salud y las ganas de seguir disfrutando cada etapa.  
Un abrazo grande.""",

    "+51933398159": """Feliz Año Nuevo, Carmen ✨

Quería decirte algo que a veces no se dice lo suficiente. Eres una persona muy valiosa y todo lo que has logrado es fruto de tu esfuerzo y de tu forma de ser. Aunque a veces dudes o no lo veas así, tienes una fortaleza muy bonita y una capacidad enorme para seguir adelante.

Este año fue lindo poder compartir contigo, conversar y coincidir en distintos momentos. Es de esas amistades que se sienten tranquilas y reales, y eso se agradece mucho.

Deseo de corazón que este nuevo año te traiga calma, confianza en ti y muchas cosas buenas. Que sigas creciendo, aprendiendo y valorándote como mereces.

Y ya sabes que aquí estaré. Para escucharte, apoyarte o acompañarte cuando lo necesites.

Te deseo un feliz Año Nuevo, Carmen 🤍  
Un abrazo grande.""",

    "+51926861287": """Feliz Año Nuevo, Edith ✨

Este año fue bonito coincidir y compartir algunos momentos contigo. Gracias por la buena vibra, las conversaciones y esa forma tan tranquila y auténtica de ser. Son esas amistades que se sienten naturales y se valoran mucho.

Espero que este nuevo año venga con cosas buenas para ti, con tranquilidad, alegrías y metas cumplidas. Que sigas avanzando y disfrutando cada etapa como mejor sabes hacerlo.

Te deseo de corazón un feliz Año Nuevo.  
Un abrazo.""",

    "+51928662257": """Feliz Año Nuevo, Bei Bei ✨

Quería decirte algo que siento de verdad. A veces uno no se da cuenta de todo lo que es capaz, y tú eres una prueba de eso. Todo lo que has logrado es fruto de tu esfuerzo y de la persona que eres, aunque en algunos momentos dudes de ti misma.

Este año fue bonito poder compartir contigo, conversar y coincidir en distintos momentos. Tienes una forma muy especial de ser y una energía tranquila que se siente bien tener cerca.

Deseo de corazón que este nuevo año confíes más en ti, que valores cada paso que das y que te sientas orgullosa de todo lo que estás construyendo. Mereces cosas buenas y un año lleno de calma y alegría.

Y ya sabes que aquí estaré. Para escucharte, apoyarte o acompañarte cuando lo necesites.

Te deseo un feliz Año Nuevo, Bei Bei 🤍  
Un abrazo grande."""
}

# ═══════════════════════════════════════════════════════════
# ⚙️ CONFIGURACIÓN
# ═══════════════════════════════════════════════════════════

HORA_OBJETIVO = 0  # Medianoche (00:00)
MINUTO_OBJETIVO = 0
DELAY_ENTRE_MENSAJES = 15  # segundos entre cada mensaje

# ═══════════════════════════════════════════════════════════
# 🕐 FUNCIÓN DE ESPERA
# ═══════════════════════════════════════════════════════════

def esperar_hasta_medianoche():
    """Espera hasta las 00:00 del día siguiente"""
    print("╔════════════════════════════════════════════════╗")
    print("║   ⏰ ESPERANDO HASTA MEDIANOCHE...            ║")
    print("╚════════════════════════════════════════════════╝")
    print()
    
    while True:
        ahora = datetime.now()
        hora_actual = ahora.hour
        minuto_actual = ahora.minute
        segundo_actual = ahora.second
        
        # Mostrar tiempo restante cada 60 segundos
        if segundo_actual == 0:
            tiempo_restante = ""
            if hora_actual < HORA_OBJETIVO:
                horas_faltantes = HORA_OBJETIVO - hora_actual
                minutos_faltantes = 60 - minuto_actual if minuto_actual > 0 else 0
                tiempo_restante = f"{horas_faltantes}h {minutos_faltantes}m"
            elif hora_actual == HORA_OBJETIVO and minuto_actual < MINUTO_OBJETIVO:
                minutos_faltantes = MINUTO_OBJETIVO - minuto_actual
                tiempo_restante = f"{minutos_faltantes}m"
            else:
                # Ya pasó medianoche de hoy, esperar hasta mañana
                horas_faltantes = (24 - hora_actual) + HORA_OBJETIVO
                minutos_faltantes = 60 - minuto_actual if minuto_actual > 0 else 0
                tiempo_restante = f"{horas_faltantes}h {minutos_faltantes}m"
            
            print(f"⏰ Hora actual: {ahora.strftime('%H:%M:%S')} | Faltan: {tiempo_restante}")
        
        # Verificar si ya es medianoche
        if hora_actual == HORA_OBJETIVO and minuto_actual == MINUTO_OBJETIVO:
            print()
            print("🎆 ¡ES MEDIANOCHE! Iniciando envío...")
            print()
            break
        
        time.sleep(1)

# ═══════════════════════════════════════════════════════════
# 📤 FUNCIÓN DE ENVÍO
# ═══════════════════════════════════════════════════════════

def enviar_mensaje_whatsapp(telefono, mensaje):
    """Envía un mensaje por WhatsApp Web"""
    try:
        # Limpiar el número (quitar espacios, guiones, etc.)
        telefono_limpio = telefono.replace("+", "").replace(" ", "").replace("-", "")
        
        # Codificar el mensaje para URL
        mensaje_codificado = urllib.parse.quote(mensaje)
        
        # Crear URL de WhatsApp
        url = f"https://web.whatsapp.com/send?phone={telefono_limpio}&text={mensaje_codificado}"
        
        # Abrir en navegador
        webbrowser.open(url)
        
        # Esperar a que cargue WhatsApp Web
        time.sleep(15)
        
        # Presionar Enter para enviar
        pyautogui.press('enter')
        
        # Esperar confirmación
        time.sleep(2)
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

# ═══════════════════════════════════════════════════════════
# 🚀 FUNCIÓN PRINCIPAL
# ═══════════════════════════════════════════════════════════

def main():
    print("╔════════════════════════════════════════════════╗")
    print("║   🎆 SISTEMA DE ENVÍO AUTOMÁTICO 2025 🎆      ║")
    print("╚════════════════════════════════════════════════╝")
    print()
    print(f"📱 Total de mensajes: {len(mensajes)}")
    print(f"⏰ Hora programada: 00:00 (Medianoche)")
    print(f"⏱️  Delay entre mensajes: {DELAY_ENTRE_MENSAJES}s")
    print()
    print("⚠️  IMPORTANTE:")
    print("   • Mantén esta ventana abierta")
    print("   • NO apagues la laptop")
    print("   • Asegúrate de estar logueado en WhatsApp Web")
    print("   • El script esperará automáticamente hasta medianoche")
    print()
    input("Presiona ENTER para iniciar la espera...")
    print()
    
    # Esperar hasta medianoche
    esperar_hasta_medianoche()
    
    # Enviar mensajes
    contador = 1
    total = len(mensajes)
    exitosos = 0
    fallidos = 0
    
    for telefono, mensaje in mensajes.items():
        try:
            # Extraer nombre del mensaje
            nombre = mensaje.split(",")[1].split("✨")[0].strip()
            
            print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print(f"📤 [{contador}/{total}] Enviando a: {nombre}")
            print(f"📞 Número: {telefono}")
            
            # Enviar mensaje
            if enviar_mensaje_whatsapp(telefono, mensaje):
                print(f"✅ Mensaje enviado exitosamente")
                exitosos += 1
            else:
                print(f"❌ Fallo al enviar")
                fallidos += 1
            
            # Esperar antes del siguiente
            if contador < total:
                print(f"⏳ Esperando {DELAY_ENTRE_MENSAJES}s antes del siguiente...")
                time.sleep(DELAY_ENTRE_MENSAJES)
            
            contador += 1
            
        except Exception as e:
            print(f"❌ ERROR al enviar a {telefono}: {str(e)}")
            fallidos += 1
            continue
    
    # Resumen final
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("✨ PROCESO COMPLETADO ✨")
    print(f"✅ Exitosos: {exitosos}")
    print(f"❌ Fallidos: {fallidos}")
    print(f"📊 Total: {total}")
    print()
    print("🎆 ¡FELIZ AÑO NUEVO 2025! 🎆")
    print()

# ═══════════════════════════════════════════════════════════
# ▶️ EJECUTAR
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()