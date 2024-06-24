---
title: "Markdown to HTML Converter"
date: "2024-05-26"
summary: "MarkdownをHTMLに変換するWebアプリ"
image: "static/img/md2html.png"
slug: "md2html"
project_url: ""
github_url: "https://github.com/ctake099/MarkdownToHTML"
---

## プロジェクト概要

MarkdownをHTMLに変換するウェブアプリケーションを開発しました。このプロジェクトでは、以下の技術を使用しました:

- **PHP**
- **Bootstrap**
- **Monacoエディタ**
- **Parsedown（PHPライブラリ）**

## アプリの特徴

- MarkdownをリアルタイムでHTMLに変換
- 変換されたHTMLをダウンロード可能
- 美しいデザインとユーザーフレンドリーなインターフェース

## 開発の背景

以前のバックエンドプロジェクトでは、MarkdownファイルをHTMLファイルに変換するプログラムを作成しました。

## 特に頑張った点

### Monacoエディタの統合

ウェブページにMonacoコードエディタを実装し、ユーザーがMarkdownテキストを直感的に入力できるようにしました。以下のスクリプトを使用して、エディタを初期化しました。

```html
<div id="editor-container" style="width:800px;height:600px;border:1px solid grey"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs/loader.min.js"></script>
<script>
    require.config({ paths: { 'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.20.0/min/vs' }});
    require(['vs/editor/editor.main'], function() {
        var editor = monaco.editor.create(document.getElementById('editor-container'), {
            value: '',
            language: 'markdown'
        });
    });
</script>
```

### PHPとParsedownによる変換ロジック

PHPのParsedownライブラリを使用して、MarkdownからHTMLへの変換機能を実装しました。これにより、Markdownテキストを簡単にHTMLに変換できるようにしました。

### ダウンロードと表示ロジックの実装

ユーザーが変換されたHTMLをダウンロードできる機能を実装しました。また、変換されたHTMLをウェブページ上に直接表示するオプションも提供しました。


### デザインとレスポンシブ対応

Bootstrapを使用して、美しく使いやすいインターフェースを実現しました。また、レスポンシブデザインを取り入れることで、さまざまなデバイスでの快適な閲覧を可能にしました。