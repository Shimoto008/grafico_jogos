# Análise de Vendas de Jogos

Este é um simples projeto que realiza uma análise de dados de vendas de jogos utilizando Python, e suas bibliotecas pandas e matplotlib. O objetivo é visualizar o faturamento total por jogo e por plataforma, além de mostrar a participação de cada título nas vendas totais por meio de gráficos interativos.

## Arquivos

- `jogos.csv`: Arquivo contendo os dados de vendas de jogos.
- `graficoJogos.py`: Script principal que realiza a leitura, análise e visualização dos dados.

## Funcionalidades

- Cálculo de faturamento total (quantidade × preço unitário)
- Agrupamento de dados por jogo e por plataforma
- Gráfico de barras para visualização do faturamento
- Gráfico de pizza para participação de cada jogo nas vendas

## Visualização

### 1. Faturamento por Jogo
![faturamento_por_Jogo]
(faturamento_jogos.png)

### 2. Faturamento por Plataforma
![faturamento_por_plataforma]
(faturamento_jogos.png)

### 3. Participação dos Jogos no Faturamento
![Grafico_de_pizza]
(participação_jogos.png)

## Como executar

1. **Clone o repositório ou copie os arquivos para seu computador.**

2. **Instale as bibliotecas necessárias:**

```bash
pip install pandas matplotlib
```

3. **Certifique-se de que o arquivo `jogos.csv` está no mesmo diretório do seu script Python.**

4. **Execute o script principal:**

```bash
python graficoJogos.py
```

## Exemplo de visualizações

- Faturamento por jogo (gráfico de barras)
- Faturamento por plataforma (gráfico de barras)
- Participação dos jogos no faturamento (gráfico de pizza)

## Pré-requisitos

- Python 3.8 ou superior
- Bibliotecas:
  - pandas
  - matplotlib

## Licença

Este projeto está licenciado sob a licença MIT.
