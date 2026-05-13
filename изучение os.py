import os
position = os.getcwd()
print()
print(f"Я пишу в этой директории {position}\n")

os.rmdir('archive')
