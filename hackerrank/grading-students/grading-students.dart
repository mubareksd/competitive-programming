List<int> gradingStudents(List<int> grades) {
  for (int i = 0; i < grades.length; i++) {
    if (grades[i] >= 38) {
      int nextMultipleOfFive = (grades[i] / 5).ceil() * 5;
      if (nextMultipleOfFive - grades[i] < 3) {
        grades[i] = nextMultipleOfFive;
      }
    }
  }
  return grades;
}

int main() {
    print(gradingStudents([73, 67, 38, 33]));
    return 0;
}