import requests
from urllib.parse  import urlparse
from bs4 import BeautifulSoup
from lxml import html
def check_url_accessibility(url, timeout=5):
    """
    检测URL是否可以正常访问 
    返回：(是否成功, 状态信息)
    """
    try:
        # 自动添加http://前缀（如果缺失）
        if not urlparse(url).scheme:
            url = "http://" + url 
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        }
        
        response = requests.get( 
            url, 
            headers=headers, 
            timeout=timeout, 
            allow_redirects=True 
        )
        
        if response.status_code  < 400:
            return True, response, f"成功访问 (状态码: {response.status_code})" 
        else:
            return False, f"访问失败 (状态码: {response.status_code})" 
            
    except requests.exceptions.RequestException  as e:
        return False, f"连接错误: {str(e)}"

def get_element_by_xpath(url,selector,selector_type = "css"):
    "url= 网址的信息"
    "xpath=网页的xpath信息"
    try :
        is_accessible,result = check_url_accessibility(url,timeout=5)
        if not is_accessible:
            print(f"URL不可访问: {result}")
            return None
        response = result 
        if selector_type.lower()  == 'xpath':
            tree = html.fromstring(response.content) 
            elements = tree.xpath(selector) 
            results = []
            for element in elements :
                if isinstance(element,str):
                    results.append(element)
                else:
                    text = element.text_content_strip() if hasattr(element,'text_content') else str(element)
                    attrs = dict(element.attrib) if hasattr(element,"attrib")   else{}
                    tag = element.tag if hasattr(element,"tag") else None
                    results.append({
                        'text': text,
                        'attrs': attrs,
                        'tag': tag 
                    })
                return results if  results else None
        else :
            soup = BeautifulSoup(response.text,  'html.parser') 
            elements = soup.select(selector) 
            results = []
            for element in elements:
                if element.name: 
                    text = element.get_text('  ', strip=True)
                    attrs = dict(element.attrs) 
                    results.append({ 
                        'text': text,
                        'attrs': attrs,
                        'tag': element.name 
                    })
                else:
                    results.append(str(element)) 
            return results if results else None 
    except requests.RequestException as e:
        print(f'请求错误: {e}')
        return None 
    except Exception as e:
        print(f'错误: {e}')
        return None

    #     if selector_type.lower()  == 'xpath':
    #         # 将XPath转换为CSS选择器(简化版)
    #         css_selector = xpath_to_css(selector)
    #         elements = soup.select(css_selector) 
    #     else :
    #         elements = soup.select(selector)
        
    #     #提取元素
    #     results=[]
    #     for element in elements:
    #         if element.name:
    #             text = element.get_text(' ',strip=True)
    #             attrs = dict(element,attrs)
    #             results.append(
    #                 {
    #                     'text':text,
    #                     'attrs':attrs,
    #                     'tag':element.name

    #                 }
    #             )
    #         else:
    #             results.append(str(element))
    #     return results if results else None
    # except requests.RequestException as e:
    #     print(f'请求错误:{e}')
    #     return None
    # except Exception as e:
    #     print(f'erro:{e}')
    #     return None
# def xpath_to_css(xpath):
#     # 简化版XPath到CSS选择器的转换 
#     # 注意: 仅支持基本XPath表达式，复杂表达式可能需要额外处理
#     xpath = xpath.lstrip('/') # 移除开头的//或/
#       # 简单转换规则 
#     replacements = [
#         ('//', ' '),      # 后代选择器
#         ('/', ' > '),     # 子选择器
#         ('[@', '['),      # 属性选择器
#         (']', ']'),       # 属性选择器结束 
#         ('=', '="'),      # 属性值 
#         ('"', '"'),       # 属性值引号 
#         (' and ', '][')   # 多条件
#     ]
#     for old,new in replacements:
#         xpath = xpath.replace(old,new)  
#         # 处理contains函数 
#     if 'contains(' in xpath:
#         import re
#         # 匹配 contains(@class, 'value') 形式 
#         matches = re.findall(r'contains\((@\w+),\s*[\'"](.*?)[\'"]\)',  xpath)
#         for attr, value in matches:
#             xpath = xpath.replace(f'contains({attr},  \'{value}\')', f'{attr[1:]}*={value}')
#             xpath = xpath.replace(f'contains({attr},  "{value}")', f'{attr[1:]}*={value}')
    
#     return xpath.strip()

# 测试用例 
test_urls = [
    "https://movie.douban.com/",   # 正常网站 
]
xpath = "//div[@class='billboard-bd']//tr/text()"
 
print("="*50)
print("URL可访问性测试")
print("="*50)
 
for url in test_urls:
    is_accessible, message = check_url_accessibility(url)
    
    if is_accessible:
        print(f"✅ [成功] {url}")
        print(f"   → {message}\n")
    else:
        print(f"❌ [失败] {url}")
        print(f"   → {message}\n")
elements = get_element_by_xpath(test_urls[0], xpath, selector_type='xpath')
if elements:
    print("找到的元素:")
    for i, element in enumerate(elements, 1):
        if isinstance(element, dict):
            print(f"{i}. 文本: {element['text']}")
            print(f"   标签: {element['tag']}")
            print(f"   属性: {element['attrs']}")
        else:
            print(f"{i}. {element}")
else:
    print("没有找到匹配的元素")

