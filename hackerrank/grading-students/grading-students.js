function gradingStudents(grades) {
  for (let i in grades) {
    if (grades[i] >= 38) {
      const x = grades[i] % 5;
      if (x >= 3) grades[i] += 5 - x;
    }
  }
  return grades;
}
