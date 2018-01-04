# bitcointoyou-python3
Uma interface simples para a Trade API da corretora Bitcointoyou.

**bitcointoyou-python3** é um script Python3 que permite ao usuário interagir com a API da corretora.
É necessário gerar um par de chaves para se comunicar com a API. Para tanto, faça o login, acesse o menu API e clique em GERAR CHAVES.

Para utilizar, basta instanciar a classe API com os parâmetros:
chave da api e senha da api.

### Exemplo:
`btc = API(chave_api, senha_api)`

Todas as funções retornam dicionários, resultado do processamento do
json enviado pelo servidor.

## Métodos definidos:

**Ticker():**
Retorna valores atuais do Bitcoin.<br />
Parâmetros: Nenhum

### Exemplo:
`btc.Ticker()`

**Balance():**
Retorna o saldo disponível para cada moeda (BTC e REAL).<br />
Parâmetros: Nenhum

### Exemplo:
`btc.Balance()`

**Orders(status):**
Retorna as ordens executadas.<br />
Parâmetros:<br />
'OPEN' - Ordens abertas,<br />
'CANCELED' - Ordens canceladas,<br />
'EXECUTED' - Ordens executadas.<br />
Caso nenhum parâmetro seja informado, retorna todas as ordens

### Exemplo:
`btc.Orders('OPEN')`

**DeleteOrder(order_id):**
Remove uma ordem agendada.<br />
Parâmetros:<br />
order_id - Id da ordem à cancelar.<br />
É possível verificar as id's das ordens abertas com o método **Orders**

### Exemplo:
`btc.DeleteOrder(1055)`

**CreateOrder(action, amount, price):**
Cria uma ordem (instantânea ou agendada).<br />
Vale lembrar que no caso de compra, se o valor<br />
informado for maior que o praticado, a compra é<br />
efetuada instantâneamente, caso contrário, é<br />
agendada.<br />
        
No caso da venda, se o valor informado for menor<br />
que o praticado, a venda é efetuada instantâneamente,<br />
caso contrário, é agendado.<br />

### Exemplos:
Compra: `btc.CreateOrder('buy', '0.00522', '52000')`
Venda: `btc.CreateOrder('sell', '0.0782', '55700')`

**OBS: Não sou responsável por qualquer problema em sua conta.
Use por sua própria conta e risco.**

Idéias ou sugestões podem ser enviadas para o email: victor.oliveira@gmx.com.
