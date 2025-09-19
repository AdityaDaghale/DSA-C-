#include<iostream>
using namespace std;


// <------- sum of n number------> 

int sumN(int n){
    int sum=0;
    for(int i=1;i<=n;i++){
        sum+=i;
    }
    return sum;
}


// <---- calculate N factorial ------> 
int factN( int n){
    int fact=1;
    for(int i=1; i<=n;i++){
        fact=fact*i;
    }
    return fact;
}


 


int main(){
// sum of n number 
    cout<<"sum of n number ="<<sumN(15)<<endl;
    cout<<"sum of n number ="<<sumN(88)<<endl;

// factorial of n number 
    cout<<"factorial of N number ="<<factN(3)<<endl;
    cout<<"factorial of N number ="<<factN(10)<<endl;   
    return 0;
 }