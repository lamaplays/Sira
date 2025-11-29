
## Personal Statement

((( personal_statement )))

---

## Education

### ((( education.degree )))
**((( education.university )))** | ((( education.dates )))

- **Honours:** ((( education.honours )))
- **GPA:** ((( education.gpa )))

---

## Experience

((* for exp in experience *))
### ((( exp.title )))
**((( exp.place )))** | ((( exp.dates )))

((* for bullet in exp.bullets *))
- ((( bullet )))
((* endfor *))

((* endfor *))

---

## Skills

- **Programming Languages:** ((( skills.programming )))
- **Libraries & Tools:** ((( skills.libraries )))
- **Other:** ((( skills.other )))

---

## Projects

((* for proj in projects *))
((* if proj.projectName *))
### ((( proj.projectName )))

((* for bullet in proj.bullets *))
((* if bullet *))
- ((( bullet )))
((* endif *))
((* endfor *))

((* endif *))
((* endfor *))