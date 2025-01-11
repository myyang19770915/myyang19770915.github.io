import os
import glob

# 掃描文章目錄
articles = glob.glob('articles/**/*.html', recursive=True)

# 生成 HTML 連結
links = []
for article in articles:
    filename = os.path.basename(article)
    # 假設使用 GitHub Pages URL
    url = f'https://myyang19770915.github.io/SingleFile-Archives/{filename}'
    links.append(f'<li><a href="{url}">{filename}</a></li>')

# 更新 index.html
with open('website/index.html', 'r') as f:
    content = f.read()

# 在特定標記之間插入連結
start_mark = '<!-- ARTICLE-LINKS-START -->'
end_mark = '<!-- ARTICLE-LINKS-END -->'
new_content = content.split(start_mark)[0] + start_mark + '\n'
new_content += '<ul>\n' + '\n'.join(links) + '\n</ul>\n'
new_content += end_mark + content.split(end_mark)[1]

with open('website/index.html', 'w') as f:
    f.write(new_content)
