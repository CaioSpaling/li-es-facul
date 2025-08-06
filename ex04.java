import java.util.*;
import java.util.stream.Collectors;

public class ex04 {
    public static void main(String[] args){
        Scanner ler = new Scanner (System.in);
        Map<String, Integer> dados = new HashMap<>();

        for(int i = 0; i <= 3; i++){
            System.out.print("Digite seu nome: ");
            String nome = ler.nextLine();
            System.out.print("Digite sua idade: ");
            int idade = ler.nextInt();
            dados.put(nome, idade);
        }

        Map<String, Integer> crescente = dados.entrySet()
        .stream()
        .sorted(Map.Entry.comparingByValue())
        .collect(Collectors.toMap(
            Map.Entry::getKey,
            Map.Entry::getValue,
            (e1, e2) -> e1,
            LinkedHashMap::new
        ));

        crescente.forEach((nome, idade) ->
            System.out.println(nome + ": " + idade));


        ler.close();
    }
}
