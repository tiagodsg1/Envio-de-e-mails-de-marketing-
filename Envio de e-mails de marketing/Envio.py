import email.message
import smtplib
import time
from datetime import datetime
import codecs
import getpass
import random


class mailTo:

    def __init__(self):
        
        print("-----  Bem Vindo! -----")
        print("Iniciando envio automatico....")
        print()
        self.email_origem =  input("Login:")
        self.email_senha = input("Senha:")
        

    def carregarModeloHTML(self):
        print("Carregando email....")
        file = codecs.open("folder.html", "r", "utf-8")
        self.file = file

    def substituirTagsHTML(self):
        #Esta implementação deste bloco fica a critério do desenvolvedor de acordo com as suas necessidades.
        print("Carregando e-mail por lista")


    def enviarEmail(self):
        logs = open('logs.txt','a')
        logs.write("Iniciando Envio de email ["+time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())+"]...\n")

        file = self.file
        mail_content = file.read()
        email_origem = self.email_origem
        email_senha = self.email_senha
        print("\n")
        print("--- Iniciando o envio dos emails ----")
        print("\n")
        msg_subject = input("Titulo do Email:")
        print("\n")
      

        arquivo =  open('lista_de_emails.txt') # Definição do arquivo que contem as listas de emails, Somente leitura
        print (arquivo.readline())
        for email_por_linha in arquivo:
            
            
            
            try:
                

                msg = email.message.Message()
                msg["From"] = email_origem
                msg["To"] = email_por_linha.strip() # pega o email e remove espaços se tiver
                msg["Subject"] = msg_subject
                msg.add_header('Content-Type', 'text/html') # definido o tipo de arquivo a ser enviado 
                msg.set_payload(mail_content) # Conteudo do email que foi definido acima como html
                msg.set_charset('utf-8')

                server = smtplib.SMTP("smtp.gmail.com",587) # Definido o servidor SMTP hotmail
                server.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
                server.starttls() #Puts connection to SMTP server in TLS mode
                server.ehlo()
                server.login(email_origem, email_senha)

                server.sendmail(email_origem,[msg['To']] , msg.as_string())

                server.quit()
                print("Enviado email para "+email_por_linha)
                time.sleep(2.4)
                logs.write("Email Enviado para : "+str(email_por_linha)+"\n")

            except:
                print ('Something went wrong...')
                logs.write("ERRO ao enviar email para: "+str(email_por_linha))
                logs.write(str(smtplib.SMTPException)+"\n")
            
            time.sleep(random.randint(2,50))
                
        
        print("Emails Enviados")
        input("Press Enter para finalizar...")


mail = mailTo()
mail.carregarModeloHTML()
mail.enviarEmail()
