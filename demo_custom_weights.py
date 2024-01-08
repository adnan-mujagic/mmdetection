import os
import random

from mmdet.apis import DetInferencer

NUM_IMAGES = 10
WEIGHTS_PATH = 'D:/Projects/Cereal/Weights/epoch_2_co_detr.pth'
VALIDATION_IMAGES_PATH = 'D:/Data/Food/test/images'
OUTPUT_DIR = 'outputs/'

config_path = 'projects/CO-DETR/configs/codino/myfoodrepo_small_custom_confg.py'
all_images = os.listdir(VALIDATION_IMAGES_PATH)
selected_images = random.sample(all_images, NUM_IMAGES)


def main():
    model = DetInferencer(config_path, WEIGHTS_PATH, device='cpu')

    for image in selected_images:
        model(os.path.join(VALIDATION_IMAGES_PATH, image), out_dir=OUTPUT_DIR)


if __name__ == '__main__':
    main()
