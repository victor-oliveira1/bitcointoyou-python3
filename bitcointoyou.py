#!/bin/python3
'''Uma interface simples para a Trade API da corretora Bitcointoyou.

Para utilizar, basta instanciar a classe API com os parâmetros:
chave da api e senha da api.

Exemplo: btc = API(chave_api, senha_api)

Todas as funções retornam dicionários, resultado do processamento do
json enviado pelo servidor.

OBS: Não sou responsável por qualquer problema em sua conta.
Use por sua própria conta e risco.

'''
import urllib.request
import urllib.parse
import time
import base64
import hmac
import json

class API:
    def __init__(self, api_key, api_pass):
        self.api_key = api_key
        self.api_pass = api_pass

    def _signature(self):
        nonce = time.strftime('%s')
        signature = base64.b64encode(
            hmac.new(
                self.api_pass.encode(),
                '{}{}'.format(nonce, self.api_key).encode(),
                digestmod='sha256').digest()
            )
        return nonce, signature


    def _baseReq(self, method):
        base_url = 'https://www.bitcointoyou.com/API'
        nonce, signature = self._signature()
        headers = {'key' : self.api_key,
                   'nonce' : nonce,
                   'signature' : signature}
        req = urllib.request.Request('{}{}'.format(base_url, method),
                                     headers=headers)
        resp = urllib.request.urlopen(req)
        page = resp.read()
        try:
            page_json = json.loads(page)
            return page_json
        except:
            return None

    def Ticker(self):
        '''Retorna valores atuais do Bitcoin.

        Parâmetros: Nenhum

        Exemplo:
        btc.Ticker()'''
        method = '/ticker.aspx'
        return self._baseReq(method)
        
    def Balance(self):
        '''Retorna o saldo disponível para cada moeda (BTC e REAL).

        Parâmetros: Nenhum
        
        Exemplo:
        btc.Balance()'''
        method = '/balance.aspx'
        return self._baseReq(method)

    def Orders(self, status=None):
        '''Retorna as ordens executadas.

        Parâmetros:
        'OPEN' - Ordens abertas,
        'CANCELED' - Ordens canceladas,
        'EXECUTED' - Ordens executadas.
        Caso nenhum parâmetro seja informado, retorna todas as ordens

        Exemplo:
        btc.Orders('OPEN')'''
        method = '/getorders.aspx?{}'.format(
            urllib.parse.urlencode(
            {'status' : status})
            )
        return self._baseReq(method)

    def DeleteOrder(self, order_id):
        '''Remove uma ordem agendada.

        Parâmetros:
        order_id - Id da ordem à cancelar.
        É possível verificar as id's das ordens abertas com o método Orders

        Exemplo:
        btc.DeleteOrder(1055)'''
        method = '/deleteorders.aspx?{}'.format(
            urllib.parse.urlencode(
                {'id' : order_id})
            )
        return self._baseReq(method)

    def CreateOrder(self, action, amount, price):
        '''Cria uma ordem (instantânea ou agendada).

        Vale lembrar que no caso de compra, se o valor
        informado for maior que o praticado, a compra é
        efetuada instantâneamente, caso contrário, é
        agendada.
        
        No caso da venda, se o valor informado for menor
        que o praticado, a venda é efetuada instantâneamente,
        caso contrário, é agendado.

        Parâmetros:
        action - 'buy' (comprar) ou 'sell' (vender),
        amount - Quantidade de compra ou venda (BTC),
        price - Valor de compra ou venda (BTC).

        
        Exemplos:
        Compra: btc.CreateOrder('buy', '0.00522', '52000')
        Venda: Compra: btc.CreateOrder('sell', '0.0782', '55700')'''
        method = '/createorder.aspx?{}'.format(
            urllib.parse.urlencode(
                {'asset' : 'BTC',
                 'action' : action,
                 'amount' : amount,
                 'price' : price})
            )
        return self._baseReq(method)
