from PIL import Image, ImageDraw, ImageFont
import os

class text_draw():
    def __init__(self, text, coordinates, color=(255, 255, 255), spacing=37):
        self.text = text
        self.coordinates = coordinates
        self.color = color
        self.spacing = spacing
        self.json = {"text": self.text, "coordinates": self.coordinates, "color": self.color, "spacing": self.spacing}

    def text(self):
        return self.text

    def coordinates(self):
        return self.coordinates

    def color(self):
        return self.color

    def spacing(self):
        return self.spacing


def shablon_edit(fold, ref, font, texts, user_id="test_id", font_size=17):
    path = f"""{os.path.abspath("__file__")[:-9]}\{fold}\{'redy'}"""
    im = Image.open(f'{ref}')

    font = ImageFont.truetype(f'{font}', size=font_size)
    draw_text = ImageDraw.Draw(im)

    for text in texts:
        draw_text.text(xy=text.coordinates,
                       text=text.text,
                       font=font,
                       fill=text.color,
                       spacing=text.spacing)

    list_of_files = []
    num = 0
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                list_of_files.append(os.path.join(file))
        editing_files = []
        for file in list_of_files:
            file = (file).split('.')[0]
            file = file.split('_')
            file[1] = int(file[1])
            editing_files.append(file)
        num = max([int(i[-1]) for i in editing_files]) + 1
    except:
        num = 0
    print(path)
    im.save(f"{path}\image_{num}.png")
    return f"{path}\image_{num}.png"


def new_directory(parent_dir, path_name):
    # new_directory(f"""{os.path.abspath("__file__")[:-9]}\users""", 'ds')
    path = os.path.join(parent_dir, path_name)
    try:
        os.mkdir(path)
    except:
        return 'Error: have same directory'


def json_convert(json: dict, user_name="test_user"):
    # test meaning
    team_name_1 = text_draw(text='\n'.join(json["team name"][:9]),
                            coordinates=(266, 270))
    team_name_2 = text_draw(text='\n'.join(json["team name"][9:18]),
                            coordinates=(775, 270))
    wwcd = text_draw(text='\n'.join(json["wwcd"][:9]),
                     coordinates=(485 + 18, 270))
    kp_1 = text_draw(text='\n'.join(json["plc pts"][:9]),
                     coordinates=(539 + 9, 270))
    kp_2 = text_draw(text='\n'.join(json["plc pts"][9:18]),
                     coordinates=(1039 + 9, 270))
    pp_1 = text_draw(text='\n'.join(json["kills"][:9]),
                     coordinates=(578 + 9, 270))
    pp_2 = text_draw(text='\n'.join(json["kills"][9:18]),
                     coordinates=(1078 + 9, 270))
    total_1 = text_draw(text='\n'.join(json["total pts"][:9]),
                        coordinates=(634 + 11, 270))
    total_2 = text_draw(text='\n'.join(json["total pts"][9:18]),
                        coordinates=(1134 + 11, 270))

    texts = [team_name_1, wwcd, kp_1, pp_1, total_1, team_name_2, kp_2, pp_2, total_2]
    return shablon_edit(f"users\{'test_user'}", "background.png", "Gotham Pro Bold.ttf", texts=texts)

if __name__ == '__main__':
    json = {'team name': ['п', 'р', 'о', 'л', 'а', 'в', 'ы', 'а', 'п', 'р', 'о', 'и', 'м', 'с', 'ч', '', '', '', '', '', '',
                   '', ''],
     'games': ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0',
               '0', '0'],
     'wwcd': ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0',
              '0', '0'],
     'plc pts': ['0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '2', '4', '6', '0', '0', '0', '0', '0',
                 '0', '0', '0'],
     'kills': ['12', '12', '12', '12', '1', '11', '1', '13', '13', '13', '15', '14', '15', '16', '16', '0', '0', '0',
               '0', '0', '0', '0', '0'],
     'total pts': ['12', '12', '12', '12', '1', '11', '1', '14', '14', '14', '16', '15', '17', '20', '22', '0', '0',
                   '0', '0', '0', '0', '0', '0']}
    json_convert(json)

