package PROGRAMACAO.JAVA.AULA2.Strings;

import java.util.Arrays;

public class Strings {

	public static void main(String[] args) {
		// String are sequences of characters

		//		String name = "Henrique";
		//		int size = name.length();
		//		System.out.println("The String "+name+" has size = "+size);

		String empty = "";
		System.out.println(empty.length());

		String fName = "Henrique";
		String lName = "Rebelo";
		String name = fName + " E M "+ lName;
		System.out.println(name);

		char start = name.charAt(0);
		char last = name.charAt(name.length() - 1);

		System.out.println(start);
		System.out.println(last);

		// Substrings
		String subStr = name.substring(3, fName.length());
		System.out.println("subStr = "+subStr);

		// Substrings
		String subStr2 [] = name.split("");
		System.out.println(Arrays.toString(subStr2));
//		System.out.println(subStr2[3]);

		// Equality tests
		String word1 = "Java";
		//		String word2 = "AspectJ";
		String word3 = new String("JAva");

		// Do not use this for String comparison!
//		System.out.println(word1 == word3);
		System.out.println(word1.equals(word3));

//		if(word1.equalsIgnoreCase(word3)){
//			System.out.println("Yes!");
//		}
//		else {
//			System.out.println("Not equal!");
//		}
	}
}