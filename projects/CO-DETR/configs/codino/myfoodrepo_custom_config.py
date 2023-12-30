_base_ = './co_dino_5scale_swin_l_lsj_16xb1_3x_coco.py'

dataset_type = "CocoDataset"
classes = ('water', 'pear', 'egg', 'grapes', 'butter', 'bread-white', 'jam', 'bread-whole-wheat', 'apple', 'tea-green',
           'white-coffee-with-caffeine', 'tea-black', 'mixed-salad-chopped-without-sauce', 'cheese', 'tomato-sauce',
           'pasta-spaghetti', 'carrot', 'onion', 'beef-cut-into-stripes-only-meat', 'rice-noodles-vermicelli',
           'salad-leaf-salad-green', 'bread-grain', 'espresso-with-caffeine', 'banana', 'mixed-vegetables',
           'bread-wholemeal', 'savoury-puff-pastry', 'wine-white', 'dried-meat', 'fresh-cheese', 'red-radish',
           'hard-cheese', 'ham-raw', 'bread-fruit', 'oil-vinegar-salad-dressing', 'tomato', 'cauliflower',
           'potato-gnocchi', 'wine-red', 'sauce-cream', 'pasta-linguini-parpadelle-tagliatelle', 'french-beans',
           'almonds', 'dark-chocolate', 'mandarine', 'semi-hard-cheese', 'croissant', 'sushi', 'berries', 'biscuits',
           'thickened-cream-35', 'corn', 'celeriac', 'alfa-sprouts', 'chickpeas', 'leaf-spinach', 'rice',
           'chocolate-cookies', 'pineapple', 'tart', 'coffee-with-caffeine', 'focaccia', 'pizza-with-vegetables-baked',
           'soup-vegetable', 'bread-toast', 'potatoes-steamed', 'spaetzle', 'frying-sausage', 'lasagne-meat-prepared',
           'boisson-au-glucose-50g', 'ma1-4esli', 'peanut-butter', 'chips-french-fries', 'mushroom', 'ratatouille',
           'veggie-burger', 'country-fries', 'yaourt-yahourt-yogourt-ou-yoghourt-natural', 'hummus', 'fish', 'beer',
           'peanut', 'pizza-margherita-baked', 'pickle', 'ham-cooked', 'cake-chocolate', 'bread-french-white-flour',
           'sauce-mushroom', 'rice-basmati', 'soup-of-lentils-dahl-dhal', 'pumpkin', 'witloof-chicory',
           'vegetable-au-gratin-baked', 'balsamic-salad-dressing', 'pasta-penne', 'tea-peppermint', 'soup-pumpkin',
           'quiche-with-cheese-baked-with-puff-pastry', 'mango', 'green-bean-steamed-without-addition-of-salt',
           'cucumber', 'bread-half-white', 'pasta', 'beef-filet', 'pasta-twist', 'pasta-wholemeal', 'walnut',
           'soft-cheese', 'salmon-smoked', 'sweet-pepper', 'sauce-soya', 'chicken-breast', 'rice-whole-grain',
           'bread-nut', 'green-olives', 'roll-of-half-white-or-white-flour-with-large-void', 'parmesan', 'cappuccino',
           'flakes-oat', 'mayonnaise', 'chicken', 'cheese-for-raclette', 'orange', 'goat-cheese-soft', 'tuna', 'tomme',
           'apple-pie', 'rosti', 'broccoli', 'beans-kidney', 'white-cabbage', 'ketchup', 'salt-cake-vegetables-filled',
           'pistachio', 'feta', 'salmon', 'avocado', 'sauce-pesto', 'salad-rocket', 'pizza-with-ham-baked', 'gruya-re',
           'ristretto-with-caffeine', 'risotto-without-cheese-cooked', 'crunch-ma1-4esli', 'braided-white-loaf', 'peas',
           'chicken-curry-cream-coconut-milk-curry-spices-paste', 'bolognaise-sauce', 'bacon-frying', 'salami',
           'lentils', 'mushrooms', 'mashed-potatoes-prepared-with-full-fat-milk-with-butter', 'fennel',
           'chocolate-mousse', 'corn-crisps', 'sweet-potato', 'bircherma1-4esli-prepared-no-sugar-added',
           'beetroot-steamed-without-addition-of-salt', 'sauce-savoury', 'leek', 'milk', 'tea', 'fruit-salad',
           'bread-rye', 'salad-lambs-ear', 'potatoes-au-gratin-dauphinois-prepared', 'red-cabbage', 'praline',
           'bread-black', 'black-olives', 'mozzarella', 'bacon-cooking', 'pomegranate', 'hamburger-bread-meat-ketchup',
           'curry-vegetarian', 'honey', 'juice-orange', 'cookies', 'mixed-nuts', 'breadcrumbs-unspiced', 'chicken-leg',
           'raspberries', 'beef-sirloin-steak', 'salad-dressing', 'shrimp-prawn-large', 'sour-cream', 'greek-salad',
           'sauce-roast', 'zucchini', 'greek-yaourt-yahourt-yogourt-ou-yoghourt', 'cashew-nut', 'meat-terrine-pata-c',
           'chicken-cut-into-stripes-only-meat', 'couscous', 'bread-wholemeal-toast', 'craape-plain', 'bread-5-grain',
           'tofu', 'water-mineral', 'ham-croissant', 'juice-apple', 'falafel-balls', 'egg-scrambled-prepared',
           'brioche', 'bread-pita', 'pasta-haprnli', 'blue-mould-cheese', 'vegetable-mix-peas-and-carrots', 'quinoa',
           'crisps', 'beef', 'butter-spread-puree-almond', 'beef-minced-only-meat',
           'hazelnut-chocolate-spread-nutella-ovomaltine-caotina', 'chocolate', 'nectarine', 'ice-tea',
           'applesauce-unsweetened-canned', 'syrup-diluted-ready-to-drink', 'sugar-melon', 'bread-sourdough',
           'rusk-wholemeal', 'gluten-free-bread', 'shrimp-prawn-small', 'french-salad-dressing', 'pancakes',
           'milk-chocolate', 'pork', 'dairy-ice-cream', 'guacamole', 'sausage', 'herbal-tea', 'fruit-coulis',
           'water-with-lemon-juice', 'brownie', 'lemon', 'veal-sausage', 'dates', 'roll-with-pieces-of-chocolate',
           'taboula-c-prepared-with-couscous', 'croissant-with-chocolate-filling', 'eggplant', 'sesame-seeds',
           'cottage-cheese', 'fruit-tart', 'cream-cheese', 'tea-verveine', 'tiramisu', 'grits-polenta-maize-flour',
           'pasta-noodles', 'artichoke', 'blueberries', 'mixed-seeds', 'caprese-salad-tomato-mozzarella',
           'omelette-plain', 'hazelnut', 'kiwi', 'dried-raisins', 'kolhrabi', 'plums', 'beetroot-raw', 'cream',
           'fajita-bread-only', 'apricots', 'kefir-drink', 'bread', 'strawberries', 'wine-rosa-c', 'watermelon-fresh',
           'green-asparagus', 'white-asparagus', 'peach')
num_classes = 273

data_root = "D:/Data/Food/"

train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        _scope_='mmdet',
        dataset=dict(
            ann_file='train/annotations.json',
            backend_args=None,
            data_prefix=dict(img='train/images/'),
            data_root=data_root,
            filter_cfg=dict(filter_empty_gt=False, min_size=32),
            pipeline=[
                dict(type='LoadImageFromFile'),
                dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
                dict(
                    keep_ratio=True,
                    ratio_range=(
                        0.1,
                        2.0,
                    ),
                    scale=(
                        1280,
                        1280,
                    ),
                    type='RandomResize'),
                dict(
                    allow_negative_crop=True,
                    crop_size=(
                        1280,
                        1280,
                    ),
                    crop_type='absolute_range',
                    recompute_bbox=True,
                    type='RandomCrop'),
                dict(min_gt_bbox_wh=(
                    0.01,
                    0.01,
                ), type='FilterAnnotations'),
                dict(prob=0.5, type='RandomFlip'),
                dict(
                    pad_val=dict(img=(
                        114,
                        114,
                        114,
                    )),
                    size=(
                        1280,
                        1280,
                    ),
                    type='Pad'),
            ],
            type=dataset_type),
        pipeline=[
            dict(max_num_pasted=100, type='CopyPaste'),
            dict(type='PackDetInputs'),
        ],
        type='MultiImageMixDataset'),
    num_workers=1,
    persistent_workers=True,
    sampler=dict(_scope_='mmdet', shuffle=True, type='DefaultSampler'))

val_dataloader = dict(
    dataset=dict(
        ann_file='val/annotations.json',
        data_prefix=dict(img='val/images'),
        data_root=data_root,
        type=dataset_type),
)

test_dataloader = val_dataloader

model = dict(
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
            num_classes=273,
            stacked_convs=1,
            type='CoATSSHead'),
    ],
    query_head=dict(
        type="CoDINOHead",
        num_classes=273
    ),
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
                num_classes=273,
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
    ],
)

val_evaluator = dict(
    _scope_='mmdet',
    ann_file=f"{data_root}val/annotations.json",
    backend_args=None,
    format_only=False,
    metric='bbox',
    type='CocoMetric')

test_evaluator = val_evaluator
