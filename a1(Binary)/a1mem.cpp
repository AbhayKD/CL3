#include<iostream>
#include"stdio.h" 
#include <string>
#include <fstream>
#include <stdlib.h>
#include <vector>

using namespace std;

void Binary_Search(int arr[],int num,int first,int last){
    if(first>last){
        cout<<"\nElement not Found...";
    }
    else{
        int mid;
        /*Calculate mid element*/ mid=(first+last)/2;

        if(arr[mid]==num){
            cout<<"\nElement found at index:"<<mid+1;
        }
        else if(arr[mid]>num){
             Binary_Search(arr,num,first,mid-1);
        }
        else{
            Binary_Search(arr,num,mid+1,last);
        }
    }
}


int main(){

int arr[20],beg,mid,end,num,i,j,n,temp,number;
fstream myfile;
vector<int> numbers;

myfile.open("example.txt", ios::in | ios::binary);  
  if (myfile.is_open())
  {
    while (myfile >> number )
    {
      numbers.push_back(number);
      myfile.get();
    }
    myfile.close();
  }
  else cout << "Unable to open file";
 
  std::copy(numbers.begin(), numbers.end(), arr);
  n = numbers.size();
  cout << "\nArray before sorting:";
  for (int i=0; i < n; i++) {
    cout << arr[i] << '\n' ;
  }


for(i=0;i<n;i++)	// Loop for Pass
{
    for(j=i+1;j<n;j++)
    {
        if(arr[i]>arr[j])
        {
            temp=arr[i];	// Interchange Values
            arr[i]=arr[j]; 
            arr[j]=temp;
        }
    }
}

cout<<"\nArray after sorting:";
for(i=0;i<n;i++)
{
cout<<arr[i]<<endl;
}


beg=0; end=n-1;
cout<<"\nEnter a value to be search:"; 
cin>>num;
Binary_Search(arr,num,beg,end);
 return(0);
}
