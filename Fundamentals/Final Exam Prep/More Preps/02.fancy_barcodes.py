import re


def emoji_detector(loop_r):
    for _ in range(loop_r):
        barcode = input()
        if re.match(r'[@][#]+[A-Z][a-zA-Z0-9]{4,}[A-Z][@][#]+', barcode):
            product_group = "".join(char for char in barcode if char.isdigit())
            if not product_group:
                product_group = '00'
            print(f'Product group: {product_group}')
        else:
            print('Invalid barcode')


loop_range = int(input())
emoji_detector(loop_range)
