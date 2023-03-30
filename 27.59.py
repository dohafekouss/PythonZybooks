current_grade = float(input())
current_points = current_grade * 0.6
points_needed = 90 - current_points
grade_on_final = points_needed / 40
print("{:.1%}".format(grade_on_final))