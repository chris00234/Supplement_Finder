import requests
import bs4 as bs

def get_html(url):
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    return soup


def main():
    url = 'https://www.gnc.com/multivitamins-for-men/201412.html#q=multivitamin&start=1'
    html = get_html(url)
    file = "gnc.html"
    with open(file, "w") as f:
        f.write(html.prettify())
    # print(html)

if __name__ == '__main__':
    main()