_base_ = 'co_dino_5scale_swin_l_lsj_16xb1_1x_coco.py'

image_size = (640, 640)
batch_augments = [
    dict(type='BatchFixedSizePad', size=image_size, pad_mask=True)
]

dataset_type = 'CocoDataset'
classes = (
    'water', 'pear', 'egg', 'grapes', 'butter', 'bread-white', 'jam',
    'bread-whole-wheat', 'apple', 'tea-green', 'white-coffee-with-caffeine',
    'tea-black', 'mixed-salad-chopped-without-sauce', 'cheese', 'tomato-sauce',
    'pasta-spaghetti', 'carrot', 'onion', 'beef-cut-into-stripes-only-meat',
    'rice-noodles-vermicelli', 'salad-leaf-salad-green', 'bread-grain',
    'espresso-with-caffeine', 'banana', 'mixed-vegetables', 'bread-wholemeal',
    'savoury-puff-pastry', 'wine-white', 'dried-meat', 'fresh-cheese',
    'red-radish', 'hard-cheese', 'ham-raw', 'bread-fruit',
    'oil-vinegar-salad-dressing', 'tomato', 'cauliflower', 'potato-gnocchi',
    'wine-red', 'sauce-cream', 'pasta-linguini-parpadelle-tagliatelle',
    'french-beans', 'almonds', 'dark-chocolate', 'mandarine',
    'semi-hard-cheese', 'croissant', 'sushi', 'berries', 'biscuits',
    'thickened-cream-35', 'corn', 'celeriac', 'alfa-sprouts', 'chickpeas',
    'leaf-spinach', 'rice', 'chocolate-cookies', 'pineapple', 'tart',
    'coffee-with-caffeine', 'focaccia', 'pizza-with-vegetables-baked',
    'soup-vegetable', 'bread-toast', 'potatoes-steamed', 'spaetzle',
    'frying-sausage', 'lasagne-meat-prepared', 'boisson-au-glucose-50g',
    'ma1-4esli', 'peanut-butter', 'chips-french-fries', 'mushroom',
    'ratatouille', 'veggie-burger', 'country-fries',
    'yaourt-yahourt-yogourt-ou-yoghourt-natural', 'hummus', 'fish', 'beer',
    'peanut', 'pizza-margherita-baked', 'pickle', 'ham-cooked',
    'cake-chocolate', 'bread-french-white-flour', 'sauce-mushroom',
    'rice-basmati', 'soup-of-lentils-dahl-dhal', 'pumpkin', 'witloof-chicory',
    'vegetable-au-gratin-baked', 'balsamic-salad-dressing', 'pasta-penne',
    'tea-peppermint', 'soup-pumpkin',
    'quiche-with-cheese-baked-with-puff-pastry', 'mango',
    'green-bean-steamed-without-addition-of-salt', 'cucumber',
    'bread-half-white', 'pasta', 'beef-filet', 'pasta-twist',
    'pasta-wholemeal', 'walnut', 'soft-cheese', 'salmon-smoked',
    'sweet-pepper', 'sauce-soya', 'chicken-breast', 'rice-whole-grain',
    'bread-nut', 'green-olives',
    'roll-of-half-white-or-white-flour-with-large-void', 'parmesan',
    'cappuccino', 'flakes-oat', 'mayonnaise', 'chicken', 'cheese-for-raclette',
    'orange', 'goat-cheese-soft', 'tuna', 'tomme', 'apple-pie', 'rosti',
    'broccoli', 'beans-kidney', 'white-cabbage', 'ketchup',
    'salt-cake-vegetables-filled', 'pistachio', 'feta', 'salmon', 'avocado',
    'sauce-pesto', 'salad-rocket', 'pizza-with-ham-baked', 'gruya-re',
    'ristretto-with-caffeine', 'risotto-without-cheese-cooked',
    'crunch-ma1-4esli', 'braided-white-loaf', 'peas',
    'chicken-curry-cream-coconut-milk-curry-spices-paste', 'bolognaise-sauce',
    'bacon-frying', 'salami', 'lentils', 'mushrooms',
    'mashed-potatoes-prepared-with-full-fat-milk-with-butter', 'fennel',
    'chocolate-mousse', 'corn-crisps', 'sweet-potato',
    'bircherma1-4esli-prepared-no-sugar-added',
    'beetroot-steamed-without-addition-of-salt', 'sauce-savoury', 'leek',
    'milk', 'tea', 'fruit-salad', 'bread-rye', 'salad-lambs-ear',
    'potatoes-au-gratin-dauphinois-prepared', 'red-cabbage', 'praline',
    'bread-black', 'black-olives', 'mozzarella', 'bacon-cooking',
    'pomegranate', 'hamburger-bread-meat-ketchup', 'curry-vegetarian', 'honey',
    'juice-orange', 'cookies', 'mixed-nuts', 'breadcrumbs-unspiced',
    'chicken-leg', 'raspberries', 'beef-sirloin-steak', 'salad-dressing',
    'shrimp-prawn-large', 'sour-cream', 'greek-salad', 'sauce-roast',
    'zucchini', 'greek-yaourt-yahourt-yogourt-ou-yoghourt', 'cashew-nut',
    'meat-terrine-pata-c', 'chicken-cut-into-stripes-only-meat', 'couscous',
    'bread-wholemeal-toast', 'craape-plain', 'bread-5-grain', 'tofu',
    'water-mineral', 'ham-croissant', 'juice-apple', 'falafel-balls',
    'egg-scrambled-prepared', 'brioche', 'bread-pita', 'pasta-haprnli',
    'blue-mould-cheese', 'vegetable-mix-peas-and-carrots', 'quinoa', 'crisps',
    'beef', 'butter-spread-puree-almond', 'beef-minced-only-meat',
    'hazelnut-chocolate-spread-nutella-ovomaltine-caotina', 'chocolate',
    'nectarine', 'ice-tea', 'applesauce-unsweetened-canned',
    'syrup-diluted-ready-to-drink', 'sugar-melon', 'bread-sourdough',
    'rusk-wholemeal', 'gluten-free-bread', 'shrimp-prawn-small',
    'french-salad-dressing', 'pancakes', 'milk-chocolate', 'pork',
    'dairy-ice-cream', 'guacamole', 'sausage', 'herbal-tea', 'fruit-coulis',
    'water-with-lemon-juice', 'brownie', 'lemon', 'veal-sausage', 'dates',
    'roll-with-pieces-of-chocolate', 'taboula-c-prepared-with-couscous',
    'croissant-with-chocolate-filling', 'eggplant', 'sesame-seeds',
    'cottage-cheese', 'fruit-tart', 'cream-cheese', 'tea-verveine', 'tiramisu',
    'grits-polenta-maize-flour', 'pasta-noodles', 'artichoke', 'blueberries',
    'mixed-seeds', 'caprese-salad-tomato-mozzarella', 'omelette-plain',
    'hazelnut', 'kiwi', 'dried-raisins', 'kolhrabi', 'plums', 'beetroot-raw',
    'cream', 'fajita-bread-only', 'apricots', 'kefir-drink', 'bread',
    'strawberries', 'wine-rosa-c', 'watermelon-fresh', 'green-asparagus',
    'white-asparagus', 'peach')
num_classes = 273

data_root = 'D:/Data/Food/'

metainfo = dict(
    classes=classes,
    palette=[(205, 73, 104), (142, 5, 47), (28, 170, 183), (133, 42, 152),
             (162, 205, 45), (243, 226, 222), (164, 137, 34), (99, 251, 124),
             (58, 129, 249), (65, 163, 5), (146, 222, 58), (132, 221, 90),
             (49, 44, 160), (253, 219, 206), (235, 33, 120), (227, 238, 176),
             (194, 247, 153), (99, 82, 137), (182, 72, 44), (142, 166, 169),
             (114, 208, 37), (103, 149, 77), (118, 85, 118), (71, 14, 75),
             (217, 123, 18), (206, 101, 86), (54, 7, 175), (141, 45, 166),
             (24, 188, 181), (14, 0, 100), (68, 133, 21), (88, 224, 166),
             (26, 57, 242), (19, 85, 156), (13, 6, 212), (195, 62, 58),
             (157, 114, 185), (133, 39, 39), (11, 140, 26), (104, 178, 127),
             (155, 51, 134), (56, 191, 94), (6, 168, 109), (179, 92, 240),
             (108, 76, 53), (33, 59, 168), (95, 4, 30), (98, 138, 144),
             (28, 239, 159), (194, 244, 1), (128, 5, 90), (2, 88, 39),
             (141, 92, 128), (79, 173, 163), (110, 200, 67), (220, 19, 239),
             (63, 88, 218), (211, 185, 14), (101, 17, 195), (237, 52, 174),
             (195, 234, 6), (222, 243, 117), (179, 2, 75), (154, 235, 61),
             (206, 179, 92), (233, 232, 239), (211, 13, 174), (105, 0, 97),
             (153, 65, 203), (79, 213, 90), (144, 87, 213), (8, 65, 132),
             (35, 53, 146), (42, 182, 37), (96, 167, 31), (149, 220, 241),
             (119, 43, 105), (191, 135, 0), (193, 205, 113), (125, 181, 79),
             (33, 0, 189), (100, 226, 238), (46, 26, 6), (230, 195, 239),
             (234, 238, 183), (186, 251, 2), (123, 162, 127), (37, 127, 76),
             (115, 232, 86), (220, 235, 74), (195, 122, 100), (45, 26, 217),
             (120, 138, 224), (146, 28, 100), (117, 209, 95), (184, 81, 239),
             (34, 202, 223), (224, 16, 32), (34, 220, 183), (184, 41, 4),
             (95, 244, 48), (186, 87, 146), (214, 92, 93), (29, 236, 54),
             (80, 221, 69), (193, 111, 26), (48, 204, 109), (25, 15, 231),
             (233, 230, 39), (55, 207, 176), (236, 42, 122), (241, 47, 208),
             (17, 232, 124), (77, 229, 93), (238, 153, 121), (219, 142, 186),
             (116, 247, 38), (192, 181, 19), (188, 236, 201), (170, 221, 66),
             (20, 158, 44), (98, 219, 111), (55, 186, 76), (224, 249, 50),
             (59, 53, 193), (57, 125, 12), (221, 192, 41), (129, 80, 76),
             (179, 72, 84), (87, 164, 212), (74, 85, 246), (173, 238, 252),
             (233, 40, 114), (190, 222, 92), (200, 15, 141), (52, 115, 6),
             (164, 54, 90), (161, 149, 80), (225, 195, 165), (130, 194, 225),
             (118, 12, 41), (7, 126, 207), (241, 215, 201), (116, 234, 184),
             (81, 222, 148), (160, 104, 106), (130, 128, 13), (234, 120, 231),
             (40, 86, 51), (83, 173, 200), (143, 86, 99), (36, 1, 240),
             (20, 232, 62), (130, 69, 202), (216, 112, 88), (174, 3, 211),
             (236, 84, 22), (216, 175, 100), (156, 147, 149), (195, 96, 102),
             (98, 39, 28), (30, 41, 1), (192, 75, 23), (231, 37, 113),
             (174, 199, 165), (235, 232, 21), (17, 86, 205), (78, 22, 63),
             (82, 139, 217), (38, 37, 109), (88, 8, 35), (73, 36, 151),
             (120, 77, 74), (69, 189, 84), (163, 134, 128), (79, 129, 193),
             (129, 111, 126), (230, 161, 181), (5, 155, 180), (50, 90, 57),
             (255, 209, 116), (186, 124, 59), (194, 98, 141), (203, 97, 78),
             (163, 154, 190), (35, 149, 204), (214, 153, 132), (29, 119, 93),
             (185, 230, 55), (177, 125, 60), (186, 234, 114), (161, 184, 109),
             (133, 141, 76), (158, 169, 237), (209, 3, 253), (233, 103, 155),
             (224, 35, 89), (207, 63, 236), (153, 180, 227), (5, 14, 180),
             (161, 201, 38), (163, 255, 99), (74, 84, 165), (89, 76, 58),
             (94, 220, 108), (166, 217, 74), (59, 179, 150), (155, 113, 87),
             (14, 10, 252), (2, 30, 66), (220, 142, 43), (69, 181, 180),
             (104, 159, 5), (41, 179, 58), (58, 119, 127), (222, 160, 217),
             (24, 150, 237), (119, 50, 117), (203, 150, 214), (231, 137, 143),
             (37, 90, 165), (157, 92, 245), (136, 159, 26), (237, 39, 101),
             (180, 15, 73), (157, 166, 217), (106, 8, 93), (45, 66, 105),
             (95, 84, 146), (224, 102, 230), (240, 178, 215), (68, 40, 7),
             (176, 17, 154), (219, 209, 198), (206, 5, 93), (53, 197, 143),
             (109, 22, 253), (67, 57, 14), (71, 15, 19), (105, 109, 134),
             (172, 110, 186), (214, 136, 137), (190, 249, 216), (105, 64, 145),
             (216, 59, 238), (235, 99, 231), (47, 220, 27), (147, 198, 179),
             (184, 147, 221), (92, 9, 86), (79, 161, 9), (170, 175, 118),
             (120, 173, 154), (26, 128, 61), (148, 112, 179), (79, 227, 220),
             (243, 177, 133), (233, 243, 113), (25, 30, 124), (25, 220, 114),
             (192, 37, 24), (148, 242, 62), (17, 130, 3), (140, 141, 83),
             (39, 29, 226), (184, 82, 74), (182, 2, 167), (105, 221, 203),
             (9, 189, 38), (200, 107, 62), (159, 33, 48), (78, 250, 76),
             (53, 149, 77)])

default_hooks = dict(
    logger=dict(_scope_='mmdet', interval=1, type='LoggerHook'))

load_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(
        type='RandomResize',
        scale=image_size,
        ratio_range=(0.1, 2.0),
        keep_ratio=True),
    dict(
        type='RandomCrop',
        crop_type='absolute_range',
        crop_size=image_size,
        recompute_bbox=True,
        allow_negative_crop=True),
    dict(type='FilterAnnotations', min_gt_bbox_wh=(1e-2, 1e-2)),
    dict(type='RandomFlip', prob=0.5),
    dict(type='Pad', size=image_size, pad_val=dict(img=(114, 114, 114))),
]

train_dataloader = dict(
    dataset=dict(
        dataset=dict(
            type=dataset_type,
            metainfo=metainfo,
            data_root=data_root,
            pipeline=load_pipeline,
            ann_file='train/annotations.json',
            data_prefix=dict(img='train/images/'))))

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=image_size, keep_ratio=True),
    dict(type='Pad', size=image_size, pad_val=dict(img=(114, 114, 114))),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(
        type='PackDetInputs',
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor'))
]

val_dataloader = dict(
    dataset=dict(
        _scope_='mmdet',
        ann_file='val/annotations.json',
        data_prefix=dict(img='val/images/'),
        metainfo=metainfo,
        pipeline=test_pipeline,
        data_root=data_root,
        type=dataset_type))

test_dataloader = val_dataloader

model = dict(
    data_preprocessor=dict(batch_augments=batch_augments),
    bbox_head=[
        dict(
            anchor_generator=dict(
                octave_base_scale=8,
                ratios=[
                    1.0,
                ],
                scales_per_octave=1,
                strides=[
                    4,
                    8,
                    16,
                    32,
                    64,
                    128,
                ],
                type='AnchorGenerator'),
            bbox_coder=dict(
                target_means=[
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ],
                target_stds=[
                    0.1,
                    0.1,
                    0.2,
                    0.2,
                ],
                type='DeltaXYWHBBoxCoder'),
            feat_channels=256,
            in_channels=256,
            loss_bbox=dict(loss_weight=24.0, type='GIoULoss'),
            loss_centerness=dict(
                loss_weight=12.0, type='CrossEntropyLoss', use_sigmoid=True),
            loss_cls=dict(
                alpha=0.25,
                gamma=2.0,
                loss_weight=12.0,
                type='FocalLoss',
                use_sigmoid=True),
            num_classes=num_classes,
            stacked_convs=1,
            type='CoATSSHead'),
    ],
    query_head=dict(num_classes=num_classes),
    roi_head=[
        dict(
            bbox_head=dict(
                bbox_coder=dict(
                    target_means=[
                        0.0,
                        0.0,
                        0.0,
                        0.0,
                    ],
                    target_stds=[
                        0.1,
                        0.1,
                        0.2,
                        0.2,
                    ],
                    type='DeltaXYWHBBoxCoder'),
                fc_out_channels=1024,
                in_channels=256,
                loss_bbox=dict(loss_weight=120.0, type='GIoULoss'),
                loss_cls=dict(
                    loss_weight=12.0,
                    type='CrossEntropyLoss',
                    use_sigmoid=False),
                num_classes=num_classes,
                reg_class_agnostic=False,
                reg_decoded_bbox=True,
                roi_feat_size=7,
                type='Shared2FCBBoxHead'),
            bbox_roi_extractor=dict(
                featmap_strides=[
                    4,
                    8,
                    16,
                    32,
                    64,
                ],
                finest_scale=56,
                out_channels=256,
                roi_layer=dict(
                    output_size=7, sampling_ratio=0, type='RoIAlign'),
                type='SingleRoIExtractor'),
            type='CoStandardRoIHead'),
    ])

val_evaluator = dict(ann_file=f'{data_root}val/annotations.json', )

test_evaluator = val_evaluator
