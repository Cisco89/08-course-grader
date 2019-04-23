def course_grader(scores):
    
    pass_fail = "fail"

    for number in scores:
        if number < 50:
            return pass_fail
        
    average = sum(scores) / len(scores)
    
    if average >= 70:
        pass_fail = "pass"
        return pass_fail
    
    return pass_fail
