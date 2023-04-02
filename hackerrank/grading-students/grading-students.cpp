#include <bits/stdc++.h>
using namespace std;

vector<int> gradingStudents(vector<int> grades) {
    for (int i = 0; i < grades.size(); i++) {
        if (grades[i] >= 38) {
            int x = grades[i] % 5;
            if (x >= 3) {
                grades[i] += (5 - x);
            }
        }
    }

    return grades;
}