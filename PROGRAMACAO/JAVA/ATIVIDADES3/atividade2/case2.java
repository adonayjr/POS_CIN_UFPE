/*(2) Desenvolva um algoritmo que receba dois números inteiros positivos A e B. 
Exiba na tela todos os números inteiros compreendidos entre A e B, excluindo os próprios A e B. 
Suponha que o usuário respeite o enunciado e insira valores válidos para A e B.

* Exemplo de execução – Exercício 2 - Caso de teste
Insira o valor de A:
1
Insira o valor de B:
10
Série numérica:
2 3 4 5 6 7 8 9 */

package PROGRAMACAO.JAVA.ATIVIDADES3.atividade2;

import java.util.Scanner;

public class case2 {
    public static void main(String[] args) {
    	Scanner input = new Scanner(System.in);

        int numero1 = 0;
        int numero2 = 0;

		System.out.printf("Insira o valor de A::\n");
		numero1 = input.nextInt();
        System.out.printf("Insira o valor de B::\n");
		numero2 = input.nextInt();
	
		input.close(); //fechando o buffer
    			    
		for(int i = numero1 + 1; i < numero2; i++){
            System.out.printf("%d ", i);
		}
	}
}
