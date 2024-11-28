# import requests
# from lxml import etree
#
# TARGET_URL = 'https://code.nhsa.gov.cn/jbzd/public/toStdIcdDetail.html'
#
#
# def get_html(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
#     }
#     url_response = requests.post(url, headers=headers).text
#     print(url_response)
#     return url_response
#
#
# def parse_html(url_response):
#     return etree.HTML(url_response)
#
#
# def get_data(html):
#     all_data = html.xpath('//section[@class="content"]/div/div[@id="classicont"]/div[@class="els-doc-h4"]')
#     print(all_data)
#
#
# if __name__ == '__main__':
#     response = get_html(TARGET_URL)
#     html = parse_html(response)
#     get_data(html)
with open('./data/chapter1.txt', 'r+', encoding='utf-8') as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip('\n'), lines))[3:]
    code_to_name = {}
    for i in lines:
        try:
            code, name = [element for element in i.split('\t')[0].split(' ') if element]
        except ValueError:
            pass
        code_to_name[code] = name
print(code_to_name)
