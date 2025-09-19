#include<iostream>
using namespace std;

 
// < ------ example of paas by value -----> 


void changex(int x){
    x=2*x;
    cout<<" x="<<x<<endl;
}

int main(){
    int x=5;
    changex(x);

    cout<<" x="<<x<<endl;
    return 0;
}