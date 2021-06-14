#include <bits/stdc++.h>
using namespace std;
 
  int main() {
  int pages_to_be_read;
  cin >> pages_to_be_read;
  
  int page_on_day[7];
  
  for(int day = 0;day < 7;day++)
     cin >> page_on_day[day];
     
  int day = 0;     
  while(pages_to_be_read > 0)
  {   
      pages_to_be_read -= page_on_day[day];
      if (pages_to_be_read <= 0)
         cout << (day+1) << "\n";
      day += 1;
      if (day >= 7)
          day = 0;
      
      
  }
}