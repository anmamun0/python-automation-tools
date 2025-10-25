#include <bits/stdc++.h>
typedef long long ll;
#define vl vector<ll> 
#define vi vector<int> 
#define in_range(i,s,n) for(int i=s; i<=n; i++)
#define in_range(i,s,n) for(int i=s; i<=n; i++)
#define in_range_back(i,s,n) for(int i=n ; i >= s; i--)
#define take_array(v,n) in_range(i,0,n) cin>>v[i]
#define print_array(v) for(auto c:v){cout<<c<<" ";}cout<<ln
#define erase_duplicates(x) x.erase(unique(all(x)),x.end());
#define cin2(a, b) cin >> a >> b;
#define cin3(a, b, c) cin >> a >> b >> c;
#define all(x) x.begin(),x.end()
#define all_0(x) memset(x,0,sizeof(x))
#define isEven(x) ((x&1)== 0)
#define yes cout << "YES\n"
#define no cout << "NO\n"
#define enter cout << "\n"
#define ln '\n'
#define PQ priority_queue
#define Hashmap unordered_map
#define pb push_back
#define gcC int main()
#define checkmate return 0;
 
using namespace std;
// using namespace __gnu_pbds;
string Password_Genarat(int n)
{
    srand(time(0));
    string sequence = ""; //65

    for (int i = 35; i <= 122; i++)
    {
        if(i>=39 and i<=47) continue;
        if(i>=58 and i<=63) continue;
        if(i>=91 and i<=97) continue;
        char c = i;
        sequence += c;
    }

    string created = "";
    for (int i = 0; i < n;i++) created += sequence[rand() % 65];
    
    return created;
}
gcC
{
  /* _Coder   : anmamun0
     _Created : 22 April 2024 ||  01:03:43
     _File    : pass_gen.cpp 
 
    بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ */
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int len;    cin>>len;
    string pass = Password_Genarat(len);

    cout << pass << endl;

    checkmate;
}