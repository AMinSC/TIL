#include <string>
#include <vector>

using namespace std;

int solution(int a, int b) {
    int sum_a_b = std::stoi(std::to_string(a) + std::to_string(b));
    int sum_b_a = std::stoi(std::to_string(b) + std::to_string(a));
    
    return sum_a_b > sum_b_a ? sum_a_b : sum_b_a;
}