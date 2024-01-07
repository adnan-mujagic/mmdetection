import random


def get_palette(n_classes):
    return [(random.randint(0,
                            255), random.randint(0,
                                                 255), random.randint(0, 255))
            for _ in range(n_classes)]


if __name__ == '__main__':
    print(get_palette(273))
