package com.SelectBranch;

public class for01 {
    public static void main(String[] args) {
        int sum = 0;
        // for循环求1-100偶数和
        for (int i=0;i<101;i++){
            if (i%2==0){
                sum+=i;
            }
        }
        System.out.println(sum);
        System.out.println("=========");

        // while循环求1-100偶数和
        sum =0 ;
        int i = 0;
        while (i<101){
            if (i%2==0){
                sum+=i;
            }
            i++;
        }
        System.out.println(sum);
        System.out.println("=========");

        // do while循环求1-100偶数和
        i=0;
        sum =0 ;
        do {
            if (i%2==0){
                sum+=i;
            }
            i++;
        }while (i<101);
        System.out.println(sum);
        System.out.println("=========");

        // for循环打印99乘法表
        for (int a =1;a<10;a++){
            for (int b = 1;b<=a;b++){
                    if (b!=1&a*b<10){System.out.print(b+"x"+a+"="+a*b+"    ");}
                    else {System.out.print(b+"x"+a+"="+a*b+"   "); }
                }
            System.out.println("");
        }
    }
}
