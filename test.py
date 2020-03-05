import requests
import json
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/63.0.3239.132 Safari/537.36'}
print("电影类型：热门 经典 可播放 豆瓣高分 冷门佳片 华语 欧美 韩国 日本 动作 喜剧 爱情 科幻 悬疑 恐怖 动画")
print("排序方式：time recommend rank")
word = input('请输入想看的电影类型: ')
sort = input('请输入排序方式: ')
start_url = "https://movie.douban.com/j/search_subjects?type=movie&tag="+word+"&sort=" \
            ""+sort+"&page_limit=20&page_start={}"
with open('douban.csv', 'a') as f:
    f.write('{}, {}, {}, {}\n'.format("电影名", "评分", "定位标识符", "图片链接"))
    for i in range(10):
        url = start_url.format(i*20)
        r = requests.get(url, headers=headers)
        ret = r.content.decode()
        result = json.loads(ret)
        res = result['subjects']
        for i in res:
            title = (i['title'])
            rate = (i['rate'])
            url = (i['url'])
            cover = (i['cover'])
            f.write('{}, {}, {}, {}\n'.format(title, rate, url, cover))
