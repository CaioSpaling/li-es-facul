/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ex1;

/**
 *
 * @author IFSP
 */
import java.util.*;

public class Ex1 {

    public static void main(String[] args) {
        int[] listanum = {1, 2, 3, 4, 5};
       
        System.out.println("A lista de números é essa: " + Arrays.toString(listanum));
        
        int soma = 0;
        for(int i = 0; i < listanum.length; i++){
            soma += listanum[i];
        }
        
        System.out.println("A soma dos valores da lista é " + soma);
    }
}
