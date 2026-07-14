#!/usr/bin/env python3
"""
清理剩余的示例文件
"""
import os
import glob

def cleanup_remaining():
    """清理剩余的示例文件"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)

    print("=" * 60)
    print("清理剩余的示例文件...")
    print("=" * 60)

    deleted_count = 0

    # 剩余的文件模式
    patterns = [
        "section_giant_*.py",
        "section_huge_*.py",
        "section_massive_*.py",
        "example_large_*.py",
    ]

    for pattern in patterns:
        matches = glob.glob(os.path.join(parent_dir, pattern))
        for filepath in matches:
            try:
                os.remove(filepath)
                deleted_count += 1
                print(f"✓ 删除: {os.path.basename(filepath)}")
            except Exception as e:
                print(f"✗ 失败: {os.path.basename(filepath)} - {e}")

    print("\n" + "=" * 60)
    print(f"清理完成！共删除 {deleted_count} 个文件")
    print("=" * 60)

    # 统计剩余Python文件
    remaining = len(glob.glob(os.path.join(parent_dir, "*.py")))
    print(f"剩余Python文件: {remaining} 个")

    # 显示项目大小
    total_size = sum(os.path.getsize(os.path.join(dirpath, filename))
                    for dirpath, dirnames, filenames in os.walk(parent_dir)
                    for filename in filenames if not filename.endswith('.pyc'))
    print(f"项目大小: {total_size / (1024*1024):.1f} MB")

if __name__ == "__main__":
    cleanup_remaining()
