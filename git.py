# Commit 1: Initial Commit - Add Base Code
git add solver.py
git commit -m "Initial commit: Add math problem solver script"

# Commit 2: Add a .gitignore File
echo "*.pyc\n__pycache__/\n.env" > .gitignore
git add .gitignore
git commit -m "Add .gitignore file"

# Commit 3: Improve User Input Handling (strip spaces)
git add solver.py
git commit -m "Improve input handling by stripping spaces"

# Commit 4: Add More Math Functions (exp and degrees)
git add solver.py
git commit -m "Add exp and degrees functions"

# Commit 5: Implement Logging
echo 'import logging' >> solver.py
echo 'logging.basicConfig(level=logging.INFO)' >> solver.py
git add solver.py
git commit -m "Add logging support"

# Commit 6: Add Exception Handling Improvements
git add solver.py
git commit -m "Improve exception handling with better error messages"

# Commit 7: Enhance User Interaction (Better Prompts)
git add solver.py
git commit -m "Enhance user prompts and instructions"

# Commit 8: Add a Requirements File
echo "math" > requirements.txt
git add requirements.txt
git commit -m "Add requirements.txt for dependencies"

# Commit 9: Refactor Code for Better Readability
git add solver.py
git commit -m "Refactor code to improve readability"

# Commit 10: Add a README File
echo "# Math Solver" > README.md
echo "A simple Python math expression solver." >> README.md
git add README.md
git commit -m "Add README file"
