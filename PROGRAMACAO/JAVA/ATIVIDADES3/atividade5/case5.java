/*(5) Desenvolva um algoritmo que receba um número N e informe se N é um número primo, ou não. 
A saber: um número primo é um inteiro positivo que só pode ser dividido por ele mesmo e por um, apenas.

*Exemplo de execução – Exercício 5 - Caso de teste 1
Insira um número:
7
7 é primo.

*Exemplo de execução – Exercício 5 - Caso de teste 2
Insira um número:
10
10 não é primo. */

package PROGRAMACAO.JAVA.ATIVIDADES3.atividade5;

import java.util.Scanner;

public class case5 {
    public static void main(String[] args) {
    	Scanner input = new Scanner(System.in);
        System.out.print("Digite um número inteiro positivo: ");
        int num = input.nextInt();
        
        if (isPrimo(num)) {
            System.out.println(num + " é um número primo.");
        } else {
            System.out.println(num + " não é um número primo.");
        }
    }
    
    public static boolean isPrimo(int num) {
        if (num <= 1) {
            return false;
        }
        
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        
        return true;
    }
}






