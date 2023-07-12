package PROGRAMACAO.JAVA.CODE_AULA.AULA2.VarsAndConstants;

import java.util.Scanner;

public class VarsAndConstants {

	public static void main(String[] args) {
		// create a Scanner to obtain input from the console
//		Scanner scan = new Scanner(System.in);
		Scanner scan = new Scanner(System.in).useDelimiter("\n");
		
		final String TEXTO = "Entrada e saida de dados."; // constante!!
		System.out.printf("%s\n", TEXTO);

		int idade = 0;
		double altura = 0.0;
		String nome = "";

		System.out.printf("Digite a idade:\n");
		idade = scan.nextInt();

		System.out.printf("Digite a altura:\n");
		altura = scan.nextDouble();

		System.out.println("Digite o nome:");
		nome = scan.next();

		System.out.println();
		System.out.printf("Dados informados:\n");
		System.out.printf("Idade %d.\n", idade);
		System.out.printf("Altura %.2f.\n", altura);
		System.out.printf("Nome %s.\n", nome);

		scan.close(); //fechando o buffer
	}
}
