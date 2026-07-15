#include <string>
#include <vector>

using namespace std;

string solution(string str1, string str2) {
    string answer = "";
    int s1_i = 0;
    int s2_i = 0;
    
    for (int i = 0; i < str1.size(); i++)
    {
        answer += str1[s1_i++];
        answer += str2[s2_i++];
    }
    
    return answer;
}