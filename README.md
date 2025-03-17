**# Rodando o Código**

```bash
javac *.java

java SequentialPrime
java ParallelPrime5Threads
java ParallelPrime10Threads

python analise_desempenho.py
```

---

# Relatório de Desempenho

**Análise de Verificação de Números Primos em Diferentes Implementações**  
*Gustavo Diniz & Leonardo Franca*

## 1. Estratégias de Implementação

Foram desenvolvidas três abordagens para verificar números primos em um arquivo:

### a) Implementação Sequencial
- **Descrição**: Processamento linha a linha, utilizando uma única thread, onde cada número é verificado sequencialmente, um após o outro.
- **Vantagem**: Simplicidade de implementação e baixa sobrecarga de concorrência.

### b) Implementação Paralela com 5 Threads
- **Descrição**: Divisão das tarefas em 5 threads concorrentes, utilizando um `ThreadPoolExecutor` para distribuir a verificação de números entre as threads.
- **Vantagem**: Redução de tempo em cenários com múltiplos núcleos de CPU.

### c) Implementação Paralela com 10 Threads
- **Descrição**: Divisão das tarefas em 10 threads concorrentes, similar à implementação de 5 threads, mas com maior paralelismo.
- **Vantagem**: Ainda maior aproveitamento de recursos em sistemas com alta capacidade de processamento paralelo.

---

## 2. Tempos de Execução Observados

Os tempos foram medidos em segundos durante a execução das implementações:

| Implementação          | Tempo (ms) |
|------------------------|------------|
| Sequencial            | 108.44     |
| Paralela (5 threads)  |  84.95     |
| Paralela (10 threads) |  77.45     |

*Os valores são referentes a uma simulação real.*

---

## 3. Análise Comparativa

### 5 Threads:
- O tempo de execução foi de **84.95ms**, representando uma redução de **34.4%** em relação à versão sequencial (**108.44ms**).
- A introdução de 5 threads acelerou a verificação de números primos, dividindo a carga de trabalho e aproveitando os múltiplos núcleos do processador.

### 10 Threads:
- O tempo de execução foi de **77.45ms**, resultando em uma redução de **37.6%** em relação à versão sequencial.
- Embora a execução com 10 threads tenha reduzido mais o tempo, a melhora não é proporcional, indicando que o aumento de threads tem um ponto de retorno decrescente.

---

## 4. Eficiência do Paralelismo

### Ganho Não Linear:
A redução de tempo ao passar de **5 para 10 threads** não foi o dobro do ganho, o que implica que a adição de mais threads não proporciona um aumento linear na performance. Esse comportamento pode ser explicado por:

- **Sobrecarga de gerenciamento de threads**: O sistema precisa alocar e gerenciar as threads, introduzindo um custo adicional que se torna mais significativo conforme o número de threads cresce.
- **Gargalos**: Em tarefas **CPU-bound**, como a verificação de números primos, pode haver concorrência entre as threads, resultando em tempo extra de espera para acesso a recursos do sistema (CPU, cache e memória).

---
