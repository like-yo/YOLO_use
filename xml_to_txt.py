import xml.etree.ElementTree as ET
import os

def get_image_size_from_xml(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    size_elem = root.find('size')
    width = int(size_elem.find('width').text)
    height = int(size_elem.find('height').text)

    return width, height

def convert_xml_to_yolo(xml_path, image_width, image_height, classes):
    actual_width, actual_height = get_image_size_from_xml(xml_path)

    tree = ET.parse(xml_path)
    root = tree.getroot()

    yolo_lines = []

    for obj in root.findall('object'):
        class_name = obj.find('name').text
        if class_name not in classes:
            continue

        class_id = classes.index(class_name)

        xmin = float(obj.find('bndbox/xmin').text)
        ymin = float(obj.find('bndbox/ymin').text)
        xmax = float(obj.find('bndbox/xmax').text)
        ymax = float(obj.find('bndbox/ymax').text)

        x_center = (xmin + xmax) / (2.0 * actual_width)
        y_center = (ymin + ymax) / (2.0 * actual_height)
        width = (xmax - xmin) / actual_width
        height = (ymax - ymin) / actual_height

        yolo_line = f"{class_id} {x_center} {y_center} {width} {height}"
        yolo_lines.append(yolo_line)

    return yolo_lines

def process_all_xml_files(xml_folder, output_folder, classes):
    os.makedirs(output_folder, exist_ok=True)

    for xml_filename in os.listdir(xml_folder):
        if xml_filename.endswith('.xml'):
            xml_path = os.path.join(xml_folder, xml_filename)
            width, height = get_image_size_from_xml(xml_path)
            yolo_lines = convert_xml_to_yolo(xml_path, width, height, classes)

            # 保存到输出文件夹
            output_path = os.path.join(output_folder, f"{os.path.splitext(xml_filename)[0]}.txt")
            with open(output_path, 'w') as output_file:
                output_file.write('\n'.join(yolo_lines))

# 示例用法
xml_folder = r'D:\Python\date_pre_solve\yolo_dataset\telegraph_pole\Annotations' 
output_folder = r'D:\Python\date_pre_solve\yolo_dataset\telegraph_pole\labels'  # 替换成你的输出文件夹路径
classes = ['nest', 'balloon', 'kite','trash']
process_all_xml_files(xml_folder, output_folder, classes)



