import glob
import os

def verify_tags(string_tags: str) -> str:
    available_tags = ['jumps','streams','consistency','tv-size','alt','tech','sliders','precision','flow','speed','stamina',
                      'fingercontrol','burst','linear','aspire','complex-rhythm']
    tags = string_tags.split()
    for tag in tags:
        if tag in available_tags:
            continue
        else:
            print("The tag '"+tag+"' is not valid. Please re-enter your set of tags")
            return verify_tags(input())
    return string_tags

def clean_tagged_data(file_names: list) -> None:
    with open("beatmaps/tagged_data.txt", "r") as f:
        lines = f.readlines()
    with open("beatmaps/tagged_data.txt", "w") as f:
        for file_name in file_names:
            for line in lines:
                if file_name in line:
                    print(file_name,line)
                    f.write(line)

def main():
    file_names = [os.path.basename(x) for x in glob.glob("beatmaps/*.osu")]
    clean_tagged_data(file_names)
    with open('beatmaps/tagged_data.txt','r+') as tagged_data:
        content = tagged_data.read()
        for file_name in file_names:
            if file_name not in content:
                print(file_name+" is not tagged. Please enter tags for the beatmap.")
                tags = verify_tags(input())
                tagged_data.write(file_name+" "+tags+"\n")
                
if __name__ == "__main__":
    main()
            
