from labcolorpicker import getColor, useLightTheme, useAlpha, rgb2lab

old_color = rgb2lab((255, 255, 255))
picked_color = getColor(old_color)
print(picked_color)

useLightTheme(True)
useAlpha(True)

old_color = rgb2lab((255, 230, 255)) + (50,)
picked_color = getColor(old_color)
print(picked_color)


# Using the old way of creating a ColorPicker:
from labcolorpicker import ColorPicker, lab2rgb, rgb2lab


my_color_picker = ColorPicker(useAlpha=True)
my_color_picker_light = ColorPicker(lightTheme=True)


old_color = rgb2lab((255, 255, 255)) + (50,)
picked_color = my_color_picker.getColor(old_color)
print(picked_color)


old_color = rgb2lab((255,0,255))
picked_color = my_color_picker_light.getColor(old_color)
print(picked_color)


# Have your color in LAB format?
old_color = (50, 100, 20, 60)  # LAB Color with 60% alpha
picked_color = my_color_picker.getColor(old_color)
picked_color = lab2rgb(picked_color[:3]) + picked_color[3:]
print(picked_color)
