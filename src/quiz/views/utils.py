def is_teacher(user):
    return user.groups.filter(name="TEACHER").exists()


def is_student(user):
    return user.groups.filter(name="STUDENT").exists()
