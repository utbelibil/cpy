group = displayio.Group()
group.x = 100
group.y = 120

image_file = open("/images/Gus.bmp", "rb")
image = displayio.OnDiskBitmap(image_file)
image_sprite = displayio.TileGrid(image, pixel_shader=getattr(image, 'pixel_shader', displayio.ColorConverter()))

group.append(image_sprite)
board.DISPLAY.show(group)

while True:
    pass