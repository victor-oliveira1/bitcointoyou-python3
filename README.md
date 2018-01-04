# bitcointoyou-python3
Uma interface simples para a Trade API da corretora Bitcointoyou.<br />

**bitcointoyou-python3** é um script Python3 que permite ao usuário interagir com a API da corretora.<br />
É necessário gerar um par de chaves para se comunicar com a API. Para tanto, faça o login, acesse o menu API e clique em <br />GERAR CHAVES.

Para utilizar, basta instanciar a classe API com os parâmetros:<br />
**chave da api e senha da api.**<br />

### Exemplo:<br />
`btc = API(chave_api, senha_api)`<br />

Todas as funções retornam dicionários, resultado do processamento do<br />
json enviado pelo servidor.<br />

## Métodos definidos:<br />

**Ticker():**
Retorna valores atuais do Bitcoin.<br />
Parâmetros: Nenhum<br />

### Exemplo:<br />
`btc.Ticker()`<br />

**Balance():**<br />
Retorna o saldo disponível para cada moeda (BTC e REAL).<br />
Parâmetros: Nenhum<br />

### Exemplo:<br />
`btc.Balance()`<br />

**Orders(status):**<br />
Retorna as ordens executadas.<br />
Parâmetros:<br />
'OPEN' - Ordens abertas,<br />
'CANCELED' - Ordens canceladas,<br />
'EXECUTED' - Ordens executadas.<br />
Caso nenhum parâmetro seja informado, retorna todas as ordens

### Exemplo:<br />
`btc.Orders('OPEN')`<br />

**DeleteOrder(order_id):**<br />
Remove uma ordem agendada.<br />
Parâmetros:<br />
order_id - Id da ordem à cancelar.<br />
É possível verificar as id's das ordens abertas com o método **Orders**

### Exemplo:<br />
`btc.DeleteOrder(1055)`

**CreateOrder(action, amount, price):**<br />
Cria uma ordem (instantânea ou agendada).<br />
Vale lembrar que no caso de compra, se o valor<br />
informado for maior que o praticado, a compra é<br />
efetuada instantâneamente, caso contrário, é<br />
agendada.<br />
        
No caso da venda, se o valor informado for menor<br />
que o praticado, a venda é efetuada instantâneamente,<br />
caso contrário, é agendado.<br />

### Exemplos:<br />
Compra: `btc.CreateOrder('buy', '0.00522', '52000')`<br />
Venda: `btc.CreateOrder('sell', '0.0782', '55700')`<br />

**OBS: Não sou responsável por qualquer problema em sua conta.<br />
Use por sua própria conta e risco.**<br />

Idéias ou sugestões podem ser enviadas para o email: victor.oliveira@gmx.com<br />
