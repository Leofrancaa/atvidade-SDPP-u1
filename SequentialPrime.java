import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class SequentialPrime {
    public static void main(String[] args) throws IOException {
        long startTime = System.nanoTime();
        List<Integer> numbers = PrimeUtils.readNumbers("Entrada01.txt");
        List<Integer> primes = new ArrayList<>();

        for (int num : numbers) {
            if (PrimeUtils.isPrime(num)) primes.add(num);
        }

        PrimeUtils.writePrimes("SaidaSequencial.txt", primes);
        double tempo = (System.nanoTime() - startTime) / 1e9;
        PrimeUtils.logTime("Sequencial", tempo);
        System.out.println("Tempo Sequencial: " + tempo + " segundos");
    }
}