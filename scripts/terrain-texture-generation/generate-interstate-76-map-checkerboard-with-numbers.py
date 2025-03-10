# https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
# https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
from PIL import Image, ImageDraw, ImageFont

SQUARE_COUNT = 8
TEXTURE_DIMS = [256, 64, 64, 32, 16]
PIL_MODE_ONE_BYTE_INDEXED_COLOUR = 'P'
FONT_NAME = "GOTHICB.TTF"

# Colour indices in superpal.act
INDEX_BLUE = 69
INDEX_YELLOW = 118

INDEX_GREEN = 136
INDEX_PURPLE = 71

INDEX_RED = 103
INDEX_AQUA = 174

INDEX_BLACK = 255
INDEX_WHITE = 240

INDEX_ORANGE = 107
INDEX_PALE_GREEN = 215

texture_dim_to_draw_numbers = {
    256: True,
    64: True,
    32: False,
    16: False
}

texture_dim_to_image_count = {
    256: 0,
    64: 0,
    32: 0,
    16: 0
}

texture_dim_to_colour_1 = {
    '256-1': INDEX_BLUE,
    '64-1': INDEX_GREEN,
    '64-2': INDEX_RED,
    '32-1': INDEX_BLACK,
    '16-1': INDEX_ORANGE
}

texture_dim_to_colour_2 = {
    '256-1': INDEX_YELLOW,
    '64-1': INDEX_PURPLE,
    '64-2': INDEX_AQUA,
    '32-1': INDEX_WHITE,
    '16-1': INDEX_PALE_GREEN
}

palette_path = 'superpal.act'
with open(palette_path, 'rb') as palette_file:
    palette_bytes = palette_file.read()

for texture_dim in TEXTURE_DIMS:
    square_pixel_dim = texture_dim // SQUARE_COUNT

    font_size = round(0.8 * square_pixel_dim)
    font = ImageFont.truetype(FONT_NAME, font_size)

    draw_numbers = texture_dim_to_draw_numbers[texture_dim]

    texture_dim_to_image_count[texture_dim] = texture_dim_to_image_count[texture_dim] + 1
    texture_dim_string = f'{texture_dim}-{texture_dim_to_image_count[texture_dim]}'

    out_path = f'checkerboard-with-numbers-map-bytes-{texture_dim_string}'

    colour_index_1 = texture_dim_to_colour_1[texture_dim_string]
    colour_index_2 = texture_dim_to_colour_2[texture_dim_string]

    image_output = Image.new(PIL_MODE_ONE_BYTE_INDEXED_COLOUR, (texture_dim, texture_dim), color = colour_index_1)
    draw = ImageDraw.Draw(image_output)

    for col in range(SQUARE_COUNT):
        for row in range(SQUARE_COUNT):
            #number = row * DIVISION_COUNT + col + 1
            number = (7 - row) * SQUARE_COUNT + col

            textX = (col * square_pixel_dim) + square_pixel_dim / 2
            textY = (row * square_pixel_dim) + square_pixel_dim / 2

            if (col + row) % 2 != 0:
                x0 = col * square_pixel_dim
                y0 = row * square_pixel_dim
                x1 = x0 + square_pixel_dim - 1
                y1 = y0 + square_pixel_dim - 1
                # rectangle() is inclusive of both start and end coordinates, hence -1 for x1 and y1 above.
                draw.rectangle([x0, y0, x1, y1], colour_index_2)
                
                if draw_numbers:
                    draw.text((textX, textY), str(number), font=font, anchor="mm", fill=colour_index_1)
            else:
                if draw_numbers:
                    draw.text((textX, textY), str(number), font=font, anchor="mm", fill=colour_index_2)

    # The bytes from these files need to be manually used to overwrite M16 textures in a PAK file.
    # It's also necessary to set the colour palette offset for each M16 file (8th byte) to 0 within the PAK file.
    with open(out_path + '.dat', 'wb') as file:
        file.write(image_output.transpose(Image.FLIP_TOP_BOTTOM).tobytes())

    # Save a PNG for comparison
    image_output.putpalette(palette_bytes)
    image_not_indexed = image_output.convert('RGB')
    image_not_indexed.save(out_path + '.png', 'PNG')
