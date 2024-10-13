def final_result(gathered_credits, credits_needed, enrolled_courses):

    if enough_credit(gathered_credits, credits_needed):
        final_print = (f"Enrollment finished! Maximum credits: {gathered_credits}.\n"
                       f"Courses: {', '.join(sorted(enrolled_courses))}")
    else:
        final_print = (f"You need to enroll in more courses! "
                       f"You have to gather {credits_needed - gathered_credits} credits more.")
    return final_print


def enough_credit(gathered_credits, credits_needed):
    return gathered_credits >= credits_needed


def gather_credits(credits_needed, *course_results ):
    enrolled_courses = []
    gathered_credits = 0

    for course, credit in course_results:
        if enough_credit(gathered_credits, credits_needed):
            break
        if course in enrolled_courses:
            continue
        enrolled_courses.append(course)
        gathered_credits += credit

    return final_result(gathered_credits, credits_needed,enrolled_courses)



print(gather_credits(
    80,
    ("Basics", 27),
))
