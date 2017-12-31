#include <iostream>
typedef unsigned long ul;
using namespace std;

// https://www.hackerrank.com/challenges/sum-vs-xor

int main() {
  ul n;
  cin >> n;

  if (!n) cout << 1 << "\n";
  else {
    ul one = 1;
    ul allFilled = (one << (64 - __builtin_clzl(n))) - 1;
    cout <<  (one << __builtin_popcountl(allFilled ^ n)) << "\n";
  }
}
