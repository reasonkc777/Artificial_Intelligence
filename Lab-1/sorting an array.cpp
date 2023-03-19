//sort an array of integers
#include <iostream>
#define MAX 100
using namespace std;
int main(){
	int arr[MAX];
	int n,i,j;
	int temp;
	cout<<"Enter total number of elements to read: ";
	cin>>n;
	if(n<0 || n>MAX){
		cout<<"Input valid range!!!"<<endl;
		return -1;
	}
	for(i=0;i<n;i++)
	{
		cout<<"Enter element ["<<i+1<<"] ";
		cin>>arr[i];
	}
	cout<<"Unsorted Array elements:"<<endl;
	for(i=0;i<n;i++)
		cout<<arr[i]<<"\t";
	cout<<endl;
	for(i=0;i<n;i++)
	{		
		for(j=i+1;j<n;j++)
		{
			if(arr[i]>arr[j])
			{
				temp  =arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
	}
	cout<<"Sorted (Ascending Order) Array elements:"<<endl;
	for(i=0;i<n;i++)
		cout<<arr[i]<<"\t";
	cout<<endl;	
	return 0;
	
}
    
