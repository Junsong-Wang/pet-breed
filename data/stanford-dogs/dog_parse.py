import scipy.io
import os
import cv2
import random
import xml.etree.ElementTree as ET

dog_images = './Images'
dog_annotation = './Annotation'
dog_train_annos_mat = './train_list.mat'
dog_test_annos_mat = './test_list.mat'
output_dir = './dog_detected'
output_txt_dir = '.'

def dog_annotation_processing(dog_annos_mat):
    mat = scipy.io.loadmat(dog_annos_mat)
    file_list = mat['file_list']
    annotation_list = mat['annotation_list']
    labels = mat['labels']
    file_str = ''
    labels_str = ''
    for i, filename_item in enumerate(file_list):
        filename = filename_item[0][0]
        annotation_filename = annotation_list[i][0][0]
        label = labels[i][0]
        root = ET.parse(dog_annotation + '/' + annotation_filename)
        bb = [int(root.find('object').find('bndbox').find('xmin').text), \
              int(root.find('object').find('bndbox').find('ymin').text), \
              int(root.find('object').find('bndbox').find('xmax').text), \
              int(root.find('object').find('bndbox').find('ymax').text)]
        print filename, bb, label
        img = cv2.imread(dog_images + '/' + filename)
        outBgr = img[bb[1]:bb[3], bb[0]:bb[2]]
        category = filename.split('/')[0]
        if not os.path.exists(output_dir + '/' + category):
            os.system('mkdir -p ' + output_dir + '/' + category)
            category_split = category.split('-')
            labels_str += category_split[0] + ' ' + category_split[1] + '\n' 
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, outBgr)
        file_str += filename + ' ' + str(int(label)-1) + '\n'
    return file_str, labels_str

if not os.path.exists(output_dir):
    os.system('mkdir -p ' + output_dir)

train_str, labels_words = dog_annotation_processing(dog_train_annos_mat)
fp = open(output_txt_dir + '/train.txt', 'w')
fp.write(train_str)
fp.close
fp = open(output_txt_dir + '/synset_words.txt', 'w')
fp.write(labels_words)
fp.close
val_str, labels_words = dog_annotation_processing(dog_test_annos_mat)
fp = open(output_txt_dir + '/val.txt', 'w')
fp.write(val_str)
fp.close



