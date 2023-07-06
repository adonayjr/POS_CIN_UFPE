/** Exemplo de execução – Exercício 5 - Caso de teste
Insira o primeiro número:
2
Insira o segundo número:
3
Resultado: 8 */

package PROGRAMACAO.JAVA.ATIVIDADES.atividade5;

import static java.lang.Math.pow;

import java.util.Scanner;

public class numeros {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        double num1 = 0;
        double num2 = 0;
        double expo = 0;

		System.out.printf("Digite num1:\n");
		num1 = input.nextDouble();
		System.out.printf("Digite num2:\n");
		num2 = input.nextDouble();
      
        expo = pow(num1,num2);

        System.out.printf("O exponecial dos números é =  "+expo);
		
		input.close(); //fechando o buffer

    }
    
}
