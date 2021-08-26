from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
text = load_texture('texture/img_3.png')


class Cube(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            model='cube',
            color=color.white,
            texture=text,
            position=position,
            origin_y=0.1,
            highlight_color=color.blue,
            pressed_color=color.red

        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                cube = Cube(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)


for z in range(20):
    for x in range(20):
        cube = Cube(position=(x, 0, z))
sky_texture = load_texture('texture/img_4.png')


class Sky(Entity):
    def __init__(self):
        super().__init__(
            model="sphere",
            parent=scene,
            texture=sky_texture,
            scale=150,
            double_sided=True

        )


sky = Sky()
player = FirstPersonController()

app.run()
