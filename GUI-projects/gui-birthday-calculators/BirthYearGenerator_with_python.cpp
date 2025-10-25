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
bool isLeapYear(int year) 
{
    if (year % 400 == 0) return true;
    if (year % 100 == 0) return false;
    if (year % 4 == 0) return true;
    return false;
}
int daysInYear(int year) {
    return isLeapYear(year) ? 366 : 365;
}
int daysInMonth(int year, int month) {
    if (month == 2) return isLeapYear(year) ? 29 : 28; 
    else {
        vi mnt = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        return mnt[month - 1];
    }
}
gcC
{
  /* _Coder   : anmamun0
     _Created : 01 June 2024 ||  01:21:30
     _File    : detactYear.cpp 
 
    بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ */
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int y = 2004 ,m = 4, day = 12; 
    
    time_t t = time(0);
    tm* now = localtime(&t);
    int cY = now->tm_year + 1900, cM = now->tm_mon + 1, cD = now->tm_mday;


    // Days from April 12, 2004, to December 31, 2004
    int fast = daysInMonth(y,m-1) - day;
    for (int i = m; i < 12; i++) fast += daysInMonth(y, i + 1); 

    // Days from January 1 to today in the current year
    int last = cD;
    for (int i = 1; i < cM; i++) last += daysInMonth(cY, i);

    int total = 0;
    for (int year = y + 1; year < cY; year++) total += daysInYear(year); 
    
    total += fast + last;
 
    cout << total << endl;

    cout << total / 365 << endl;
    int exday = total % 365;
    cout << exday << endl; 

    // hasdfkj;
    checkmate;
}