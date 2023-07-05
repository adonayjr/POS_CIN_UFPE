package PROGRAMACAO.JAVA;

import java.util.Scanner;

public class scan {

	public static void main(String[] args) {
		// create a Scanner to obtain input from the console
		Scanner scan = new Scanner(System.in);
		
		int A, B, soma, subtr, mult, div;
		   
	    System.out.printf("Digite o primeiro valor: \n");
	    A = scan.nextInt();
	    System.out.printf("Digite o segundo valor: \n");
	    B = scan.nextInt();
	   
	    soma = A + B;
	    subtr = A - B;
	    mult = A * B;
	    div = A / B;
	   
	    System.out.printf("Resultados: \n");
	    System.out.printf("Soma: %d.\n", soma);
	    System.out. printf("Subtra.: %d.\n", subtr);
	    System.out.printf("Mult.: %d.\n", mult);
	    System.out.printf("Div.: %d.\n", div);
		
		scan.close(); //fechando o buffer
	}
}