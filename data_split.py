import os
import random
import shutil

# 定义数据集路径
# image_folder = r'D:\Python\date_pre_solve\RSDDs\data_rail\split_data\try_img'  # 图像文件夹路径
# label_folder = r'D:\Python\date_pre_solve\RSDDs\data_rail\split_data\transted_txt_from_xml'  # 标签文件夹路径

# # 定义划分后的数据集保存路径
# train_folder = r'D:\Python\date_pre_solve\RSDDs\data_rail\split_data\data\train'  # 训练集保存路径
# val_folder = r'D:\Python\date_pre_solve\RSDDs\data_rail\split_data\data\valid'  # 验证集保存路径

import os
from sklearn.model_selection import train_test_split
from shutil import copyfile

def create_subfolders(base_folder, subfolders):
    for subfolder in subfolders:
        os.makedirs(os.path.join(base_folder, subfolder), exist_ok=True)

def move_files_to_subfolders(file_paths, subfolders, base_folder):
    for file_path in file_paths:
        # 确保文件存在
        if not os.path.exists(file_path):
            # print(f"Source file does not exist: {file_path}")
            continue

        for subfolder in subfolders:
            dest_folder = os.path.join(base_folder, subfolder)
            os.makedirs(dest_folder, exist_ok=True)  # 确保目标文件夹存在
            dest_path = os.path.join(dest_folder, os.path.basename(file_path))
            # print(f"Moving {file_path} to {dest_path}")
            
            # 打印一下目标路径
            # print(f"Destination path: {dest_path}")
            
            # 确保目标文件夹存在
            os.makedirs(dest_folder, exist_ok=True)
            
            copyfile(file_path, dest_path)

def split_dataset(images_folder, labels_folder, output_folder, test_size, valid_size, random_state=None):
    # 列出images文件夹中的文件
    image_list = os.listdir(images_folder)
    # 构建对应的labels,images文件夹中的文件路径
    label_files = [os.path.join(labels_folder, i.replace(".jpg", ".txt")) for i in image_list]
    image_files = [os.path.join(images_folder, i) for i in image_list]

    # 将数据划分成训练集和测试集
    train_images, test_images, train_labels, test_labels = train_test_split(
        image_files, label_files, test_size=test_size, random_state=random_state
    )

    # 将剩余的数据划分成训练集和验证集
    train_images, valid_images, train_labels, valid_labels = train_test_split(
        train_images, train_labels, test_size=valid_size/(1-test_size), random_state=random_state
    )
    print("训练集图像数量:", len(train_images))
    print("训练集标签数量:", len(train_labels))

    print("验证集图像数量:", len(valid_images))
    print("验证集标签数量:", len(valid_labels))

    print("测试集图像数量:", len(test_images))
    print("测试集标签数量:", len(test_labels))

    # 创建输出文件夹结构
    create_subfolders(output_folder, ["train", "val", "test"])
    create_subfolders(os.path.join(output_folder, "train"), ["images", "labels"])
    create_subfolders(os.path.join(output_folder, "val"), ["images", "labels"])
    create_subfolders(os.path.join(output_folder, "test"), ["images", "labels"])

    # 将图像和标签文件移动到相应的子文件夹中
    move_files_to_subfolders(train_images, ["images"], os.path.join(output_folder, "train"))
    move_files_to_subfolders(train_labels, ["labels"], os.path.join(output_folder, "train"))

    move_files_to_subfolders(valid_images, ["images"], os.path.join(output_folder, "val"))
    move_files_to_subfolders(valid_labels, ["labels"], os.path.join(output_folder, "val"))

    move_files_to_subfolders(test_images, ["images"], os.path.join(output_folder, "test"))
    move_files_to_subfolders(test_labels, ["labels"], os.path.join(output_folder, "test"))

# 示例用法
images_folder = r'D:\Python\date_pre_solve\yolo_dataset\telegraph_pole\images'  # 替换成包含图像文件的文件夹路径
labels_folder = r'D:\Python\date_pre_solve\yolo_dataset\telegraph_pole\labels'  # 替换成包含标签文件的文件夹路径

os.makedirs(os.path.join(r'D:\Python\date_pre_solve\yolo_dataset\telegraph_pole\data_telegraph'), exist_ok=True)
output_folder = r'D:\Python\date_pre_solve\yolo_dataset\telegraph_pole\data_telegraph'  # 替换成你的输出文件夹路径

# 按 1:1:8 的比例划分数据集
split_dataset(images_folder, labels_folder, output_folder, test_size=0.1, valid_size=0.1, random_state=42)
