package PROGRAMACAO.JAVA.AULA1.scan2;

import java.util.Scanner;

public class Scan2 {

	public static void main(String[] args) {
		// create a Scanner to obtain input from the console
		Scanner input = new Scanner(System.in);
		
		int idade = 0;
		int ano = 1950;
		double peso = 0.0; 

		System.out.printf("Valor inicial da idade: %d.\n", idade);

		System.out.printf("Digite uma idade:\n");
		idade = input.nextInt();
		System.out.printf("Digite um ano:\n");
		ano = input.nextInt();
		
		System.out.printf("Digite um peso:\n");
		peso = input.nextDouble();
		
		System.out.printf("Idade informada: %d.\n", idade);
		System.out.printf("Ano informado: %d.\n", ano);
		System.out.printf("Peso informado: %.2f.\n", peso);
		
		input.close(); //fechando o buffer
	}
}