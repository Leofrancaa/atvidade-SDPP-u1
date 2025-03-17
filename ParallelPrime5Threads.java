import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

public class ParallelPrime5Threads {
    public static void main(String[] args) throws IOException, InterruptedException, ExecutionException {
        long startTime = System.nanoTime();
        List<Integer> numbers = PrimeUtils.readNumbers("Entrada01.txt");
        ExecutorService executor = Executors.newFixedThreadPool(5);
        List<Future<Boolean>> futures = new ArrayList<>();

        for (int num : numbers) {
            futures.add(executor.submit(() -> PrimeUtils.isPrime(num)));
        }

        List<Integer> primes = new ArrayList<>();
        for (int i = 0; i < futures.size(); i++) {
            if (futures.get(i).get()) primes.add(numbers.get(i));
        }

        executor.shutdown();
        PrimeUtils.writePrimes("SaidaParalela5.txt", primes);
        double tempo = (System.nanoTime() - startTime) / 1e9;
        PrimeUtils.logTime("Paralela5", tempo);
        System.out.println("Tempo Paralelo (5 threads): " + tempo + " segundos");
    }
}