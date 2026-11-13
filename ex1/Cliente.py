
# Discentes: Débora Yasmim Sousa Rocha, Laura Xavier De Oliveira

import socket

try:
    ENDERECO_IP = input("Informe o endereço IP do servidor: ")
    PORTA = int(input("Informe a porta do servidor: "))
except (KeyboardInterrupt, ValueError):
    print("\nCliente finalizado ou porta inválida.")
    raise SystemExit


def start_client_tcp():

    # Cria o socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Realiza a conexão com o servidor
        client_socket.connect((ENDERECO_IP, PORTA))

        print("Conexão estabelecida com sucesso!")
        print("Digite 'sair' para encerrar a conexão.")

        while True:

            mensagem = input("Digite sua mensagem: ")

            # Verifica se o usuário deseja sair
            if mensagem.lower() == "sair":
                print("Encerrando conexão...")
                break

            # Valida mensagens vazias
            if mensagem.strip() == "":
                print("Mensagem vazia não permitida!")
                continue

            # Envia a mensagem para o servidor
            client_socket.sendall(mensagem.encode("utf-8"))

            # Recebe a confirmação do servidor
            resposta = client_socket.recv(1024)

            if not resposta:
                print("Servidor encerrou a conexão.")
                break

            print(resposta.decode("utf-8"))

    except ConnectionRefusedError:
        print("Não foi possível conectar: servidor indisponível.")

    except OSError as erro:
        print(f"Erro na comunicação: {erro}")

    finally:
        # Garante o encerramento do socket
        client_socket.close()
        print("Conexão encerrada.")


# Inicia o cliente TCP
start_client_tcp()
