from typing import List

def gradingStudents(grades: List[int]) -> List[int]:
    for i in range(0, len(grades)):
        if grades[i] >= 38:
            x = grades[i] % 5
            if x >= 3:
                grades[i] += (5 - x)

    return grades