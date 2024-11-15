from PIL import Image

img_offset = 30
img_file = 'monro.jpg'
result_file = 'resized_filtered_monro.jpg'

img = Image.open(img_file)
red_channel, green_channel, blue_channel = img.split()

coordinates = (img_offset, 0, red_channel.width, red_channel.height)
red_channel_left = red_channel.crop(coordinates)
coordinates = (img_offset/2, 0, red_channel.width-img_offset/2, 
               red_channel.height)
red_channel_centre = red_channel.crop(coordinates)
red_channel_blended = Image.blend(red_channel_left, red_channel_centre, 0.5)

coordinates = (0, 0, blue_channel.width-img_offset, blue_channel.height)
blue_channel_right = blue_channel.crop(coordinates)
coordinates = (img_offset/2, 0, blue_channel.width-img_offset/2, 
               blue_channel.height)
blue_channel_centre = blue_channel.crop(coordinates)
blue_channel_blended = Image.blend(blue_channel_right, blue_channel_centre, 0.5)

coordinates = (img_offset/2, 0, green_channel.width-img_offset/2, 
               green_channel.height)
green_channel = green_channel.crop(coordinates)

result_image = Image.merge('RGB', (red_channel_blended, green_channel, 
                                   blue_channel_blended))
result_image.thumbnail((80, 80))
result_image.save(result_file)
