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

    static int maior(int num1, int num2){
        if(num1>num2){
        return num1;
        }else if(num1<num2){
        return num2;
        }else{
        return 0;
        }
    }
	 public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

		int x, y, m;
		System.out.printf("Digite num 1: \n");
		x = scan.nextInt();
		System.out.printf("Digite num 2: \n");
		y = scan.nextInt();

		m = maior(x,y);

		System.out.printf("Maior:%\n", m);

		scan.close(); //fechando o buffer
	}
 }