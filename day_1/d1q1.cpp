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
            pos = pos % 100;
        } else {
            pos -= steps;
            while (pos < 0) {
                pos += 100;
            }
        }
        if (pos == 0) {
            cnt ++;
        }
    }

    cout << cnt << endl;
}

