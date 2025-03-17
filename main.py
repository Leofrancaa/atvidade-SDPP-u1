import time
import concurrent.futures
import matplotlib.pyplot as plt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def read_input(filename):
    with open(filename, 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]
    return numbers

def write_output(filename, primes):
    with open(filename, 'w') as f:
        for p in primes:
            f.write(f"{p}\n")

def process_sequential(numbers):
    primes = []
    for n in numbers:
        if is_prime(n):
            primes.append(n)
    return primes

def process_parallel(numbers, num_threads):
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = {executor.submit(is_prime, n): i for i, n in enumerate(numbers)}
        for future in concurrent.futures.as_completed(futures):
            index = futures[future]
            results[index] = future.result()
    sorted_results = [results[i] for i in range(len(numbers))]
    primes = [numbers[i] for i, is_p in enumerate(sorted_results) if is_p]
    return primes

if __name__ == "__main__":
    input_filename = "Entrada01.txt"
    numbers = read_input(input_filename)

    # Processamento Sequencial
    start = time.time()
    primes_seq = process_sequential(numbers)
    time_seq = time.time() - start
    write_output("Saida01Sequencial.txt", primes_seq)

    # Processamento Paralelo com 5 threads
    start = time.time()
    primes_par5 = process_parallel(numbers, 5)
    time_par5 = time.time() - start
    write_output("Saida01Paralela5.txt", primes_par5)

    # Processamento Paralelo com 10 threads
    start = time.time()
    primes_par10 = process_parallel(numbers, 10)
    time_par10 = time.time() - start
    write_output("Saida01Paralela10.txt", primes_par10)

    # Gerar Relatório
    with open("relatorio.txt", "w") as f:
        f.write("Relatório de Desempenho\n\n")
        f.write("Estratégia de Implementação:\n")
        f.write("- Sequencial: Verifica cada número em ordem, um após o outro.\n")
        f.write("- Paralela (5/10 threads): Utiliza ThreadPoolExecutor para distribuir tarefas entre threads, mantendo a ordem original via índices.\n\n")
        f.write("Tempos de Execução:\n")
        f.write(f"Sequencial: {time_seq:.4f} segundos\n")
        f.write(f"Paralela (5 threads): {time_par5:.4f} segundos\n")
        f.write(f"Paralela (10 threads): {time_par10:.4f} segundos\n\n")
        f.write("Conclusão: Devido ao Global Interpreter Lock (GIL) do Python, o ganho de desempenho com threads é limitado para tarefas CPU-bound. O uso de multiprocessos seria mais eficaz.\n")

    # Gerar Gráfico
    labels = ['Sequencial', '5 Threads', '10 Threads']
    times = [time_seq, time_par5, time_par10]
    plt.bar(labels, times, color=['blue', 'green', 'red'])
    plt.ylabel('Tempo (segundos)')
    plt.title('Comparação de Desempenho')
    plt.savefig('desempenho.png')
    plt.close()