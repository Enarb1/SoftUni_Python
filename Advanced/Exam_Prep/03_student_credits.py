def final_result(total_credits, courses):

    if total_credits >= 240:
        final_print = f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        final_print = f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

    course_sorted = sorted(courses.items(), key=lambda r: r[1], reverse=True)
    final_print += '\n'.join(f"{course_name} - {d_credit:.1f}" for course_name, d_credit in course_sorted)

    return final_print


def students_credits(*results):
    courses = {}
    total_credits = 0

    for score in results:
        course,course_credits,max_points,test_score = score.split("-")
        percentage = int(test_score) / int(max_points)
        earned_credits = int(course_credits) * percentage
        courses[course] = courses.get(course, earned_credits)
        total_credits += earned_credits

    return final_result(total_credits, courses)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)