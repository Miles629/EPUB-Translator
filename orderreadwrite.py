import os
import zipfile
import shutil
from bs4 import BeautifulSoup
from DeepSeek import translate
def unzip_epub(epub_path, temp_dir):
    with zipfile.ZipFile(epub_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

def get_chapter_order(opf_path):
    with open(opf_path, 'r', encoding='utf-8') as f:
        opf_content = f.read()
    soup = BeautifulSoup(opf_content, 'xml')  # 使用 'xml' 解析器
    spine = soup.find('spine')
    itemrefs = spine.find_all('itemref')
    chapter_order = [itemref.get('idref') for itemref in itemrefs]
    return chapter_order

def get_chapter_paths(manifest, chapter_order, temp_dir):
    temp_dir = os.path.join(temp_dir, 'OEBPS')
    paths = {}
    for item in manifest.find_all('item'):
        id = item.get('id')
        href = item.get('href')
        if id in chapter_order:
            paths[id] = os.path.join(temp_dir, href)
    return paths

def writefile(new_content,file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)            
def translator(soup,giventexts,lang):
    Done=True
    results = translate(giventexts,lang)
    new_soup=str(soup)
    new_soup.find('/p>')
    # 使用字符串的split方法分割字符串，并在每个段落后面追加一个句子
    parts = new_soup.split("</p>")
    # print(results)
    sentences = results.splitlines()
    new_html_str = ""
    if len(parts) != len(sentences)+1 and len(parts) != 1:
        print("两个列表的长度{}不同{}，正在重试。".format(len(parts),len(sentences)))
        Done=False
    for i in range(len(parts)):
        # 如果是最后一个</p>，则不加句子
        if i < len(parts) - 1 and i < len(sentences):
            new_html_str += parts[i] + "</p><p>" + sentences[i] + "</p>"
        else:
            new_html_str += parts[i]
    return Done,new_html_str
def trans_chapters_in_order(chapter_paths,lang,write=False):
    backtexts=""
    for chapter_id, path in chapter_paths.items():
        if os.path.exists(path):  # 确保文件路径存在
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            print(f"Processing Chapter {chapter_id}:",soup.title.string)
            # if chapter_id== 'x_book1.html':
                # print(soup)
                # paragraphs = soup.find_all('p')
                # for i, p in enumerate(paragraphs, start=1):
                #     text = p.get_text()
                #     backtexts += text+"\n"
                # done=False
                # timemax=3
                # i=0
                # while not done and i< timemax:
                #     done,results = translator(soup,backtexts,lang)
                #     i+=1
                # if write:
                #     writefile(results,path)
            paragraphs = soup.find_all('p')
            for i, p in enumerate(paragraphs, start=1):
                text = p.get_text()
                backtexts += text+"\n"
            done=False
            timemax=3
            i=0
            while not done and i< timemax:
                done,results = translator(soup,backtexts,lang)
                i+=1
            if write:
                writefile(results,path)    
            print("\n---\n")
        else:
            print(f"File not found: {path}")
def read_chapters_in_order(chapter_paths):
    backtexts=""
    for chapter_id, path in chapter_paths.items():
        if os.path.exists(path):  # 确保文件路径存在
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            print(f"Processing Chapter {chapter_id}:",soup.title.string)
            if chapter_id== 'x_book1.html':
                print(soup)
                paragraphs = soup.find_all('p')
                for i, p in enumerate(paragraphs, start=1):
                    text = p.get_text()
                    backtexts += text+"\n"
                print(backtexts)
                exit()
            # print(soup.get_text())
            print("\n---\n")
        else:
            print(f"File not found: {path}")

def create_epub(folder_path, output_path):
    # 确保输出路径的文件名以.epub结尾
    if not output_path.endswith('.epub'):
        output_path += '.epub'

    # 创建一个新的ZIP文件
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as new_zip:
        # 遍历文件夹中的所有文件和子文件夹
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                # 构建文件的完整路径
                file_path = os.path.join(foldername, filename)
                # 将文件添加到ZIP文件中
                new_zip.write(file_path, arcname=os.path.relpath(file_path, folder_path))
    print(f'EPUB文件已成功创建在: {output_path}')

def main(epub_path = '/root/Tools/epub-Translator/棉花帝国.epub',
    temp_dir = 'temp_unzip',
    output_path = '棉花帝国2.epub', 
    write = True):
    
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    unzip_epub(epub_path, temp_dir)

    opf_path = os.path.join(temp_dir, 'OEBPS', 'content.opf')
    chapter_order = get_chapter_order(opf_path)
    
    with open(opf_path, 'r', encoding='utf-8') as f:
        opf_content = f.read()
    soup = BeautifulSoup(opf_content, 'xml')
    manifest = soup.find('manifest')

    chapter_paths = get_chapter_paths(manifest, chapter_order, temp_dir)

    trans_chapters_in_order(chapter_paths,"English",write)

    if write==True:
        # zip_epub(temp_dir, output_path)
        create_epub(temp_dir, output_path)
    
    # read_chapters_in_order(chapter_paths)

    # 清理临时文件夹
    shutil.rmtree(temp_dir)

if __name__ == '__main__':
    main()
