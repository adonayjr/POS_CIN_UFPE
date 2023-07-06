/** Exemplo de execução – Exercício 4 - Caso de teste
Insira a base:
4
Insira a altura:
10
Area do triangulo:  20 */

package PROGRAMACAO.JAVA.ATIVIDADES.atividade4;

import java.util.Scanner;

public class triangulo {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int base = 0;
        int altura = 0;
        int area = 0;

		System.out.printf("Digite base:\n");
		base = input.nextInt();
		System.out.printf("Digite altura:\n");
		altura = input.nextInt();
      
        area = (base*altura)/2;

        System.out.printf("area do triangulo =  "+area);
		
		input.close(); //fechando o buffer

    }
    
}
