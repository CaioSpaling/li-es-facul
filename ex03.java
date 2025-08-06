import java.util.Scanner;

public class ex03 {
    public static void main(String[] args){
        Scanner ler = new Scanner (System.in);
        System.out.print("\n");
        System.out.print("Digite um número inteiro: ");
        int num = ler.nextInt();
        if(num < 50){
            for(int i = num; i <= 50; i++){
                System.out.print(" "+i+" ");
            }
        }
        else if(num > 50){
            for(int i = num; i >= 50; i--){
                System.out.print(" " +i+ " ");
            }
        }
        else if(num == 50){
            System.out.print("O número selecionado é igual a 50!");
        }
        ler.close();
        }
    }

