/*(2) Faça o design de uma função "isFirstGreater" que receba três números. 
No final o programa deve imprimir "Condição satisfeita", na tela, 
caso o primeiro dado inserido seja maior do que os outros dois (o primeiro não pode ser igual a nenhum). 
Caso contrário, deve ser impressa a mensagem: "Erro". OBS: use vetor/array de 3 posicoes para armazenar os numeros lidos.

*Exemplo de execução – Exercício 2 - Caso de teste 1
Insira o primeiro número:
3
Insira o segundo número:
2
Insira o terceiro número:
1
Condição satisfeita
*Exemplo de execução – Exercício 2 - Caso de teste 2
Insira o primeiro número:
2
Insira o segundo número:
3
Insira o terceiro número:
1
Erro

*Exemplo de execução – Exercício 2 - Caso de teste 3
Insira o primeiro número:
2
Insira o segundo número:
2
Insira o terceiro número:
1
Erro */

package PROGRAMACAO.JAVA.ATIVIDADES4.CASO2;

import java.util.Scanner;

public class caso2 {
	 public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

		int x, y, z;
        
		System.out.printf("Digite num 1: \n");
		x = scan.nextInt();
		System.out.printf("Digite num 2: \n");
		y = scan.nextInt();
		System.out.printf("Digite num 2: \n");
		z= scan.nextInt();

		int c = condicao(x, y, z);

        scan.close();
        
        if (c == 0) {
            System.out.println("Condição perfeita"); 
        } else {
            System.out.println("Erro");
        }
    }

    public static int condicao(int x, int y, int z) {
        if ((x > y && x > z) || (y < x && y > z) || (z < x && y > z)) {
            return 0;
        } else {
            return -1;
        }
    }
}