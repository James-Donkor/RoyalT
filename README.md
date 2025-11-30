#FOR CODESPACES
# 1. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py migrate

# 4. Start the development server
python manage.py runserver 0.0.0.0:8000











# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/royalT.git
cd mixinbox

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables
cp .env.example .env

# 5. Run migrations
python manage.py migrate

# 6. Start the development server
python manage.py runserver
