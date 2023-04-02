package hackerrank.grading;

import java.util.List;

class Result {
    public static List<Integer> gradingStudents(List<Integer> grades) {
        for (int i = 0; i < grades.size(); i++) {
            if (grades.get(i) >= 38) {
                int x = grades.get(i) % 5;
                if (x >= 3) {
                    grades.set(i, grades.get(i) + 5 - x);
                }
            }
        }
        return grades;
    }

    public static void main(String[] args) {
        Result result = new Result();
        List<Integer> lst = new List<Integer>() {
            73, 63, 38, 33
        };
        System.out.println(result.gradingStudents(lst));
    }
}