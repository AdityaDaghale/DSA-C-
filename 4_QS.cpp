#include<iostream>
using namespace std ;

// <------ calculate sum of digit number ------->

int sumOfDigits(int num){
    int digSum=0;

    while(num>0){
        int lastDigt=num%10;
        num=num/10;

        digSum+=lastDigt;
    } 
    return digSum;
}

int main(){
    cout<<" sum ="<<sumOfDigits(14505)<<endl;
    return 0;
}