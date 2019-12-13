# Transactions

Um dos _datasets_ utilizado no curso da "Intro to Hadoop and MapReduce" da Udacity. Ele contém uma listagem de lojas, itens comprados, o valor e método de pagamento. Um dataset inicial para exercitar MapReduce.

As colunas são:

- `date`: Data da compra
- `time`: Hora da compra
- `store`: Local da compra
- `item`: Item comprado
- `value`: Valor gasto na compra
- `payment`: Método de pagamento

Abaixo as 4 primeiras linhas do arquivo:

```tsv
2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex
2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
2012-01-01	09:00	San Diego	Music	66.08	Cash
2012-01-01	09:00	Pittsburgh	Pet Supplies	493.51	Discover
```

## Steps iniciais

Faça o download do arquivo, e suba o arquivo para o HDFS.

## Exercício 01

Escreva um `mapper` e `reducer` que retorne a quantidade de vendas por `store`, e responda:

- a. Quantas vendas cada `store` possui?
- b. Qual `store` possui o maior número de vendas?
- c. Qual `store` possui o menor número de vendas?

## Exercício 02

Escreva um `mapper` e `reducer` que retorne o valor gasto por `store`, e responda:

- a. Em qual `store` foi gasto o maior valor?
- b. Em qual `store` foi gasto o menor valor?

## Exercício 03

Escreva um `mapper` e `reducer` que retorne o valor gasto por `item`, e responda:

- a. Qual `item` tem o maior valor?
- b. Qual `item` tem o menor valor?

## Exercício 04

Escreva um `mapper` e `reducer` que retorne o valor gasto pelo método de pagamento, e responda:

- a. Qual forma de pagamento tem o maior valor?
- b. Qual forma de pagamento tem o menor valor?

## Exercício 05

Escreva um `mapper` e `reducer` que retorne quantas vezes o método de pagamento foi utilizado, e responda, qual foi o método de pagamento mais utilizado?
