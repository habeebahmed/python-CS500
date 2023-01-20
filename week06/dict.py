
from typing import Dict, List


def get_average(scores: Dict[str, List[int]]) -> Dict[str, float]:
    average: dict[str, float] = {}
    for key, value in scores.items():
        name: str = key
        scorelist: List[int] = value
        sum: int = 0
        for score in scorelist:
            sum += score
        avg: float = sum / len(scores)
        average[name] = avg
    return average

def get_best_student(scores: Dict[str, List[int]]) -> str:
    avg_scores: Dict[str, float] = get_average(scores)
    max_score: float = 0
    highest_scorer: str = ""
    for key, value in avg_scores.items():
        if max_score < value:
            max_score = value
            highest_scorer = key

    return highest_scorer

def get_best_students(scores: Dict[str, List[int]]) -> List[str]:
    avg_scores: Dict[str, float] = get_average(scores)
    best_students_list: list[str] = []
    for name in avg_scores:
        if avg_scores[name] > 8:
            best_students_list.append(name)
    return best_students_list


def main() -> None:
    courses: dict[str, str] = {"CS204": "C Prog", "CS500": "Python", "CS500L": "Python Lab"}
    print(courses)

    for k, v in courses.items():
        print(k, v)
    
    scores: dict[str, List[int]] = {}
    scores["Peter"] = [8, 9, 10]
    scores["Lily"] = [7, 10, 8]
    scores["Jum"] = [7, 6, 8]
    # for key in scores:
    #     print(key, scores[key])
    avg_scores: dict[str, float] = get_average(scores)
    print(avg_scores)
    print("The highest scorer", get_best_student(scores))
    print()
    print("Best students list", get_best_students(scores))


if __name__=="__main__":
    main()