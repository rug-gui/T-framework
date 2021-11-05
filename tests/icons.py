import tkinter as tk
from typing import ChainMap
from PIL import ImageOps
from PIL.ImageOps import colorize

from wand import image


if False:

    from pytkfaicons.conv import build, get_repo, convert_all, copy_meta

    # build(opts="-c", callb=print)
    # convert_all()
    # copy_meta()


from pytkfaicons.conv import get_scaled_tk_icon
from pytkfaicons.icons import get_icon_image, tk_image_loader, get_tk_icon

root = tk.Tk()

frame1 = tk.Frame(root)
tk.Label(frame1, text="on the fly resized (slow)").pack(side="left")

# resize on the fly (slow)
img0 = get_scaled_tk_icon("arrow-left", "solid", 64)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img0).pack(side="left")

img1 = get_scaled_tk_icon("arrow-right", "solid", 48)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img1).pack(side="left")

img2 = get_scaled_tk_icon("asterisk", "solid", 32)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img2).pack(side="left")

img3 = get_scaled_tk_icon("barcode", "solid", 24)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img3).pack(side="left")

img4 = get_scaled_tk_icon("baby", "solid", 12)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img4).pack(side="left")

img5 = get_scaled_tk_icon("bahai", "solid", 8)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img5).pack(side="left")

img6 = get_scaled_tk_icon("bars", "solid", 6)
tk.Button(frame1, justify=tk.LEFT, padx=10, image=img6).pack(side="left")

frame1.pack()

# this is the same implementation as get_tk_faicon.icon()
# using get_icon_image(), and tk_image_loader() as loader
# what returns tk.PhotoImage

class faicon():
    def icon(name, style):
        # pre-calculated 32px height icons (fast)
        return get_icon_image(name, style, loader=tk_image_loader)
    def inverticon(name, style):
        from PIL import Image,ImageTk,ImageOps
        image = get_icon_image(name, style, loader=Image.open)
        if image.mode == 'RGBA':
            r,g,b,a = image.split()
            rgb_image = Image.merge('RGB', (r,g,b))

            inverted_image = ImageOps.invert(rgb_image)

            r2,g2,b2 = inverted_image.split()

            final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
            return ImageTk.PhotoImage(final_transparent_image)
        else:
            inverted_image = ImageOps.invert(image)
            return ImageTk.PhotoImage(inverted_image)
    def coloricon(name, style,cname):
        from PIL import Image,ImageTk
        import numpy as np
        image = get_icon_image(name, style, loader=Image.open)
        im =image
        data = np.array(im)   # "data" is a height x width x 4 numpy array
        red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
        # Replace white with red... (leaves alpha values alone...)
        white_areas = (red == 0) & (blue == 0) & (green == 0)
        data[..., :-1][white_areas.T] = (0, 255, 0) # Transpose back needed
        im2 = Image.fromarray(data)
        return ImageTk.PhotoImage(im2)
    def color(name, style,cname):
        from PIL import Image,ImageTk
        img = get_icon_image(name, style, loader=Image.open)
        pixdata = img.load()
        # Clean the background noise, if color != white, then set to black.
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y] == (0, 0, 0, 255):
                    pixdata[x, y] = (0, 255, 150, 255)
        im = img
        im.show()
        return ImageTk.PhotoImage(im)

frame2 = tk.Frame(root)

left = faicon.inverticon("arrow-left", "solid")
right = faicon.inverticon("arrow-right", "solid")
asterisk = faicon.inverticon("asterisk", "solid")
barcode = faicon.inverticon("barcode", "solid")
baby = faicon.inverticon("baby", "solid")
bahai = faicon.inverticon("bahai", "solid")
bars = faicon.inverticon("bars", "solid")
spotify = faicon.coloricon("spotify","brands","green")

tk.Label(frame2, text="pre-caclulated (fast)").pack(side="left")

tk.Button(frame2, justify=tk.LEFT, padx=10, image=left,bg='black').pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=right,bg='black').pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=asterisk,bg='black').pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=barcode,bg='black').pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=baby,bg='black').pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=bahai,bg='black').pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=bars,bg='black').pack(side="left")
tk.Button(frame2, justify=tk.LEFT, padx=10, image=spotify,bg='black').pack(side="left")

frame2.pack()

root.mainloop()
