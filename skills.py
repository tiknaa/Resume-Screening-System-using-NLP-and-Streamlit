skills_db = [
"python",
"machine learning",
"deep learning",
"sql",
"tensorflow",
"pytorch",
"nlp",
"data analysis",
"statistics",
"java",
"c++",
"data science",
"docker",
"aws"
]
def extract_skills(text):

    found = []

    for skill in skills_db:

        if skill in text:
            found.append(skill)

    return found