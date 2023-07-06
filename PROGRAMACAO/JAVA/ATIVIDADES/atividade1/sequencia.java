/* Exemplo de execução – Exercício 1 - Caso de teste
Informe quatro números, em sequência:
1
2
3
4
Resultado da soma:  10*/

package PROGRAMACAO.JAVA.ATIVIDADES.atividade1;

import java.util.Scanner;

public class sequencia {
    public static void main(String[] args) {
    
    /*int soma = 0;
    int numero = 1;

    for (int i = 0; i < 3; i++ );{
    numero = numero + 1;
    soma = soma + numero;
    }

    System.out.println("Soma: "+ soma);*/

    	Scanner input = new Scanner(System.in);

        int numero1 = 0;
        int numero2 = 0;
        int numero3 = 0;
        int numero4 = 0;
        int soma = 0;

		System.out.printf("Digite numero1:\n");
		numero1 = input.nextInt();
		System.out.printf("Digite numero2:\n");
		numero2 = input.nextInt();
        System.out.printf("Digite numero3:\n");
		numero3 = input.nextInt();
        System.out.printf("Digite numero4:\n");
		numero4 = input.nextInt();
        
        soma = numero1 + numero2 + numero3 + numero4;

        System.out.printf("Soma dos números =  "+soma);
		
		input.close(); //fechando o buffer
	}
}