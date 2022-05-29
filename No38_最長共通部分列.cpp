#include <bits/stdc++.h>
using namespace std;

string A;
string B;

int solve(int x, int y){
    int lx = x;
    int ly = y;

    vector<vector <int>> dp(lx + 1, vector<int>(ly+1));
    for(int i=0; i<=lx; i++){
        for(int j=0;j<=ly; j++){
            dp[i][j] = 0;
        }
    }
    for(int i=0; i<lx; i++){
        for(int j=0;j<ly; j++){
            if(A[i] == B[j]){
                dp[i+1][j+1] = dp[i][j] + 1;
            }else if(dp[i][j+1] > dp[i+1][j]){
                dp[i+1][j+1] = dp[i][j+1];
            }else{
                dp[i+1][j+1] = dp[i+1][j];
            }
        }
    }
    // for(int i=0;i<=x;i++){
    //     for(int j=0;j<=y; j++){
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    return dp[lx][ly];
}

int main(){
    int q;
    cin >> q;

    for(int i=0; i<q;i++){
        A = "";
        B = "";
        cin >> A;
        cin >> B;

        cout << solve(A.size(), B.size()) << endl;
    }
}