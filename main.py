import pandas as pd  # manipular dados
import matplotlib.pyplot as plt

# Local em que esta armazenado o arquivo
arquivo = 'test.py'

nome = []
numero = []

# Tratamento de abertura, leitura e fechamento de arquivo
with open(arquivo) as linhas:
    for linha in linhas:
        #Quebra a linha pelo delimitador
        conteudo = linha.split(";")
        # Atribuindo a primeira parte ANTES de ;
        nome.append(conteudo[0])
        # Atribuindo a segunda parte APOS ;
        numero.append(int(conteudo[1]))

plt.rcParams.update({'font.size': 14})

df = pd.DataFrame({'tipo defeito': nome,
                  'freq (%)': numero})
df['cum (%)'] = df['freq (%)'].cumsum()/df['freq (%)'].sum()*100


fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.set_title('Grafico de Pareto')
color1 = 'blue'
# ax1.set_xlabel('X')
ax1.set_ylabel('Frequência (%)', color=color1)

ax1.bar(df['tipo defeito'], df['freq (%)'], color=color1, edgecolor='orange', linewidth=2, \
        hatch='-')
# ax1.set_ylim([-10,10])
ax1.tick_params(axis='y', labelcolor=color1)

color2 = 'black'
ax2 = ax1.twinx()  # compartilhar o mesmo eixo x
ax2.set_ylabel('fr %', color=color2)

ax2.plot(df['tipo defeito'], df['cum (%)'], color=color2, marker='s', markersize=8, linestyle='-')

ax2.tick_params(axis='y', labelcolor=color2)
ax2.set_ylim([0, 120])

for tick in ax1.get_xticklabels():
    tick.set_rotation(45)

plt.savefig('GraficoPareto.png', format='png', dpi=600, bbox_inches='tight')
plt.show()