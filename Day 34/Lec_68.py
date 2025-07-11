import os
# os.rename("Day 34/Clutter_Folder/file.txt","Day 34/Clutter_Folder/MyFile.txt")
files = os.listdir("Day 34/Clutter_Folder")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"Day 34/Clutter_Folder/{file}",f"Day 34/Clutter_Folder/{i}.png")
        i=i+1