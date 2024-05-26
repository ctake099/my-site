import markdown
from jinja2 import Environment, FileSystemLoader
from markdown.extensions.meta import MetaExtension
from markdown.extensions.fenced_code import FencedCodeExtension
import os
import re

# テンプレート環境を設定
env = Environment(loader=FileSystemLoader('templates'))

# HTMLテンプレートを読み込む
template = env.get_template('base.html')

def markdown_to_html(md_file):
    with open(md_file, 'r', encoding='utf-8') as file:
        md = markdown.Markdown(extensions=[MetaExtension(), FencedCodeExtension()])
        html = md.convert(file.read())
        meta = {key: value[0].strip().strip('"') if value else "" for key, value in md.Meta.items()}
        return html, meta

def process_directory(directory):
    items = []
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            path = os.path.join(directory, filename)
            html, meta = markdown_to_html(path)
            slug = meta.get('slug', generate_slug(meta.get('title', '')))
            external_url = meta.get('external_url', "")
            item = {
                'title': meta.get('title', 'No Title'),
                'date': meta.get('date', 'No Date'),
                'summary': meta.get('summary', ''),
                'content': html,
                'slug': slug,
                'external_url': external_url
            }
            if 'image' in meta:  # 画像がメタデータに含まれている場合
                item['image'] = meta['image']
            items.append(item)
    return items

def generate_slug(title):
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower())
    return slug.strip('-')

# プロジェクトとポストを処理
projects = process_directory('content/projects')
posts = process_directory('content/posts')

# 最終的なHTMLをレンダリング
rendered_html = template.render(projects=projects, posts=posts)

# 出力ディレクトリの設定
output_dir = 'docs'
os.makedirs(output_dir, exist_ok=True)

# HTML ファイルとして出力
output_path = os.path.join(output_dir, 'index.html')
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(rendered_html)

def generate_detail_html(item, template_name, output_folder, context_name):
    template = env.get_template(template_name)
    html_content = template.render(**{context_name: item})
    output_path = os.path.join('docs', output_folder, item['slug'] + '.html')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

for post in posts:
    generate_detail_html(post, 'blog_detail.html', 'blog', 'post')

for project in projects:
    generate_detail_html(project, 'project_detail.html', 'projects', 'project')
