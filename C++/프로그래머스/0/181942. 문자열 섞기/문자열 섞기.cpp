#include <string>
#include <vector>

using namespace std;

string solution(string str1, string str2) {
    string answer = "";
    string total_str = str1 + str2;
    int s1_len = str1.size();
    int s2_len = str2.size();
    int s1_i = 0;
    int s2_i = 0;
    
    for (int i = 0; i < total_str.size(); i++)
    {
        if (s1_i < s1_len)
        {
            answer += str1[s1_i];
            s1_i++;
        }
        if (s2_i < s2_len)
        {
            answer += str2[s2_i];
            s2_i++;
        }
    }
    
    return answer;
}