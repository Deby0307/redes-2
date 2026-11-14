
# Trabalho 2 – Redes de Computadores 2

Repositório desenvolvido para a disciplina de **Redes de Computadores 2**, ministrada pelo professor Alessandro Vivas Andrade.

O trabalho tem como objetivo desenvolver habilidades práticas de programação em redes de computadores utilizando os protocolos TCP e UDP, explorando conceitos de comunicação cliente-servidor, manipulação de threads, programação com sockets e análise de tráfego de rede utilizando o Wireshark.

## 👥 Integrantes

- Débora Yasmim Sousa Rocha
- Laura Xavier de Oliveira

## 🛠️ Tecnologias utilizadas

- Python 3.10 ou superior
- Sockets TCP e UDP
- Biblioteca `socket`
- Biblioteca `threading`
- Wireshark
- Sistema operacional Linux

## 📁 Estrutura do repositório

```text
Trabalho2-RedesComputadores2/
│
├── exercicio1/
│   ├── servidor.py
│   ├── cliente.py
│   └── README.md
│
├── exercicio2/
│   ├── servidor.py
│   ├── cliente.py
│   └── README.md
│
├── exercicio3/
│   ├── servidor.py
│   ├── cliente.py
│   └── README.md
│
├── exercicio4/
│   ├── servidor.py
│   ├── cliente.py
│   └── README.md
│
├── exercicio5/
│   ├── captura_exercicio5.pcapng
│   ├── evidencia_exercicio5.png
│   └── README.md
│
├── exercicio6/
│   ├── captura_exercicio6.pcapng
│   ├── evidencia_exercicio6.png
│   └── README.md
│
└── README.md
```

*Observação: a estrutura apresenta uma organização sugerida. Os nomes dos arquivos podem ser ajustados conforme a implementação.*

## 📚 Exercícios desenvolvidos

### Exercício 1 – Cliente-Servidor TCP

Implementação de um sistema de comunicação cliente-servidor utilizando o protocolo TCP, permitindo que múltiplos clientes se conectem simultaneamente ao servidor por meio de threads.

**Principais funcionalidades:**

- Comunicação utilizando sockets TCP.
- Atendimento simultâneo de múltiplos clientes.
- Utilização de threads para gerenciar conexões.
- Envio e recebimento de mensagens.
- Validação de mensagens e tratamento de erros.
- Encerramento seguro das conexões.

### Exercício 2 – Servidor Echo UDP

Desenvolvimento de um servidor utilizando o protocolo UDP, responsável por receber mensagens dos clientes e retornar o mesmo conteúdo, implementando um serviço de eco.

**Principais funcionalidades:**

- Comunicação utilizando sockets UDP.
- Envio e recebimento de datagramas.
- Retorno das mensagens recebidas pelo servidor.
- Validação do tamanho das mensagens.
- Tratamento de erros e tempo limite de resposta.

### Exercício 3 – Chat em Rede TCP

Implementação de um sistema de chat em tempo real, permitindo a comunicação entre múltiplos usuários conectados a um servidor central.

**Principais funcionalidades:**

- Comunicação utilizando TCP.
- Conexão simultânea de múltiplos clientes.
- Identificação dos usuários por nickname.
- Transmissão de mensagens para os demais participantes (broadcast).
- Utilização de threads para envio e recebimento de mensagens.
- Notificação de entrada e saída de participantes.

### Exercício 4 – Servidor de Hora com Threads

Desenvolvimento de um servidor TCP multithread capaz de fornecer a hora atual para múltiplos clientes simultaneamente.

**Principais funcionalidades:**

- Comunicação utilizando sockets TCP.
- Atendimento simultâneo por meio de threads.
- Envio da hora atual no formato HH:MM:SS.
- Controle de concorrência utilizando `threading.Lock`.
- Contador de clientes atendidos.
- Registro de logs das solicitações recebidas.

### Exercício 5 – Análise de Tráfego HTTP

Captura e análise de pacotes HTTP utilizando o Wireshark, com o objetivo de identificar os métodos de requisição, URLs acessadas, códigos de status e cabeçalhos da comunicação.

**Procedimentos realizados:**

- Captura de pacotes de rede utilizando o Wireshark.
- Acesso a um site HTTP pelo navegador.
- Aplicação do filtro `http` para localizar os pacotes.
- Análise das requisições e respostas HTTP.

**Observações:**

Durante a captura, foi identificada uma requisição HTTP utilizando o método GET, direcionada ao recurso `/connecttest.txt`. Também foi identificada uma resposta do servidor com código de status `200 OK`, indicando que a solicitação foi atendida com sucesso. A resposta apresentou o tipo de conteúdo `text/plain`.

**Arquivos:**

- `exercicio5.pcapng`: arquivo com os pacotes capturados.
- `captura de tela.png`: captura de tela destacando os pacotes relevantes.

### Exercício 6 – Estabelecimento e Encerramento de Conexão TCP

Captura e análise do processo de estabelecimento e encerramento de uma conexão TCP, identificando os pacotes responsáveis pela comunicação entre cliente e servidor.

**Procedimentos realizados:**

- Captura de pacotes utilizando o Wireshark.
- Estabelecimento de conexão com um servidor Web utilizando Telnet na porta 80.
- Aplicação do filtro `tcp` para localizar os pacotes.
- Identificação dos pacotes do processo Three-Way Handshake.
- Análise dos pacotes de encerramento da conexão.

**Análise:**

O processo de estabelecimento de uma conexão TCP é composto por três etapas: SYN, SYN-ACK e ACK. Essas etapas permitem estabelecer a comunicação entre cliente e servidor. Também são analisados os pacotes responsáveis pelo encerramento da conexão, identificados pelas flags FIN/ACK ou RST.

**Arquivos:**

- `execicio6.pcapng`: arquivo com os pacotes capturados.
- `captura de tela.png`: captura de tela destacando os pacotes relevantes.

## ⚙️ Requisitos

Para executar os programas, é necessário possuir:

- Python 3.10 ou superior.
- Sistema operacional Linux.
- Git.
- Wireshark para os exercícios de análise de tráfego.

Para verificar a versão do Python:

```bash
python3 --version
```

## ▶️ Como executar os programas

Cada exercício de programação possui seus próprios arquivos de cliente e servidor.

Primeiramente, acesse o diretório do exercício desejado:

```bash
cd exercicio1
```

Em um terminal, execute o servidor:

```bash
python3 servidor.py
```

Em outro terminal, execute o cliente:

```bash
python3 cliente.py
```

Os comandos específicos e parâmetros de execução podem variar conforme cada exercício. Consulte o README.md presente em cada diretório para obter as instruções detalhadas.

## 📡 Análise de tráfego com Wireshark

Os exercícios 5 e 6 utilizam o Wireshark para capturar e analisar pacotes de rede.

As capturas são armazenadas nos diretórios correspondentes, acompanhadas de imagens que destacam os pacotes relevantes e de descrições dos resultados observados.

## 🎓 Disciplina

**Disciplina:** Redes de Computadores 2

**Professor:** Alessandro Vivas Andrade

**Instituição:** Universidade Federal dos Vales do Jequitinhonha e Mucuri (UFVJM)

**Ano:** 2026
