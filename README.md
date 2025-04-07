# Руководство по внесению изменений

## Обновление версий

Наш проект автоматически обновляет версии на основе меток PR:

* Добавьте метку `feature` к PR для увеличения минорной версии (0.1.0 -> 0.2.0)
* Добавьте метку `hotfix` к PR для увеличения патч-версии (0.1.0 -> 0.1.1)

После слияния PR с одной из этих меток, CI/CD автоматически:
1. Обновит номер версии в файлах version.txt и setup.py
2. Создаст коммит с сообщением формата `[0.2.0] <- [0.1.0] minor up`
3. Добавит к PR метку с новой версией (например, `PR-0.2.0`)