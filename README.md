# training-repository

Структура репозитория ("болванка"):
training-repository/
├── .github/
│   └── workflows/
│       └── ci.yml                 # CI: запускает тесты на push/PR
├── docs/
│   ├── Makefile
│   ├── api.md                     # страница API (Sphinx autodoc)
│   ├── conf.py                    # конфиг Sphinx (+ путь к src)
│   ├── index.rst                  # оглавление документации
│   └── make.bat
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_evaluation.ipynb
│   ├── 03_reporting.ipynb
│   └── sandbox.ipynb
├── src/
│   ├── mypkg/
│   │   ├── __init__.py
│   │   └── hello.py
│   └── tests/
│       └── test_hello.py          # юнит-тест (сейчас лежит внутри src)
├── .gitignore
├── LICENSE
├── README.md
├── pytest.ini                      # настройки pytest (pythonpath=src, testpaths=…)
└── requirements.txt                # зависимости (pytest и др.)


📦 Установка
Клонируйте репозиторий:

git clone https://github.com/Tatiana-Nes/training-repository.git
cd training-repository

                  
(Рекомендуется) создайте виртуальное окружение:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

                  
Установите зависимости:

pip install -r requirements.txt

                  
🧪 Запуск тестов (если есть)
pytest

                  
📚 Генерация документации (Sphinx)
Перейдите в папку документации:

cd docs

                  
Сгенерируйте HTML-документацию:

make html

                  
Откройте в браузере:

open _build/html/index.html  # Windows: start _build/html/index.html

                  
🚀 Автопубликация документации
Документация автоматически собирается и публикуется на GitHub Pages при каждом коммите в ветку main.

Ссылка на документацию:
👉 https://Tatiana-Nes.github.io/training-repository/

🛠️ Основные команды разработки
Цель	Команда
Установка зависимостей	pip install -r requirements.txt
Запуск тестов	pytest
Сборка документации	cd docs && make html
Локальный просмотр доков	открыть docs/_build/html/index.html
