def setbackground(color1,color2):
    from PIL import Image, ImageDraw

    def interpolate(f_co, t_co, interval):
        det_co =[(t - f) / interval for f , t in zip(f_co, t_co)]
        for i in range(interval):
            yield [round(f + det * i) for f, det in zip(f_co, det_co)]


    imgsize=(1920,1080)
    gradient = Image.new('RGBA', imgsize, color=0)
    draw = ImageDraw.Draw(gradient)

    f_co = (253, 46, 216)
    t_co = (23, 214, 255)
    for i, color in enumerate(interpolate(f_co, t_co, gradient.width * 2)):
        draw.line([(i, 0), (0, i)], tuple(color), width=1)
    gradient.show()
