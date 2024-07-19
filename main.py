import pandas as pd
import matplotlib.pyplot as plt
import os

# Caminhos para os diretórios
ingressantes_dir = 'ingressantes/'
egressos_dir = 'egressos/'

# Inicializa dicionários para armazenar os dados
ingressantes_data = {'Ano': [], 'Homens': [], 'Mulheres': []}
egressos_data = {'Ano': [], 'Homens': [], 'Mulheres': []}

# Função para processar arquivos CSV
def processar_csv(diretorio, dados, tipo, curso_filtro):
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.csv'):
            ano = arquivo.split('-')[1].split('.')[0]
            df = pd.read_csv(os.path.join(diretorio, arquivo), delimiter=';')
            
            # Filtrar para o curso específico
            df = df[df['nome_curso'] == curso_filtro]
            
            homens = df[df['sexo'] == 'M'].shape[0]
            mulheres = df[df['sexo'] == 'F'].shape[0]
            dados['Ano'].append(ano)
            dados['Homens'].append(homens)
            dados['Mulheres'].append(mulheres)
            print(f'{tipo} - {ano}: Homens={homens}, Mulheres={mulheres}')

# Nome do curso a ser filtrado
curso_filtro = 'ENGENHARIA DE COMPUTAÇÃO'
#curso_filtro = 'ENGENHARIA DE ELÉTRICA'
#curso_filtro = 'TECNOLOGIA DA INFORMAÇÃO'

# Processar ingressantes
processar_csv(ingressantes_dir, ingressantes_data, 'Ingressantes', curso_filtro)

# Processar egressos
processar_csv(egressos_dir, egressos_data, 'Egressos', curso_filtro)

# Criar DataFrames para plotagem
ingressantes_df = pd.DataFrame(ingressantes_data)
egressos_df = pd.DataFrame(egressos_data)

# Função para plotar gráfico de barras
def plotar_grafico(df, titulo):
    df.set_index('Ano', inplace=True)
    df_percentage = df.div(df.sum(axis=1), axis=0) * 100  # Converte para porcentagem
    df_percentage.plot(kind='bar', stacked=True, color=['blue', 'pink'])
    plt.title(titulo)
    plt.xlabel('Ano')
    plt.ylabel('Porcentagem (%)')
    plt.legend(title='Sexo', labels=['Homens', 'Mulheres'])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Plotar gráficos
plotar_grafico(ingressantes_df, f'Porcentagem de Ingressantes em {curso_filtro} por Ano')
plotar_grafico(egressos_df, f'Porcentagem de Egressos de {curso_filtro} por Ano')
