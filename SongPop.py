import json
import sys

"""
    Usage:
        python SongPop.py (and put the json in console)
        
        or
        
        python SongPop.py -f (read the json from file "input.json")
"""

def main(args=[]):
    try:
        if(len(args) > 1 and args[1] == "-f"):
            arq = open("input.json")
            js = json.loads(arq.read())
        else:
            js = json.loads(input("Json: "))
    except:
        print("Erro ao ler json.")
        exit(0)

    try:
        questions = js["quiz"]["questions"]
    except:
        questions = js["quizDatas"]["questions"]

    q = 1
    for question in questions:
        index = question["answerIndex"]
        songs = question["songs"]
        type = question["type"]

        s = 0
        for song in songs:
            if(s == index):
                print("==============")
                print("QUEST", q)

                artist = song["artist"]
                title = song["title"]

                if(type == "Artist"):
                    print(artist.upper())
                else:
                    print(title.upper())
            s += 1

        q += 1

if __name__ == "__main__":
    main(sys.argv)