#include <iostream>
#include <cassert>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int subs(int a, int b) {
    return a - b;
}

int mul(int a, int b) {
    return a * b;
}

double divide(int a, int b) {
    return static_cast<double>(a) / b;
}

int main() {
    assert(add(2, 3) == 5);
    assert(subs(2, 3) == -1);
    assert(mul(2, 3) == 6);
    assert(divide(6, 3) == 2);

    cout << "All tests passed." << endl;
    return 0;
}
