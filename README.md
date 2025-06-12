# Software to generate random set of exam papers

Requires an array of questions to be put into `input.json` in this order

```json
[
    "Определение VCS (Version Control System). Основные задачи.",
    "Назовите и охарактеризуйте типы систем управления версиями (LVCS, CVCS, DVCS).",
    "Основные принципы работы Git. Чем он отличается от других VCS?",
    "Перечислите и объясните основные понятия Git (репозиторий, коммит, ветка, удаленный репозиторий, слияние, клонирование, индекс, HEAD)."
]
```

This script outputs `markdown` file with further formatting

```markdown
# Билет 1

№1 Определение VCS (Version Control System). Основные задачи.

№2 Перечислите и объясните основные понятия Git (репозиторий, коммит, ветка, удаленный репозиторий, слияние, клонирование, индекс, HEAD).

# Билет 2

№1 Назовите и охарактеризуйте типы систем управления версиями (LVCS, CVCS, DVCS).

№2 Основные принципы работы Git. Чем он отличается от других VCS?
```

## Logic

Set of gets split into `n` parts according to `num_of_questions` variable. Then exam variants are generated getting one question from each split.