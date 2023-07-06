package PROGRAMACAO.JAVA.AULA1.incremento;

public class incremento {

    public static void main(String[] args) {

    int c = 5;

    int d, e, f, g;

    d = c++;
    System.out.println("C = " + c);
    System.out.println("C = " + d);
    e = ++c;
    System.out.println("C = " + c);
    System.out.println("C = " + e);
    f = c--;
    System.out.println("C = " + c);
    System.out.println("C = " + f);
    g = --c;
    System.out.println("C = " + c);
    System.out.println("C = " + g);
}

}