import os
import re
import requests
from urllib.parse import urlparse
import hashlib

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', printEnd="\r"):
    """显示命令行进度条"""
    if total == 0:
        return
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    if iteration == total: 
        print()

def get_filename_from_url(img_url):
    """从URL中提取或生成唯一文件名"""
    parsed_url = urlparse(img_url)
    filename = os.path.basename(parsed_url.path)
    if not filename or not re.search(r'\.(jpg|jpeg|png|gif|webp|bmp|svg)$', filename, re.IGNORECASE):
        ext = '.jpg'
        hash_name = hashlib.md5(img_url.encode('utf-8')).hexdigest()
        filename = f"{hash_name}{ext}"
    return filename

def download_and_replace_images():
    base_dir = os.getcwd()
    images_dir = os.path.join(base_dir, 'images')
    
    img_pattern = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]+)\)')
    
    file_matches = {}  # 记录每个文件对应的匹配项 {filepath: {'content': str, 'matches': set}}
    unique_urls = set() # 记录去重后的所有URL

    print("正在扫描当前目录及子目录下的 Markdown 文件...")
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if not file.endswith('.md'):
                continue
                
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"[警告] 读取文件失败 {filepath}: {e}")
                continue
                
            matches = img_pattern.findall(content)
            if matches:
                unique_file_matches = set(matches)
                file_matches[filepath] = {
                    'content': content,
                    'matches': unique_file_matches
                }
                for alt, url in unique_file_matches:
                    unique_urls.add(url)
                    
    if not file_matches:
        print("未发现包含网络图片的 Markdown 文件。")
        return

    # 1. 打印预览信息
    print("\n" + "="*40)
    print(" 📊 解析与下载预览")
    print("="*40)
    print(f"📁 下载目标文件夹: {images_dir}")
    print("\n📄 涉及的 Markdown 文件及图片数量:")
    for fp, data in file_matches.items():
        rel_fp = os.path.relpath(fp, base_dir)
        print(f"  - {rel_fp}: {len(data['matches'])} 张图片")
    print(f"\n🌐 总计需要下载的不重复图片数量: {len(unique_urls)} 张")
    
    # 命令行交互确认
    confirm = input("\n确认并开始下载/替换？(y/n) [默认: y]: ").strip().lower()
    if confirm not in ('y', 'yes', ''):
        print("已取消操作。")
        return

    # 创建目标文件夹
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # 2. 下载图片并显示进度条
    print("\n" + "="*40)
    print(" ⬇️ 开始下载图片")
    print("="*40)

    url_to_filename = {}
    successful_urls = set()  # 记录成功下载或已存在的URL
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    total_imgs = len(unique_urls)
    for i, img_url in enumerate(unique_urls, 1):
        filename = get_filename_from_url(img_url)
        save_path = os.path.join(images_dir, filename)
        url_to_filename[img_url] = filename
        
        # 刷新进度条
        print_progress_bar(i-1, total_imgs, prefix='下载进度:', suffix=f'处理中...       ', length=30)
        
        if not os.path.exists(save_path):
            # 增加重试机制，最多重试3次
            for attempt in range(3):
                try:
                    response = requests.get(img_url, headers=headers, timeout=15)
                    response.raise_for_status()
                    with open(save_path, 'wb') as img_f:
                        img_f.write(response.content)
                    successful_urls.add(img_url)
                    break  # 下载成功，跳出重试循环
                except Exception as e:
                    if attempt == 2:  # 最后一次重试失败
                        print(f"\n[下载失败] {img_url} -> {e}")
            
        else:
            successful_urls.add(img_url)
        
        # 再次更新进度条到当前完成状态
        print_progress_bar(i, total_imgs, prefix='下载进度:', suffix=f'完成 ({i}/{total_imgs})', length=30)

    # 3. 替换 Markdown 内的链接
    print("\n" + "="*40)
    print(" 🔄 开始更新 Markdown 链接")
    print("="*40)
    
    updated_files = 0
    for fp, data in file_matches.items():
        content = data['content']
        matches = data['matches']
        new_content = content
        modified = False
        
        root = os.path.dirname(fp)
        rel_images_dir = os.path.relpath(images_dir, root)
        
        for alt_text, img_url in matches:
            # 只有成功下载的图片才进行链接替换
            if img_url not in successful_urls:
                continue
                
            filename = url_to_filename.get(img_url)
            rel_img_path = os.path.join(rel_images_dir, filename).replace('\\', '/')
            
            old_str = f"![{alt_text}]({img_url})"
            new_str = f"![{alt_text}]({rel_img_path})"
            
            if old_str in new_content:
                new_content = new_content.replace(old_str, new_str)
                modified = True
                
        if modified:
            try:
                with open(fp, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ 更新成功: {os.path.relpath(fp, base_dir)}")
                updated_files += 1
            except Exception as e:
                print(f"❌ 更新失败: {os.path.relpath(fp, base_dir)} - {e}")
                
    print(f"\n🎉 恭喜！处理完毕！共更新了 {updated_files} 个文件。")

if __name__ == '__main__':
    download_and_replace_images()