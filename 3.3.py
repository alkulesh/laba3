timetable = {}
with open("Расписание.txt", "r", encoding="utf-8") as file:
    for line in file:
        subject, lessons = line.strip().split(": ")
        lessons = lessons.split(" ")
        total_lessons = 0
        for lesson in lessons:
            count, type = lesson.strip("()").split("(")
            total_lessons +=int(count)
            timetable[subject]=total_lessons
print(timetable)
