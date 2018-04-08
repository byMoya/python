import re
import os
import urllib
from urllib import request
from bs4 import BeautifulSoup

# 建议下载，根据页数
suggest_download_page = 20
# local_dir_path_prefix = 'd:' + os.sep + 'tv'
# local_dir_path_prefix = 'd:' + os.sep + 'neihan'
local_dir_path_prefix = 'd:' + os.sep + 'xiee'
# local_dir_path_prefix = 'd:' + os.sep + 'neihan_page_50_70'
# book_folder = '001'
web_url = 'http://m.hldm123.cc/shaonvmanhua/48201.html'
# 少女漫画
# series_url = 'http://m.hldm99.com/shaonvmanhua/'
# 内涵漫画
# series_url = 'http://m.hldm99.com/nahanmanhua/'
# 邪恶漫画
series_url = 'http://m.hldm123.cc/xieemanhua/'


# 获取soup
def get_soup(url):
    html = request.urlopen(url).read()
    return BeautifulSoup(html, "html.parser")


# 获取下载图片路径
def get_picture_url_from_div(soup, attrs_name, attrs_value):
    div_content = soup.find_all(attrs={attrs_name: attrs_value})
    if div_content[0]:
        return div_content[0].img.get('src')
    else:
        print('this page has not picture')


# 获取书页数
def get_picture_total_page(soup, attrs_name, attrs_value):
    page_ul = soup.find_all(attrs={attrs_name: attrs_value})

    if len(page_ul) == 0:
        return 0

    try:
        total_page_str = page_ul[0].a.string
        return re.sub("\D", "", total_page_str)
    except Exception as e:
        print(str(e))
        return 0


# 是否建议下载(根据页数)
def is_suggest_to_down(total_page):
    # if 50 < total_page < 71:
    if total_page > suggest_download_page:
        return True
    else:
        print('页数不足' + str(suggest_download_page) + '页, 不建议下载')
        # print('页数不足' + '50页, 不建议下载')
        return False


# 下载图片到指定路径
def download_picture_from_url_to_path(image_url, file_path, picture_name):
    try:
        if not os.path.exists(file_path):
            print('文件夹不存在,新建文件夹')
            os.makedirs(file_path)

        # 获取图片后缀
        file_suffix = os.path.splitext(image_url)[1]
        file_name = '{}{}{}{}'.format(file_path, os.sep, picture_name, file_suffix)
        if os.path.exists(file_name):
            print(file_name + '图片已下载')
            return
        urllib.request.urlretrieve(image_url, filename=file_name)
    except IOError as e:
        print('文件操作失败' + e)
    except Exception as e:
        print('错误' + str(e))


# 补全页码
def get_page_serial(supply_num):
    if supply_num < 10:
        return '00' + str(supply_num)
    elif supply_num < 100:
        return '0' + str(supply_num)
    else:
        return str(supply_num)


# 下载一本书
def down_tv_sample_book(book_url):
    soup = get_soup(book_url)
    print(book_url)
    total_page = int(get_picture_total_page(soup, 'class', 'Pages font_size_small'))

    if not total_page or total_page == 0:
        print('没有页数的书,直接返回')
        return

    if not is_suggest_to_down(total_page):
        return

    local_file_path = local_dir_path_prefix + os.sep + str(book_url[book_url.rfind('/') + 1: len(book_url) - 5])

    if os.path.exists(local_file_path) and len(os.listdir(local_file_path)) == total_page:
        print('此书已下载')
        return

    for i in range(1, total_page + 1):
        try:
            if i == 1:
                html_url = book_url
            else:
                html_url = book_url[0:len(book_url) - 5] + '_' + str(i) + '.html'
            soup = get_soup(html_url)
            img_url = get_picture_url_from_div(soup, 'class', 'ArticleBox')
            download_picture_from_url_to_path(img_url, local_file_path, get_page_serial(i))
        except Exception as e:
            print(e)


# 系列丛书-------------------------------------------------------------------------------------
# 获取系列书页数
def get_series_book_total_page(first_page_url):
    soup = get_soup(first_page_url)
    page_ul = soup.find_all(attrs={'class': 'pagelist'})
    page_as = page_ul[0].find_all('a')
    pages_a = page_as[len(page_as) - 1].get('href')
    return pages_a[1:len(pages_a) - 5]


# 获取系列单页的书链接
def get_page_books_url_list(book_list_url):
    soup = get_soup(book_list_url)
    book_li = soup.find_all(attrs={'class': 'libox'})

    books_url = []

    for li in book_li:
        book_url = li.a.get('href')
        books_url.append(book_url)

    return books_url
    # print(books_url)


# 获取整个系列的全部书url
def get_all_series_book_urls(first_url):
    series_pages = int(get_series_book_total_page(first_url))
    series_all_book_url_list = []

    for i in range(1, series_pages + 1):
        if i == 1:
            series_all_book_url_list.extend(get_page_books_url_list(first_url))
        else:
            series_all_book_url_list.extend(get_page_books_url_list(first_url + "h" + str(i) + '.html'))

    return series_all_book_url_list


# 下载整个系列符合条件的书
def download_all_series_book(series_first_url):
    all_book_url_list = get_all_series_book_urls(series_first_url)
    for book_url in all_book_url_list:
        down_tv_sample_book(book_url)


download_all_series_book(series_url)

# get_page_books_url_list(series_url)
# get_all_series_book_urls(series_url)


# 测试网址
# down_tv_sample_book(web_url)


# get_picture_url_from_div(soup, 'class', 'ArticleBox')
# print(get_picture_url_from_div(soup, 'class', 'ArticleBox'))
# get_picture_total_page(soup, 'class', 'Pages font_size_small')

# print(soup)

# local_file_path = local_dir_path_prefix + os.sep + '001'
# img_url = 'http://www.baidu.com/img/bd_logo1.png'
# download_picture_from_url_to_path(img_url, local_file_path, '001')
# print(len('http://www.aliyun.html'))