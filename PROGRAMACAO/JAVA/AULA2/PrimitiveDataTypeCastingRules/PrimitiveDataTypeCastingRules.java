package PROGRAMACAO.JAVA.AULA2.PrimitiveDataTypeCastingRules;

public class PrimitiveDataTypeCastingRules {

	public static void main(String[] args) {
		// Primitive data type casting rules [regras de coercao]

		int i = 10;
		double d = 10.5;
		float f = 10.5f;
		
		// widening conversion [op. alargamento]
		d = i; // cast implicito
		
		// narrowing conversion [op. estreitamento]
		i = (int)d; // cast explicito
		
		float f2 = (float)(f + d);
		double d2 = f + d;
		
		// int + int -> int
		// double + double -> double
		// float + float -> float
		// long + long -> long
		// int + float -> float
		// int + double -> double
		// int + long -> long
		// float + double -> double
		
		byte b, b2 = 10, b3 = 10;
		
		b = (byte)(b2 + b3);
		
		short s, s2 = 10, s3 = 10;
		
		s  = (short)(s2 + s3);


	}
}