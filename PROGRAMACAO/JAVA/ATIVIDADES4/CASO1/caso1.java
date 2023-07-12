/*(1) Faça o design de uma função "maior" que receba dois números [inteiros e positivos] e retorne o maior deles.
 Caso eles sejam iguais, deve-se mostrar a mensagem "Os números são iguais".

* Exemplo de execução – Exercício 1 - Caso de teste 1
Insira o primeiro número:
1
Insira o segundo número:
2
O maior é: 2

* Exemplo de execução – Exercício 1 - Caso de teste 2
Insira o primeiro número:
1
Insira o segundo número:
1
Os números são iguais */
package PROGRAMACAO.JAVA.ATIVIDADES4.CASO1;

import java.util.Scanner;

public class caso1 {
	 public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

		int x, y;
        
        
		System.out.printf("Digite num 1: \n");
		x = scan.nextInt();
		System.out.printf("Digite num 2: \n");
		y = scan.nextInt();

        int m = maior(x,y);

        scan.close();
        
        if (m != -1) {
            System.out.println("O maior número é: " + m); 
        } else {
            System.out.println("Os números são iguais");
        }
    }

    public static int maior(int x, int y) {
        if (x > y) {
            return x;
        } else if (y > x) {
            return y;
        } else {
            return -1;
        }
    }
}