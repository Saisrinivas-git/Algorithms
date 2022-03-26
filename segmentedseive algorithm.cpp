#include<bits/stdc++.h>
using namespace std;
int n=10000001;
int primes[10000001];
void gen_seive()
{
    for(int i=0; i<n; i++)
    {
        primes[i]=1;
    }
    for(int i=2; i*i<n; i++)
    {
        if(primes[i])
        {
            for(int j=i*i; j<n; j+=i)
            {
                primes[j]=0;
            }
        }
    }
}
vector<int>gen_primes(int num)
{
    vector<int>v;
    for(int i=2; i<num; i++)
    {
        if(primes[i])
        {
            v.push_back(i);
        }
    }
    return(v);
}
int main()
{
    gen_seive();
    int t;
    int firstmul;
    cout<<"ENTER NO OF TEST CASES: ";
    cin>>t;
    while(t--)
    {
        int l,r;
        cin>>l>>r;
        vector<int> x=gen_primes(sqrt(r)+1);
        vector<int>dup(r-l+1,1);
        for(auto it:x)
        {
            if((l/it)*it < l)
            {
                firstmul=((l/it)+1)*it;
            }
            else
            {
                firstmul=(l/it)*it;
            }
            for(int j=firstmul; j<=r; j+=it)
            {
                dup[j-l]=0;
            }
        }
        for(int i=0; i<dup.size(); i++)
        {
            if(dup[i]==1)
            {
                cout<<l+i<<" ";
            }
        }
    }
}
