/*(4) Desenvolva um algoritmo que peça ao usuário que preencha os dados de um vetor de 5 posições com valores reais quaisquer, 
desde que estejam compreendidos entre 1 e 100 (suponha que o usuário irá respeitar o enunciado). 
Depois, faça o design de uma função "dividir100" que divide o conteúdo de cada posição do vetor por 100. Ao final, 
o programa deve mostrar, na tela, o conteúdo de cada posição do vetor, dividido por 100.
* Exemplo de execução – Exercício 4 - Caso de teste
Insira o dado da posição  1:
10
Insira o dado da posição  2:
20
Insira o dado da posição  3:
30
Insira o dado da posição  4:
40
Insira o dado da posição  5:
50
Conteúdo dividido por 100:
 0.1
 0.2
 0.3
 0.4
 0.5
 */
package PROGRAMACAO.JAVA.ATIVIDADES4.CASO4;

import java.util.Scanner;

public class caso4 {
    public static void main(String[] args) {
        double[] vetor = new double[5];
        
        preencherVetor(vetor);
        dividir100(vetor);
        exibirVetorDividido(vetor);
    }
    
    public static void preencherVetor(double[] vetor) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite os valores do vetor (entre 1 e 100):");
        for (int i = 0; i < vetor.length; i++) {
            double valor = scanner.nextDouble();
            
            // Verifica se o valor está entre 1 e 100
            if (valor >= 1 && valor <= 100) {
                vetor[i] = valor;
            } else {
                System.out.println("Valor inválido. Digite novamente:");
                i--; // Volta uma posição para digitar o valor novamente
            }
        }
    }
    
    public static void dividir100(double[] vetor) {
        for (int i = 0; i < vetor.length; i++) {
            vetor[i] /= 100;
        }
    }
    
    public static void exibirVetorDividido(double[] vetor) {
        System.out.println("Conteúdo do vetor dividido por 100:");
        for (int i = 0; i < vetor.length; i++) {
            System.out.println(vetor[i]);
        }
    }
}