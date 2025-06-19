def generate_resume(name, email, skills):
    skills_list = skills.split(',')
    return {
        'name': name,
        'email': email,
        'skills': [skill.strip() for skill in skills_list]
    }
