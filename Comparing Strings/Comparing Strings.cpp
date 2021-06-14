#include <bits/stdc++.h>
using namespace std;
 
int main()
{   
    string string1,string2;
    
    cin >> string1 >> string2;
 
    if(string1.length() != string2.length())
    {
        cout <<"NO" << endl;
        return 0;
    }
 
    vector<int> swaping_elements;
    
    for(int i=0; i<string1.length(); i++)
    {
        if(string1[i] != string2[i])
        {
            swaping_elements.push_back(i);
        }
    }
    if(swaping_elements.size() != 2)
    {
        cout << "NO" << endl;
        return 0;
    }
 
    swap(string1[swaping_elements[0]], string1[swaping_elements[1]]);
 
    if(string1 == string2)
    {
        cout<<"YES"<<endl;
    }
    else
    {
        cout<<"NO"<<endl;
    }
    return 0;
    
}