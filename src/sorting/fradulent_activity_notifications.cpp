#include <iostream>
#include <vector>
using namespace std;
typedef vector<int> vi;

// https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

vi getCounts(const vi& v, int maxElement) {
  vi counts(maxElement + 1);
  for (int i = 0; i < v.size(); ++i)
    ++counts[v[i]];
  
  return counts;
}

int nextNonZero(const vi& v, int n) {
  for (int i = n + 1; i < v.size(); ++i)
    if (v[i]) return i;
  return -1;
}

float median(const vi& counts, int len) {
  int counted = 0;
  for (int n = 0; n < counts.size(); ++n) {
    counted += counts[n];
    if (counted > len/2) return n;
    else if (counted == len/2 && len % 2 == 0)
      return (n + nextNonZero(counts, n))/2.0;
  }
  return 0;
}

int countFrauds(const vi& exp, int d) {
  int frauds = 0;
  vi counts = getCounts(vector<int> (exp.begin(), exp.begin() + d), 200);
  for (int i = d; i < exp.size(); ++i) {
    if (exp[i] >= 2*median(counts, d)) ++frauds;
    ++counts[exp[i]];
    --counts[exp[i-d]];
  }
  return frauds;
}

int main() {
  int n, d;
  cin >> n >> d;
  vector<int> exp(n);
  for (int i = 0; i < n; ++i)
    cin >> exp[i];
  
  cout << countFrauds(exp, d) << "\n";
}
