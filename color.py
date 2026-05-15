class Color():
    def __init__(self, color_code: int):
        if(color_code > 0xffffff or color_code < 0x000000):
            raise ValueError(f"color {hex(color_code)} is out of range")

        self.color_code = color_code
    def __repr__(self):
        return "class Color {\"color_code\": " + f"0x{'0' * (8 - len(hex(self.color_code))) + hex(self.color_code)[2:]}" + "}"

red =     Color(0xff0000)
orange =  Color(0xffaa00)
yellow =  Color(0xffff00)
green =   Color(0x00ff00)
cyan =    Color(0x00ffff)
blue =    Color(0x0000ff)
magenta = Color(0xff00ff)
white =   Color(0xffffff)
gray =    Color(0x888888)
grey =    Color(0x888888)
black =   Color(0x000000)
