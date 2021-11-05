def set(type,*args,**kwargs):
    print(type,args,kwargs)
    if type=='angular':
        from accesories.bg_utils import angled_bg
        color1=utils.color_string_to_rgb(args[0])
        color2=utils.color_string_to_rgb(args[1])
        angled_bg.setbackground(color1,color2)
    elif type=='linear':
        import linear_bg
        color1=utils.color_string_to_rgb(args[0])
        color2=utils.color_string_to_rgb(args[1])
        linear_bg.setbackground(color1,color2)
    elif type=='radial':
        import radial_bg
        color1=utils.color_string_to_rgb(args[0])
        color2=utils.color_string_to_rgb(args[1])
        radial_bg.setbackground(color1,color2)
    elif type=='blur':
        import blur_bg
        blur_bg.setbackground(args[0])
class utils:
    global NAMED_COLORS
    NAMED_COLORS = {
    "white":   (0xFF, 0xFF, 0xFF),
    "silver":  (0xC0, 0xC0, 0xC0),
    "gray":    (0x80, 0x80, 0x80),
    "black":   (0x00, 0x00, 0x00),
    "red":     (0xFF, 0x00, 0x00),
    "maroon":  (0x80, 0x00, 0x00),
    "yellow":  (0xFF, 0xFF, 0x00),
    "olive":   (0x80, 0x80, 0x00),
    "lime":    (0x00, 0xFF, 0x00),
    "green":   (0x00, 0x80, 0x00),
    "aqua":    (0x00, 0xFF, 0xFF),
    "teal":    (0x00, 0x80, 0x80),
    "blue":    (0x00, 0x00, 0xFF),
    "navy":    (0x00, 0x00, 0x80),
    "fuchsia": (0xFF, 0x00, 0xFF),
    "purple":  (0x80, 0x00, 0x80)
}
    def color_string_to_rgb(color_string):
        # Named color
        if color_string in NAMED_COLORS:
            return NAMED_COLORS[color_string]
        # #f00 or #ff0000 -> f00 or ff0000
        if color_string.startswith("#"):
            color_string = color_string[1:]
        # f00 -> ff0000
        if len(color_string) == 3:
            color_string = color_string[0] * 2 + color_string[1] * 2 + color_string[2] * 2  # noqa
        # ff0000 -> (255, 0, 0)
        return (
            int(color_string[0:2], 16),
            int(color_string[2:4], 16),
            int(color_string[4:], 16)
            ) 
