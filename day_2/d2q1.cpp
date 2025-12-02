#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

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
                if (digits % 2 == 0) {
                    int exp = digits / 2;

                    if (i % (long)pow(10, exp) == i / (long)pow(10, exp)) {
                        // cout << "start: " << start << " end: " << end << " i: " << i << endl;
                        acc += i;
                    }
                }
            }
        }
    }

    cout << acc << endl;
}

