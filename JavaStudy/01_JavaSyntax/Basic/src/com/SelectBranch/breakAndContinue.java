package com.SelectBranch;

public class breakAndContinue {

    public static void main(String[] args) {

        //  break
        int sum=0;
        for (int i=0;i<101;i++){
            sum+=i;
            if (i==10){
                break;
            }
        }
        System.out.println(sum );
        // continue
        sum=0;
        for (int i=0;i<101;i++){
            if (i%2==0){
                continue;
            }
            sum+=i;
        }
        System.out.println(sum );
    }
}
