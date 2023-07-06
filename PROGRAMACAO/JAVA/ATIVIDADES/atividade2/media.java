/** Exemplo de execução – Exercício 2 - Caso de teste
Informe três notas, em sequência:
5,5
6,0
6,5
Média aritmética:  6
 */

package PROGRAMACAO.JAVA.ATIVIDADES.atividade2;

import java.util.Scanner;

public class media {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double numero1 = 0.0;
        double numero2 = 0.0;
        double numero3 = 0.0;
        double media = 0.0;

		System.out.printf("Digite numero1:\n");
		numero1 = input.nextDouble();
		System.out.printf("Digite numero2:\n");
		numero2 = input.nextDouble();
        System.out.printf("Digite numero3:\n");
		numero3 = input.nextDouble();

        media = (numero1 + numero2 + numero3)/3;

        System.out.printf("Sua média =  "+media);

        input.close(); //fechando o buffer

}
}