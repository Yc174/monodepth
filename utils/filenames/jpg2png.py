import os

txt_name = 'kitti_test_files.txt'
txt2_png_name = 'kitti_test_files_png.txt'
new_file = open(txt2_png_name, 'w')
with open(txt_name, 'r') as f:
    for line in f:
        l = line.replace('jpg', 'png')
        print(l)
        new_file.write(l)

new_file.close()