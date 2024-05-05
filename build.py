import markdown
from jinja2 import Environment, FileSystemLoader
from markdown.extensions.meta import MetaExtension
import os

# テンプレート環境を設定
env = Environment(loader=FileSystemLoader('templates'))

# HTMLテンプレートを読み込む
template = env.get_template('base.html')

def markdown_to_html(md_file):
    with open(md_file, 'r', encoding='utf-8') as file:
        md = markdown.Markdown(extensions=[MetaExtension()])
        html = md.convert(file.read())
        meta = {key: value[0].strip().strip('"') if value else "" for key, value in md.Meta.items()}
        return html, meta

def process_directory(directory):
    items = []
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            path = os.path.join(directory, filename)
            html, meta = markdown_to_html(path)
            item = {
                'title': meta.get('title', 'No Title'),
                'date': meta.get('date', 'No Date'),
                'summary': meta.get('summary', ''),
                'content': html
            }
            if 'image' in meta:  # 画像がメタデータに含まれている場合
                item['image'] = meta['image']
            items.append(item)
    return items

from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader('templates'))

def render_projects(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            html_content, meta = markdown_to_html(os.path.join(directory, filename))
            template = env.get_template('project.html')
            rendered_html = template.render(project=meta)
            output_path = os.path.join('output', filename.replace('.md', '.html'))
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(rendered_html)

render_projects('content/projects')


# プロジェクトとポストを処理
projects = process_directory('content/projects')
posts = process_directory('content/posts')

# 最終的なHTMLをレンダリング
rendered_html = template.render(projects=projects, posts=posts)

# 出力ディレクトリの設定
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# HTML ファイルとして出力
output_path = os.path.join(output_dir, 'index.html')
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(rendered_html)

