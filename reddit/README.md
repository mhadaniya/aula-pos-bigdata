# Reddit

O [Reddit](https://www.reddit.com) divulgou um enorme conjunto de dados contendo todos os ~ 1,7 bilhões de comentários disponíveis ao público. No [Kaggle](https://www.kaggle.com), é possível encontrar um dataset de tamanho menor, contendo aproximadamente 30GBs, referentes ao mês de Maio de 2015. Ainda assim, é uma quantidade muito grande para analisarmos. Existe um subconjunto deste dataset, contendo 100 subreddits com base na contagem de comentários, resultando em um arquivo de ~4,5 GB, que é utilizado em um curso do Udacity.

```bash
wget https://s3.amazonaws.com/content.udacity-data.com/courses/ud1000/data/comments.tar.gz
```

Os dados estão em um arquivo CSV, contendo as seguintes colunas:

- `subreddit`: o subreddit no qual o comentário foi publicado
- `author`: nome de usuário do autor do comentário
- `body`: texto do comentário
- `create_utc`: registro de data e hora UTC de quando o comentário foi publicado
- `ups`: Comentários positivos
- `downs`: Comentário em votação
- `gilded`: 1 se o usuário receber ouro no Reddit pelo comentário, 0 caso contrário
- `archived`: 1 se o comentário foi arquivado, 0 caso contrário

Abaixo a 1a linha do arquivo:

```tsv
AskReddit	jesse9o3	No one has a European accent either  because it doesn't exist. There are accents from Europe but not a European accent.	1430438400	3	0	0	0
```

## Steps iniciais

Faça o download do arquivo, e suba o arquivo para o HDFS.

## Exercício 01

Escreva um `mapper` e `reducer` que retorne o número `ups`, `downs` de cada subreddit.

## Exercício 02

Escreva um `mapper` e `reducer` que conte as palavras **"love"** e **"hate"** nos comentários e calcule o um "índice de amor" para cada subreddit. O índice de amor é a diferença na contagem de amor e ódio, dividida pela soma:

$\frac{(love - have)}{(love + hate)}$

Este é um tipo de medida normalizada. Varia de 1 a -1, levando em consideração o número total de comentários sobre amor e ódio. Isso faz com que os subreddits tão grandes, com vários comentários, estejam na mesma escala que os subreddits pequenos.

Qual subreddit tem o maior índice de amor? Qual tem o menor índice de amor?

## Exercício 03

Escreva um `mapper` e `reducer` que retorne - para cada usuário - o número de comentários, o número médio de votos por comentário.

Responda as seguintes questões:

- a. Quem é mais prolífico, ou seja, quem tem mais comentários.
- b. Quem é o mais curtido, a média mais alta de votos?
