int* gradingStudents(int grades_count, int* grades, int* result_count) {
    for (int i = 0; i < grades_count; i++) {
        if (grades[i] >= 38) {
            int x = grades[i] % 5;
            if (x >= 3) {
                grades[i] += (5 - x);
            }
        }
    }
    return grades;
}