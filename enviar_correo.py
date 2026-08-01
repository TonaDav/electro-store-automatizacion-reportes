import smtplib , getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_reporte():
    smtp_objeto = smtplib.SMTP("smtp.gmail.com", 587)

    smtp_objeto.ehlo()

    smtp_objeto.starttls()

    email = input("Ingrese su correo (gmail): ")
    contrasena = getpass.getpass("Contrasena:")
    smtp_objeto.login(email, contrasena)

    emisor = email
    receptor = input("Ingrese el correo del destinatario (gmail): ")

    asunto = input("Ingrese el asunto: ")
    cuerpo = input("Ingrese el mensaje: ")

    # Creamos el mensaje como multipart (text + archivo adjunto)
    mensaje = MIMEMultipart()
    mensaje["From"] = emisor
    mensaje["To"] = receptor
    mensaje["Subject"] = asunto
    # Agregamos el cuerpo como texto plano.
    mensaje.attach(MIMEText(cuerpo, "plain"))

    nombre_archivo = "reporte_electrostore.xlsx"

    with open(nombre_archivo, "rb") as mi_archivo:
        adjunto = MIMEBase("application", "octet-stream")
        adjunto.set_payload(mi_archivo.read())

    encoders.encode_base64(adjunto)
    adjunto.add_header("Content-Disposition", "attachment", filename=nombre_archivo)
    mensaje.attach(adjunto)

    smtp_objeto.sendmail(emisor, receptor, mensaje.as_string())
    smtp_objeto.quit()

if __name__ == "__main__":
    enviar_reporte()