import json
file = open("out.json", "r").readlines()
with open("input.txt", "a") as outf:
    for line in file:
        try:
            urls = json.loads(line)["entities"]["urls"]
            hashtags = json.loads(line)["entities"]["hashtags"]         
            for url in urls:
                print(url)
                outf.write(f"{url['expanded_url']}\n")
            print(hashtags)
            for ht in hashtags:
               outf.write(f"{ht['text']}\n")
        except Exception as e:
            print(e)
            
