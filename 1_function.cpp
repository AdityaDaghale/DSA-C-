#include<iostream>
using namespace std;

//sum of 2 number --->
int sum(int a,int b){
    int s= a+b;
    return s;
}
 // min of 2 number--->
 int minOfTow(int a,int b){
    if(a<b){
        return a;
    }
    else{
        return b;
    }
 }

int main(){
    cout<<sum(10,5)<<endl;;
    cout<<minOfTow(15,5)<<endl;;
    return 0;

}