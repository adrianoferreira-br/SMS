# ----------------------------------------------------
#   ENVIO DE SMS EM MASSA
#   http://converttosqlite.com/convert/
# ----------------------------------------------------
import sqlite3
import os
import time

#--------------------------------------
# Conecta no banco
#--------------------------------------
def conecta_db(nome_file_db):
    sqlite3.version
    sqlite3.sqlite_version
    conn = sqlite3.connect(nome_file_db)
    pointer = conn.cursor()
    return pointer

#--------------------------------------
# Pega o número do celular na tabela
#--------------------------------------
def get_celular_from_tab(pointer, linha):
    sql = "select nr_celular from  tb_cadastro where PK=" + linha
    pointer.execute(sql)
    telefone = str(pointer.fetchone())
    if telefone != "None":
        celular = telefone[2:(telefone.index(",") - 1)]  # -------- (u'48999582333',)
    else:
        print("Erro na linha:", linha)
    print(linha, celular)
    return(celular)

# --------------------------------------
# Envia CURL para UnniTI com nr do celular
# --------------------------------------
def envia_sms(ipCentral, login, senha, celular, msg):
    #url = "curl --http1.0 -k --cookie \"i18bext=pt-BR&senha=" + senha + "&username=" + login + "\" --data \"evento=salvar&numeroDestino=" + celular + "&mensagem=" + msg + "\" https://" + ipCentral + "/sistemaEnviarSMS.htm"
    #os.system(url)
    ##os.environ()
    time.sleep(0.2)

# --------------------------------------
# Trata graficos
# --------------------------------------
def graphic():
    return

# --------------------------------------
# Defines
# --------------------------------------
ipCentral = "192.100.206.183"
msg = " by Intelbras 001"
celular = "999582333"  # "11976566415"
login = "admin"
senha = "admin"
qtd_sms = 97+10
x = 0


#--------------------------------------
# Programa Principal
#--------------------------------------
print("----------------------------------")
print("IP:",ipCentral, " Login/Senha:",login,"/",senha)
print("Mensagem:",msg)

pointer = conecta_db("/home/adriano/PycharmProjects/SMS/CadastroEventoUnniti.sqlite")
for i in range(1,528): # Primeiro nr celular, total de cadastro 528
    nr = str(i+1)
    celular2 = get_celular_from_tab(pointer, nr)
    if len(celular2) < 11:
        print("Telefone fixo")
    else:
        envia_sms(ipCentral, login, senha, celular2, msg)

