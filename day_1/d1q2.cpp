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
    
    int pos = 50;
    int cnt = 0;
    string line;
    while (getline(inputFile, line)) {
        char dir = line[0];
        int steps = stoi(line.substr(1));
        if (dir == 'R') {
            pos += steps;
            while (pos >= 100) {
                pos -= 100;
                cnt ++;
            }
        } else {
            int orgPos = pos;
            pos = pos - steps;
            if (pos == 0) {
                cnt ++;
            }
            if (pos < 0) {
                if (pos % 100 == 0) {
                    cnt ++;
                }
                while (pos < 0) {
                    pos += 100;
                    cnt ++;
                }
                if (orgPos == 0) {
                    cnt --;
                }
            }
        }
    }

    cout << cnt << endl;
}

