import os

ROOT = os.path.join(os.path.dirname(__file__), 'source')

def generate_toctree(directory):
    # 获取目录中所有 .rst 文件
    files = [f for f in os.listdir(directory) if f.endswith('.md')]
    # 按文件名逆序排序
    files.sort(reverse=True)
    print(".. toctree::")
    print("   :maxdepth: 1")
    print("   :caption: 目录\n")
    for file in files:
        # 去掉文件扩展名
        print(f"   {os.path.splitext(file)[0]}")

if __name__ == '__main__':
    generate_toctree(ROOT)
