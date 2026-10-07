# Desafio Técnico — Target

Soluções em Python para os três exercícios do desafio técnico da Target, envolvendo cálculo de comissões, movimentação de estoque e cálculo de juros por atraso.

## Tecnologias

- Python 3
- JSON para armazenamento dos dados
- Bibliotecas padrão do Python: `json`, `decimal`, `uuid` e `datetime`

Não é necessário instalar dependências externas.

## Estrutura do projeto

```text
desafio_target/
├── comissoes.py
├── vendas.json
├── movimentacoes.py
├── estoque.json
├── juros.py
└── README.md
```

## 1. Cálculo de comissões

Lê as vendas do arquivo `vendas.json`, calcula a comissão de cada venda e apresenta o total por vendedor.

| Valor da venda | Comissão |
| --- | --- |
| Abaixo de R$ 100,00 | Sem comissão |
| De R$ 100,00 até menos de R$ 500,00 | 1% |
| A partir de R$ 500,00 | 5% |

Os cálculos utilizam `Decimal`, com arredondamento do total de cada vendedor para duas casas decimais.

Execute:

```bash
python comissoes.py
```

## 2. Movimentação de estoque

Permite registrar entradas e saídas dos produtos cadastrados em `estoque.json`.

Cada movimentação registra:

- Identificador numérico gerado com UUID.
- Código do produto.
- Tipo da movimentação: entrada ou saída.
- Descrição informada pelo usuário.
- Quantidade movimentada.
- Estoque anterior e estoque final.

O programa valida o produto, exige uma quantidade inteira positiva e uma descrição, além de impedir saídas superiores ao estoque disponível.

Após cada movimentação, exibe o saldo final e salva o estoque atualizado e o histórico no arquivo `estoque.json`.

Execute:

```bash
python movimentacoes.py
```

## 3. Cálculo de juros

Recebe um valor e uma data de vencimento, calculando juros simples de 2,5% por dia de atraso até a data atual do computador.

```text
Juros = valor × 0,025 × dias de atraso
Total = valor + juros
```

A data deve ser informada no formato `dd/mm/aaaa`. Caso o vencimento seja hoje ou uma data futura, os juros serão zero.

Exemplo: um valor de R$ 100,00 com 4 dias de atraso gera R$ 10,00 de juros, totalizando R$ 110,00.

Execute:

```bash
python juros.py
```

## Como executar

1. Instale o Python 3.
2. Clone o repositório:

   ```bash
   git clone https://github.com/AlexandreMJunior/desafio_target.git
   ```

3. Acesse a pasta:

   ```bash
   cd desafio_target
   ```

4. Execute o exercício desejado utilizando os comandos apresentados acima.

Execute os programas a partir da pasta do projeto para que os arquivos JSON sejam encontrados.

Em ambientes nos quais o comando `python` não estiver disponível, utilize `python3`.
