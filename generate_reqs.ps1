# generate_requirements.ps1
pip install --upgrade pipreqs
python -m pipreqs.pipreqs . --force --encoding=utf8
