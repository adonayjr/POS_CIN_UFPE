/*(1) Desenvolva um algoritmo que some todos os números inteiros compreendidos entre 1 e 10 (inclusive).

*Exemplo de execução – Exercício 1 - Caso de teste
Somatório:  55 */

package PROGRAMACAO.JAVA.ATIVIDADES3.atividade1;

public class caso1 {
	 public static void main(String[] args) {
		int soma = 0;
    			    
		for(int i = 1; i <= 10; i++ ){
			soma = soma + i;
			i++;
			
		}
		System.out.printf("%d ", soma);
	}
}