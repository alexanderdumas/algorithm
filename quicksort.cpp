#include<iostream>
using namespace std;

void swap(int a[],int i,int j){
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

void quicksort(int a[], int begin,int end){
    if(begin+1>end){
        return;
    }
    int temp = a[begin];
    int i = begin;
    int j = end;

    while(i!=j){
        while(i<j && a[j] >= temp){
            j--;
        } 
        while(i<j && a[i] <= temp){
            i++;
        }
        if(i<j){
            swap(a,i,j);
        }
    }
    if(i!=begin){
        swap(a,i,begin);
    }
    quicksort(a,begin,i-1);
    quicksort(a,i+1,end);
}

void print(int a[], int k){
    for(int i=0;i<=k; i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
}

int main(){
    int a[] = {1,5,4,3,10,7};
    int len = sizeof(a)/sizeof(a[0]);
    print(a,len-1);
    quicksort(a,0,len-1);
    print(a,len-1);
}