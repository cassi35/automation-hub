from monitor_juridico.test.endpoint import processo
from email.message import EmailMessage
import os 
import smtplib
def send_email()->None:
    msg = EmailMessage()

    msg["From"] ="cgrsobral@gmail.com"
    msg["To"] = "sobralcassique@gmail.com"
    msg["Subject"] = (
        f"Nova comunicação - "
        f"{processo['numero_processo']}"
    )

    advogados = "\n".join(
        f"- {adv['nome']} ({adv['oab']})"
        for adv in processo["advogados"]
    )

    corpo = f"""
Nova comunicação processual encontrada.

Processo: {processo["numero_processo"]}
Tipo: {processo["tipo_comunicacao"]}
Tribunal: {processo["tribunal"]}
Órgão: {processo["orgao"]}
Classe: {processo["classe"]}
Data: {processo["data_disponibilizacao"]}

Advogados:
{advogados}

Teor da comunicação:
{processo["texto"]}

Documento original:
{processo["link_documento"] or "Não disponível"}
"""

    msg.set_content(corpo)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(
           "cgrsobral@gmail.com",
           "jdlw zpqh gtok btkp",
        )
        smtp.send_message(msg)
