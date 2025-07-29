# print ("hello word")
# print("111")
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
# def is_url_access(url,timeout=5):
#     " 检测url是否可以正常的访问 "
#     try:
#         if not urlparse(url).scheme:
#             url = "http://" + url
#         response = requests.get(url,  timeout=timeout, allow_redirects=True)
#         if response.status_code  < 400:
#             return True, f"Success (Status {response.status_code})" 
#         else:
#             return False, f"Failed (Status {response.status_code})" 
#     except requests.exceptions.RequestException  as e:
#         return False, f"Error: {str(e)}"
# """获取URL内容并用BeautifulSoup解析:param url: 要获取的URL:param timeout: 超时时间(秒):return: (是否成功, BeautifulSoup对象/错误信息)"""
# def fetch_and_parse(url, timeout=5):
#     accessible, msg = is_url_access(url, timeout)
#     if not accessible :
#         return False, msg 
#     try :
#         response = requests.get(url,timeout=timeout)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text , 'html.parser')
#     except requests.exceptions.RequestException as e:
#         return False , f"request erro: {str(e)}"
#     except Exception as e:
#         return False, f"request erro : {str(e)}"

#         return
# if __name__ == "__main__":
#     test_urls = [
#         "https://www.baidu.com", 
#         "www.douban.com"
#     ]
    
#     print("URL访问性测试:")
#     for url in test_urls:
#         result, detail = is_url_access(url)
#         status = "可访问" if result else "不可访问"
#         print(f"{url}: {status} - {detail}")
    
#     print("\n网页内容获取测试:")
#     demo_url = "https://www.baidu.com" 
#     success, content = fetch_and_parse(demo_url)
#     if success:
#         print(f"成功获取 {demo_url} 的内容")
#         print(f"网页标题: {content.title.string}") 
#     else:
#         print(f"获取失败: {content}")
url = "https://movie.douban.com/"
# 构造请求头和代理信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}
web = requests.get(url,headers=headers)
print('end', type(web))
print('code=',web.status_code)