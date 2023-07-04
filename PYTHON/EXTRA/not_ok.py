def conectar_servidor():
    print("Conexão com o servidor estabelecida.")


def criar_conexao(destinatario):
    print("Conexão com o destinatário {} estabelecida.".format(destinatario))


def autenticar():
    print("Autenticação realizada com sucesso.")


def enviar_texto(mensagem):
    print("Mensagem enviada: {}".format(mensagem))


def encerrar_conexao():
    print("Conexão encerrada.")


def exibir_mensagem_enviada():
    print("Mensagem enviada com sucesso.")


def exibir_erro(mensagem):
    print("Erro: {}".format(mensagem))


def enviar_mensagens():
    while True:
        destinatario = input("Digite o nome do destinatário (ou 'sair' para encerrar): ")
        if destinatario.lower() == "sair":
            break


        mensagem = input("Digite a mensagem: ")
        if not mensagem:
            exibir_erro("Digite uma mensagem.")
            continue


        conectar_servidor()
        criar_conexao(destinatario)
        autenticar()
        enviar_texto(mensagem)
        encerrar_conexao()
        exibir_mensagem_enviada()


enviar_mensagens()