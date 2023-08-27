#include<iostream>

using namespace std;

void print(int a[], int size){
    for(int i=0; i<size; i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
}

void swap(int a[], int i, int j){
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

void heapUp(int a[], int size){
    for(int i=0; i<size; i++){//调整所有的节点
        int cur = i;
        int father = (i-1)/2;
        while(a[cur] > a[father]){
            swap(a,cur,father);
            cur = father;
            father = (cur-1)/2;
        }
        //print(a,size);
    }
}

void heapDown(int a[], int index, int size){
    int left = 2 * index + 1;
    int right = 2 * index + 2;
    while(left < size){
        int maxindex = 0;
        if(right < size && a[left] < a[right]){
            maxindex = right;
        }else{
            maxindex = left;
        }
        if(a[index] > a[maxindex]){
            break;
        }
        swap(a,index,maxindex);
        left = 2 * maxindex + 1;
        right = 2 * maxindex + 2;
    }
}

void heapsort(int a[], int size){
    heapUp(a,size);
    //print(a,size);
    while(size > 1){//小于1个不处理
        swap(a,0,size-1);
        size--;
        heapDown(a,0,size);
    }
}

int main(){
    int a[] = {1,4,3,2,8,6};
    int len = sizeof(a)/sizeof(a[0]);
    print(a,len);
    heapsort(a,len);
    print(a,len);
}