#API尝试 https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000
import requests
url = 'https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000'
headers = {"Accept": "application/vnd.github.v3+json"} #这个是github的API规定的请求头，用于告诉API我们希望接收JSON格式的响应

r = requests.get(url,headers=headers)
print(f"Status code:{r.status_code}")    #用requests调用API,打印状态码

#响应转换为字典
response_dict = r.json()
print(f"Total repositories:{response_dict['total_count']}")
print(f"Complete reseults:{not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']     #和items关联的是一个列表，其中包含了很多字典
print(f"Repositories returned:{len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\nKeys:{len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
#处理结果
print(response_dict.keys())