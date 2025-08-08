/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex2;

import java.util.Scanner;

/**
 *
 * @author IFSP
 */
public class Ex2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);
        int[] notas = new int[5];
        
        System.out.println("CALCULADOR DE MÉDIAS");
        System.out.println("Digite 5 notas:");
        
        for(int i = 0; i < 5; i++){
            System.out.print("Digite a nota "  + (i + 1) + ":");
            notas[i] = ler.nextInt();       
        }
        
        int soma = 0;
        for(int i = 0; i < notas.length; i++){
            soma += notas[i];
        }
        
        double media = soma/notas.length;
        
        System.out.println("A média das notas digitadas é: " + media);
    }
}