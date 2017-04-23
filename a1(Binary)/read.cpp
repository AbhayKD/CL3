#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
using namespace std;

int main () {
  fstream myfile;
  vector<int> num;
  int result, i,a[100];
  myfile.open("example.txt", ios::in | ios::binary);
  
  if (myfile.is_open())
  {
    while (myfile >> result )
    {
      num.push_back(result);
      myfile.get();
    }
    myfile.close();
  }

  else cout << "Unable to open file"; 
  
  std::copy(num.begin(), num.end(), a);
  for (int i=0; i < num.size(); i++) {
    cout << a[i] << '\n';
  }

   return 0;
}
