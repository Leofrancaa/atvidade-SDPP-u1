import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class PrimeUtils {
    
    // Verifica se um número é primo
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }

    // Lê números do arquivo de entrada
    public static List<Integer> readNumbers(String filename) throws IOException {
        List<Integer> numbers = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                numbers.add(Integer.parseInt(line.trim()));
            }
        }
        return numbers;
    }

    // Escreve os primos no arquivo de saída
    public static void writePrimes(String filename, List<Integer> primes) throws IOException {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(filename))) {
            for (int prime : primes) {
                bw.write(prime + "\n");
            }
        }
    }

    // Registra o tempo de execução em um arquivo
    public static void logTime(String mode, double time) throws IOException {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("tempos.txt", true))) {
            bw.write(mode + ":" + time + "\n");
        }
    }
}