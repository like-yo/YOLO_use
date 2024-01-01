# YOLO_use
yolov5,v8使用细节

1.首先导入YOLO的包。
有两种方式：1.安装到python环境中。直接在命令台pip install ultralytics，如果用pip网速不好或者拒绝访问，可以到ultralytics官网下载YOLO源码，在源码路径那里会有setup.py文件，命令台cd到有setup.py那里然后安装包即可。
            2.以源码方式运行。到ultralytics官网下载YOLO源码，然后因为每个模块都有相应定义好功能的.py文件或者已经初始化加载层级之间包的__init__.py文件，所以是可以直接调用的，
              在ultralytics同级目录那里写自己的py文件即可。
2.编写train.py和val.py以及predict.py文件。这个ultralytics官网https://docs.ultralytics.com/zh/有对应说明用法。
3.制作数据集。获取images的方式，可以是寻找开源数据集，可以通过爬虫爬取的方式获取图片，可以自己拍。然后标注可以用makesense官方网站，也可以用labelme、labelmg等工具导出yolo格式的txt文件。可以标注一定量的数据集后，使用数据增强脚本连带图片和标签一起变多从而扩充数据集，最后再数据集划分。数据集的格式有两种，一种是整体划分为images和labels，然后每个images和labels里面再对应train、val、test；另一种是先整体划分为train、val、test三个文件夹，然后每一个文件夹里面对应有images和labels两个文件夹。但不论哪种格式都要要注意的是千万要注意images和labels的拼写不要错，因为YOLO官方脚本设定寻找路径是对应那两个名。
4.配置dataset.yaml文件里面的目录路径，类别。
5.直接训练，然后训练结果默认会保存在runs/detect/train中，当然可以通过导入setings包修改默认路径。
