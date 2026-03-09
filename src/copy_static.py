import os
import shutil


def copy_static(src, dst):
    # удалить старую public
    if os.path.exists(dst):
        shutil.rmtree(dst)

    # создать новую
    os.mkdir(dst)

    copy_recursive(src, dst)


def copy_recursive(src, dst):
    items = os.listdir(src)

    for item in items:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)

        else:
            print(f"Creating directory: {dst_path}")
            os.mkdir(dst_path)
            copy_recursive(src_path, dst_path)