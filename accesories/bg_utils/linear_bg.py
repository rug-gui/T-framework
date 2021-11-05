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
    vertical = False
    horizontal = False
    for i, color in enumerate(interpolate(f_co, t_co, gradient.width)):
        if vertical:   
            draw.line([(0, i), (gradient.width, i)], tuple(color), width=1)
        elif horizontal:
            draw.line([(i, 0), (i, gradient.height)], tuple(color), width=1)
        else:
            draw.line([(i*2, 0), (0, i*2)], tuple(color), width=2)  
    gradient.save('assets/bg/0.png')