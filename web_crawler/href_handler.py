import os
import bs4 as bs

def fetch_url(file):
    with open(file, "r") as f:
        li = set()
        line = f.readline()
        while line:
            if "thumb-link" in line:
                li.add(line)
            line = f.readline()
    return li

def parse_url_href(li):
    tmp = []
    for url in li:
        url = url.split("href=")[1]
        url = url.split(" ")[0]
        url = url.strip("\"")
        tmp.append(url)
    return tmp
        
def parse_url_title(li):
    tmp = []
    for url in li:
        url = url.split("title=")[1]
        # url = url.split(" ")[0]
        url = url.strip("\"")
        url = url[:-3]
        tmp.append(url)
    return tmp

def main():
    file = "gnc.html"
    li = fetch_url(file)
    save_file = "all_url.txt"
    href_li = parse_url_href(li)
    title_li = parse_url_title(li)
    
    with open(save_file, "w") as f:
        for i in range(len(href_li)):
            f.write(href_li[i] + " " + title_li[i] + "\n")

if __name__ == '__main__':
    main()