package PROGRAMACAO.JAVA.CODE_AULA.AULA2.decremento;

public class Decrement {

	public static void main(String[] args) {
		// demonstrate prefix decrement operator
		int c = 5;
		
//		System.out.println(" c before predecrement: "+c);
//		System.out.println("     predecrementing c: "+(++c));
//		System.out.println("  c after predecrement: "+c);
		
//		System.out.println(); // skip a line
		
		// demonstrate postfix decrement operator
		c = 5;
//		System.out.println(" c before postdecrement: "+c);
//		System.out.println("     postdecrementing c: "+(c++));
//		System.out.println("  c after postdecrement: "+c); // -> c = 6; 
		
		// c = c - 1;
		// c -= 1;
		// c--;
		// --c;
		
        int d, e;
        
        d = c--;
        System.out.println("c = "+c);
        System.out.println("d = "+d);
//        System.out.println("d = "+(d--));
        System.out.printf("d = %d\n", d--);
        System.out.println("d = "+d);
        
        System.out.println(); // skip a line
        
        e = --c;
        System.out.println("c = "+c);
        System.out.println("e = "+e);
	}

}