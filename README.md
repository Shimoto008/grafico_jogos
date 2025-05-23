# Análise de Vendas de Jogos

Este projeto realiza uma análise de dados de vendas de jogos utilizando Python, pandas e matplotlib. O objetivo é visualizar o faturamento total por jogo e por plataforma, além de mostrar a participação de cada título nas vendas totais por meio de gráficos interativos.

## Arquivos

- `vendas_jogos.csv`: Arquivo contendo os dados de vendas de jogos.
- `analise.py`: Script principal que realiza a leitura, análise e visualização dos dados.
- Pasta `graficos/`: Contém as imagens geradas pelos gráficos.

## Funcionalidades

- Cálculo de faturamento total (quantidade × preço unitário)
- Agrupamento de dados por jogo e por plataforma
- Gráfico de barras para visualização do faturamento
- Gráfico de pizza para participação de cada jogo nas vendas

## Como executar

1. **Clone o repositório ou copie os arquivos para sua máquina.**

2. **Instale as bibliotecas necessárias:**

```bash
pip install pandas matplotlib
```

3. **Certifique-se de que o arquivo `vendas_jogos.csv` está no mesmo diretório do seu script Python.**

4. **Execute o script principal:**

```bash
python analise.py
```

## Visualizações

### 1. Faturamento por Jogo
![faturamento_jogos](https://github.com/user-attachments/assets/781474f5-cb41-48e2-ac50-697e13032795)


### 2. Faturamento por Plataforma
![faturamento_plataforma](https://github.com/user-attachments/assets/2fe14b7e-63a2-434b-a0da-0491e718bfbb)


### 3. Participação dos Jogos no Faturamento (Gráfico de Pizza)
![participação_jogos](https://github.com/user-attachments/assets/15070350-efa1-42f9-a0a8-b433559966cd)


## Pré-requisitos

- Python 3.8 ou superior
- Bibliotecas:
  - pandas
  - matplotlib

## Licença

Este projeto está licenciado sob a licença MIT.
