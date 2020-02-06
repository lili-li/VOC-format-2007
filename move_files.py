
import os,shutil

# move file to other directorys.
# files must satify this format as follow:
# "xxxx-xx.txt".
# @src: source path(type string)
# @dst: destination path(type string)
# @format: file format
def move_files(src, dst, format):
    list = []

    # Get all file name to a list.
    file = os.listdir(src)

    # Show all file.
    print("total file list", file)

    # Get vaild file name.
    for i in range(0, len(file)):
        #if file[i].rfind(format) != -1 and (int)file[i].find(".") >= 8000 and  (int)file[i] <= 9999:
        index = file[i].rfind(format)
        print("index = ", index)
        if index != -1 and (int)(file[i][0: index]) >= 8000 and (int)(file[i][0: index]) <= 9999:
            list.append(file[i])

    # Show vaild file.
    print(" move file ",list)

    # Move file to other directory
    for i in range(0, len(list)):
        shutil.move(src + "\\" + list[i], dst + "\\" + list[i])

# test code.
def main():
	move_files('C:\Software\pycharm_office\ecg_xiaobo\VOCdevkit\VOC2007\Annotations', 'C:\Software\pycharm_office\ecg_xiaobo\\test_images_2000\\test_xml', ".xml")

if __name__ == '__main__':
	main()