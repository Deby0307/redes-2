
### Exercício 5 – Análise de Tráfego HTTP

**Objetivo:** Capturar e analisar pacotes HTTP utilizando o Wireshark, identificando os métodos de requisição, URLs acessadas, códigos de status e cabeçalhos da comunicação.

**Procedimentos realizados:**
- Captura de pacotes de rede utilizando o Wireshark.
- Acesso a um site HTTP pelo navegador.
- Aplicação do filtro `http` para localizar os pacotes.
- Análise das requisições e respostas HTTP.

**Observações:**

Durante a captura, foi identificada uma requisição HTTP utilizando o método GET, direcionada ao recurso `/connecttest.txt`. Também foi identificada uma resposta do servidor com código de status `200 OK`, indicando que a solicitação foi atendida com sucesso. A resposta apresentou o tipo de conteúdo `text/plain`.

**Arquivos:**
- `captura_exercicio5.pcapng`
- `evidencia_exercicio5.png`

### Exercício 6 – Estabelecimento e Encerramento de Conexão TCP

**Objetivo:** Capturar e analisar o processo de estabelecimento e encerramento de uma conexão TCP, identificando os pacotes responsáveis pela comunicação entre cliente e servidor.

**Procedimentos realizados:**
- Captura de pacotes utilizando o Wireshark.
- Estabelecimento de conexão com um servidor Web utilizando Telnet na porta 80.
- Aplicação do filtro `tcp` para localizar os pacotes.
- Identificação dos pacotes do processo Three-Way Handshake.
- Análise dos pacotes de encerramento da conexão.

**Observações:**

A análise da captura permite observar o processo de estabelecimento de uma conexão TCP, composto por três etapas: SYN, SYN-ACK e ACK. Esse processo permite estabelecer uma comunicação confiável entre cliente e servidor. Também são analisados os pacotes responsáveis pelo encerramento da conexão, identificados pelas flags FIN/ACK ou RST.

**Arquivos:**
- `captura_exercicio6.pcapng`
- `evidencia_exercicio6.png`
