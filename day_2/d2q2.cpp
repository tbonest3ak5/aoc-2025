#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

bool checkStr(long long num, int d) {
    bool ret = true;
    long long temp = -1;
    long long mod = pow(10, d);
    while (num > 0) {
        if (temp == -1) {
            temp = num % mod;
        } else {
            if (temp != num % mod) {
                ret = false;
                break;
            }
        }
        num /= mod;
    }

    return ret;
}

int main() {
    // Read from file
    ifstream inputFile("input.txt");
    if (!inputFile) {
        cerr << "Error: Could not open input.txt" << endl;
        return 1;
    }
    
    long long acc = 0;
    string line;
    while (getline(inputFile, line)) {
        stringstream ss(line);
        string range;
        while (getline(ss, range, ',')) {
            int split = range.find('-');
            long long start = stol(range.substr(0, split));
            long long end = stol(range.substr(split + 1));
            
            for (long long i = start; i <= end; i++) {
                int digits = (i == 0) ? 1 : log10(i) + 1;

                for (int d = 1; d <= digits/2; d ++) {
                    if (digits % d == 0) {
                        // check substrings of len d
                        if (checkStr(i, d)) {
                            cout << "start: " << start << " end: " << end << " i: " << i << endl;
                            acc += i;
                            break;
                        }
                    }
                }    
            }
        }
    }

    cout << acc << endl;
}

