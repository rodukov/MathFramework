#include <iostream>
using namespace std;

/* Good print function */
void print(string print_argument, bool end=true) {
    cout << print_argument;
    if(end){ cout << endl; }
}


int main() {
    string x1, x2, y1, y2;
    /* Inform user about rule */
    print("Enter 'x' to label as unknown");

    /* Get first fraction */
    print("numerator of first fraction > ", false); cin >> x1;
    print("denominator of first fraction > ", false); cin >> x2;

    /* Get second fraction */
    print("numerator of second fraction > ", false); cin >> y1;
    print("denominator of second fraction > ", false); cin >> y2;

    /* TUI View */
    print(x1, false); print("   ", false); print(y1, true);
    /* Draw '-' and equals symbol */
    for(short int c = 1; c <= x1.length(); c++) {
        if(c == x1.length()){ print("-", false); print(" = ", false); }
        else { print("-", false); }
    }
    /* Draw '-' */
    for(short int c = 1; c <= y1.length(); c++) {
        if(c == y1.length()){ print("-", true); }
        else { print("-", false); }
    }
    print(x2, false); print("   ", false); print(y2, true);

    print("Answer: ", false);
    if(x1 == "x") { cout << (std::stof(x2)*std::stof(y1))/std::stof(y2) << endl; }
    else if (x2 == "x") { cout << (std::stof(x1)*std::stof(y2))/std::stof(y1) << endl; }
    else if (y1 == "x") { cout << (std::stof(x1)*std::stof(y2))/std::stof(x2) << endl; }
    else if (y2 == "x") { cout << (std::stof(x2)*std::stof(y1))/std::stof(x1) << endl; }
    else { print("Fatal Error 'x' not found, watch README.md"); }
    return 0;
}