/** Exemplo de execução – Exercício 3 - Caso de teste
Insira o salário:
1000
Novo salário:  1250 */

package PROGRAMACAO.JAVA.ATIVIDADES1.atividade3;

import java.util.Scanner;

public class salario {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        double salario = 0;
        double aumento = 0;
        double novo_salario = 0;

		System.out.printf("Digite salario:\n");
		salario = input.nextDouble();
		System.out.printf("Digite aumento:\n");
		aumento = input.nextDouble();
      
        novo_salario = salario + aumento;

        System.out.printf("novo_salario =  "+novo_salario);
		
		input.close(); //fechando o buffer

    }
    
}
