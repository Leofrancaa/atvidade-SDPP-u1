import matplotlib.pyplot as plt

def ler_tempos():
    tempos = {'Sequencial': 0, 'Paralela5': 0, 'Paralela10': 0}
    try:
        with open('tempos.txt', 'r') as f:
            linhas = f.readlines()
            for linha in linhas:
                modo, tempo = linha.strip().split(':')
                tempos[modo] = float(tempo)
    except FileNotFoundError:
        print("Erro: Arquivo 'tempos.txt' não encontrado.")
    return tempos

def gerar_grafico(tempos):
    modos = ['Sequencial', 'Paralela5', 'Paralela10']  # Definido aqui
    valores = [tempos[modo] for modo in modos]
    cores = ['blue', 'green', 'red']
    
    plt.figure(figsize=(10, 5))
    plt.bar(modos, valores, color=cores)
    plt.ylabel('Tempo (segundos)')
    plt.title('Desempenho: Verificação de Números Primos')
    plt.savefig('desempenho.png')
    plt.close()

def gerar_relatorio(tempos):
    modos = ['Sequencial', 'Paralela5', 'Paralela10']  # Adicionado aqui
    with open('relatorio.txt', 'w') as f:
        f.write("Relatório de Desempenho\n\n")
        f.write("Estratégias de Implementação:\n")
        f.write("- Sequencial: Processamento linha a linha com uma única thread.\n")
        f.write("- Paralela5: Divisão das tarefas em 5 threads concorrentes.\n")
        f.write("- Paralela10: Divisão das tarefas em 10 threads concorrentes.\n\n")
        f.write("Tempos de Execução:\n")
        for modo in modos:  # Usando a variável definida
            f.write(f"{modo}: {tempos[modo]:.3f} segundos\n")
        f.write("\nConclusão: O uso de threads reduz o tempo, mas há sobrecarga de gerenciamento.\n")

if __name__ == "__main__":
    tempos = ler_tempos()
    if tempos['Sequencial'] > 0:
        gerar_grafico(tempos)
        gerar_relatorio(tempos)
        print("Relatório e gráfico gerados com sucesso!")
    else:
        print("Dados incompletos. Execute todas as implementações Java primeiro.")