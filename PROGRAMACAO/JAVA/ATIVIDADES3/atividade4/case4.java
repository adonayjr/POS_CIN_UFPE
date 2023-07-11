/*(4) Desenvolva um algoritmo que peça ao usuário que insira dois números inteiros positivos A e B, 
no qual A deve ser menor que B (supõe-se que o usuário irá respeitar esse enunciado). 
O algoritmo deve mostrar, na tela, todos os números ímpares compreendidos entre A e B (inclusive).

* Exemplo de execução – Exercício 4 - Caso de teste
Insira o valor de A:
1
Insira o valor de B:
10
É impar: 1
É impar: 3
É impar: 5
É impar: 7
É impar: 9
 */

package PROGRAMACAO.JAVA.ATIVIDADES3.atividade4;

import java.util.Scanner;

public class case4 {
    public static void main(String[] args) {
    	Scanner input = new Scanner(System.in);

        int numero1 = 0;
        int numero2 = 0;

		System.out.printf("Insira o valor de A::\n");
		numero1 = input.nextInt();
        System.out.printf("Insira o valor de B::\n");
		numero2 = input.nextInt();
	
		input.close(); //fechando o buffer
    			    
		for(int i = numero1; i < numero2; i++){
            if (i%2 !=0){
            System.out.printf("É impar = %d \n", i);
            }
		}
	}
}
