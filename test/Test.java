package test;

public class Test {
    public static int add(int a, int b) {
        return a + b;
    }

    public static int subs(int a, int b) {
        return a - b;
    }

    public static int mul(int a, int b) {
        return a * b;
    }

    public static double div(int a, int b) {
        return (double) a / b;
    }

    public static void main(String[] args) {
        assert add(2, 3) == 5 : "Test for add failed";
        assert subs(2, 3) == -1 : "Test for subs failed";
        assert mul(2, 3) == 6 : "Test for mul failed";
        assert div(6, 3) == 2 : "Test for div failed";

        System.out.println("All tests passed.");
    }
}
