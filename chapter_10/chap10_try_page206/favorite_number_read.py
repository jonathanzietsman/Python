from pathlib import Path
import json

path = Path(r'C:\01\Knowledge\Web Programming\codeCollage\Python\chapter_10\chap10_try_page206\users_imformation.json')

contents = path.read_text()

user_fav_nmbr = json.loads(contents)

print(f"I know your favorite number! It’s {user_fav_nmbr}")