#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int sum_a_b = stoi(to_string(a) + to_string(b));
    int sum_b_a = stoi(to_string(b) + to_string(a));
    
    return sum_a_b > sum_b_a ? sum_a_b : sum_b_a;
}