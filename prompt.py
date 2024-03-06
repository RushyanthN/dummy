def open_file(corpus):
    with open(corpus, 'r') as file:
        contents = file.read_lines()
    return contents



def report_count(token):
    text = open_file('coupus.txt')
    count=0
    for line in text:
        for word in line.split():
            if word == token:
                count+=1
    return count
