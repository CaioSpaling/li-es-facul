import java.util.Scanner;

public class ex01{
public static void main (String[] args){
    Scanner ler = new Scanner (System.in);
    System.out.print("\nDigite um número: ");
    int num1 = ler.nextInt(); 
    System.out.print("Digite outro número: ");
    int num2 = ler.nextInt();
    int soma = num1 + num2;
    System.out.print("A soma entre " + num1 + " + " + num2 + " = " + soma);
    ler.close();
}
}
