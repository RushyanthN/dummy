def open_file(corpus):
    with open(corpus, 'r') as file:
        contents = file.readlines()
    return contents



def report_count(token):
    text = open_file('corpus.txt')
    count=0
    for line in text:
        for word in line.split():
            if word == token:
                count+=1
    return print(f"The term {token} shows up in the corpus {count} times.")
    