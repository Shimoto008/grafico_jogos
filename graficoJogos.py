import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('jogos.csv')

#faturamento total de cada jogo
df['faturamento'] = df['quantidade'] * df['preco_unitario']

faturamento_jogo = df.groupby('jogo')['faturamento'].sum()

faturamento_jogo.plot(kind="bar", color="skyblue")
plt.title("faturamento dos jogos")
plt.ylabel("faturamento R$")
plt.xlabel("jogo")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#faturamento total por plataforma
faturamento_plataforma = df.groupby('plataforma')['faturamento'].sum()
faturamento_plataforma.plot(kind='bar', color='steelblue')
plt.title('Faturamento por plataforma')
plt.ylabel("Total de vendas")
plt.xlabel("Plataforma")
plt.xticks(rotation=40)
plt.tight_layout()
plt.show()

#participação de cada jogo no faturamento

faturamento_jogo = df.groupby('jogo')['faturamento'].sum()

valores = faturamento_jogo
labels = faturamento_jogo.index

plt.pie(valores,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90)
plt.title('Participação dos jogos no faturamento')
plt.axis('equal')
plt.tight_layout()
plt.savefig('graficos')
plt.show()


