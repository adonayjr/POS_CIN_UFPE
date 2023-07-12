/*(3) Desenvolva um algoritmo que peça para o usuário inserir vários números inteiros. 
O algoritmo deverá contabilizar a quantidade de números positivos informados. 
Caso o usuário digite 0, o algoritmo deve mostrar quantidade contabilizada e encerrar.

* Exemplo de execução – Exercício 3 - Caso de teste
Insira um número:
5
Insira um número:
5
Insira um número:
-1
Insira um número:
0
Quantidade de positivos: 2 */

package PROGRAMACAO.JAVA.ATIVIDADES3.atividade3;

import java.util.Scanner;

public class case3 {
    public static void main(String[] args) {
    	Scanner input = new Scanner(System.in);

        int numero = 0;
        int i = 0;

		System.out.printf("Insira um numero( 0 = parar):\n");
		numero = input.nextInt();

		while(numero!=0){
            if (numero>0){
                i = i + 1;
            }
            System.out.printf("Insira um numero( 0 = parar):\n");
		    numero = input.nextInt();
		}
        input.close(); //fechando o buffer
        System.out.printf("Quantidade de positivos: "+ i);
	}  
}



