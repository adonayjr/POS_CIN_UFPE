/*(3) Faça o design de uma função "parImpar" que receba um número inteiro e verifique se esse número é par ou ímpar.

*Exemplo de execução – Exercício 3 - Caso de teste 1
Insira um número:
2
2 é par.

*Exemplo de execução – Exercício 3 - Caso de teste 2
Insira um número:
3
3 é impar. */
package PROGRAMACAO.JAVA.ATIVIDADES4.CASO3;

import java.util.Scanner;

public class caso3 {
	 public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

		int x;
        
		System.out.printf("Digite num 1: \n");
		x = scan.nextInt();

		int c = condicao(x);

        scan.close();
        
        if (c == 0) {
            System.out.println("Número par"); 
        } else {
            System.out.println("Número impar");
        }
    }

    public static int condicao(int x) {
		if(x%2==0){
			return 0;
		}else{
			return -1;
		}  
    }
}