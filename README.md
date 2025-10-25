# training-repository

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
