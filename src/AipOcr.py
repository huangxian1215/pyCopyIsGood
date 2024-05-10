# pip install baidu-aip
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '68217465'
API_KEY = 'evn6TpUm74zI8PugReIDRUVE'
SECRET_KEY = 'WbPZtOkpSxXXAkWLSy4H4QfqsJWOzxAs'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()


# image = get_file_content('./tmp.png')
# url = "https://www.x.com/sample.jpg"
# pdf_file = get_file_content('文件路径')

# 调用通用文字识别（标准版）
# res_image = client.basicGeneral(image)
# res_url = client.basicGeneralUrl(url)
# res_pdf = client.basicGeneralPdf(pdf_file)
# print(res_image)
# print(res_url)
# print(res_pdf)

# 如果有可选参数
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

def pic2txt():
    image = get_file_content('./tmp.png')
    res_image = client.basicGeneral(image, options)
    txt = ''
    if 'words_result' in res_image:
        words_list = res_image['words_result']
        for item in words_list:
            if 'words' in item:
                word = item['words']
                txt+=word
    return txt

# res_url = client.basicGeneralUrl(url, options)
# res_pdf = client.basicGeneralPdf(pdf_file, options)

# print(res_url)
# print(res_pdf)