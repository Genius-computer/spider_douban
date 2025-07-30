import requests
from urllib.parse  import urlparse
 
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
            return True, f"成功访问 (状态码: {response.status_code})" 
        else:
            return False, f"访问失败 (状态码: {response.status_code})" 
            
    except requests.exceptions.RequestException  as e:
        return False, f"连接错误: {str(e)}"
 
# 测试用例 
test_urls = [
    "https://movie.douban.com/",   # 正常网站 
]
 
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