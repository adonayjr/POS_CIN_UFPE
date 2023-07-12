/*(5) Desenvolva um algoritmo que preencha um vetor numérico de 5 posições. 
Após preencher todo o vetor, o usuário deve inserir uma chave de busca X. 
Caso exista algum número igual a X, dentro do vetor, o algoritmo deve mostrar, 
na tela, o índice da primeira posição na qual X foi encontrado. 
Caso contrário, o algoritmo deve se encerrar com uma única mensagem, dizendo "Chave não encontrada.".

OBS: para essa questão nao é obrigatório usar uma função...

* Exemplo de execução – Exercício 5 - Caso de teste 1
Insira o dado da posição  1:
11
Insira o dado da posição  2:
12
Insira o dado da posição  3:
13
Insira o dado da posição  4:
14
Insira o dado da posição  5:
15
Insira a chave de busca:
15
Chave encontrada na posição:  5

* Exemplo de execução – Exercício 5 - Caso de teste 2
Insira o dado da posição  1:
11
Insira o dado da posição  2:
12
Insira o dado da posição  3:
13
Insira o dado da posição  4:
14
Insira o dado da posição  5:
15
Insira a chave de busca:
20
Chave não encontrada! */
package PROGRAMACAO.JAVA.ATIVIDADES4.CASO5;

import java.util.Scanner;

public class caso5 {
    public static void main(String[] args) {
        int[] vetor = new int[5];
        
        preencherVetor(vetor);
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite a chave de busca (X): ");
        int chave = scanner.nextInt();
        
        int indice = buscarChave(vetor, chave);
        
        if (indice != -1) {
            System.out.println("Chave encontrada na posição: " + indice);
        } else {
            System.out.println("Chave não encontrada.");
        }
    }
    
    public static void preencherVetor(int[] vetor) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite os valores do vetor:");
        for (int i = 0; i < vetor.length; i++) {
            vetor[i] = scanner.nextInt();
        }
    }
    
    public static int buscarChave(int[] vetor, int chave) {
        for (int i = 0; i < vetor.length; i++) {
            if (vetor[i] == chave) {
                return i; // Retorna o índice da primeira ocorrência da chave
            }
        }
        
        return -1; // Retorna -1 caso a chave não seja encontrada
    }
}