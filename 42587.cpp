#include <string>
#include <vector>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0, cnt = 9, cur = 0, turn = 1;
    int np[10] = {0, };
    int jool[100] = {0, };
    for( int p : priorities ) np[p]++;
    while( cnt > 0 ) {
        if( !np[cnt] ) {
            cnt--;
            continue;
        }
        while( jool[cur] || priorities[cur] != cnt ) {
            cur = (cur+1)%priorities.size();
        }
        np[cnt]--;
        jool[cur] = turn++;
        if( cur == location ) {
            answer = jool[cur];
            break;
        }
    }
    return answer;
}
