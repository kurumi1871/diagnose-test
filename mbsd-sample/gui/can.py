import tkinter as tk


class Entity():
    ''' Entity class '''
    def __init__(self, canvas, x, y, width=60, height=40):
        self.canvas = canvas
        self.x, self.y, self.width, self.height = x, y, width, height
        self.start_x = self.start_y = None
        self.connections = []

        self.id = self.canvas.create_rectangle(x, y, x + width, y + height,
                                               fill="lightblue", width=3)
        self.canvas.tag_bind(self.id, "<ButtonPress>", self.button_press)
        self.canvas.tag_bind(self.id, "<Motion>", self.move)
        self.canvas.tag_bind(self.id, "<ButtonRelease>", self.button_release)

    def button_press(self, event):
        ''' マウスのボタンが押されたときの処理 '''
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

    def move(self, event):
        ''' マウスが移動したときの処理 '''
        if event.state & 256:  # マウスボタン1が押されているときだけ（ドラッグ中のみ）
            can_x = self.canvas.canvasx(event.x)
            can_y = self.canvas.canvasy(event.y)
            coords = self.canvas.coords(self.id)
            coords[0] -= self.start_x - can_x
            coords[1] -= self.start_y - can_y
            coords[2] -= self.start_x - can_x
            coords[3] -= self.start_y - can_y
            self.canvas.coords(self.id, coords)
            self.start_x = can_x
            self.start_y = can_y
            self.x, self.y = coords[0:2]
            for connection in self.connections:
                connection.move(self)

    def button_release(self, event):  # pylint: disable=unused-argument
        ''' マウスのボタンが離されたとき '''
        self.start_x = self.start_y = None

    def get_center(self):
        ''' 中心座標を戻します '''
        return self.x + self.width//2, self.y + self.height//2

    def add_listener(self, connection):
        ''' コネクションのリスナーを登録します '''
        self.connections.append(connection)


class Connection():
    ''' Connection class '''
    def __init__(self, canvas, start_entity, end_entity):
        self.canvas = canvas
        self.start_e = start_entity
        self.end_e = end_entity
        start_entity.add_listener(self)
        end_entity.add_listener(self)

        self.id = self.canvas.create_line(self.get_intersection(start_entity),
                                          self.get_intersection(end_entity))

    def move(self, entity):
        ''' エンティティが移動したときの処理（エンティティから呼び出される）'''
        coords = self.canvas.coords(self.id)
        if entity == self.start_e:
            coords[0:2] = self.get_intersection(entity)
            coords[2:4] = self.get_intersection(self.end_e)
        elif entity == self.end_e:
            coords[0:2] = self.get_intersection(self.start_e)
            coords[2:4] = self.get_intersection(entity)
        self.canvas.coords(self.id, coords)

    def get_intersection(self, entity):
        ''' 矩形との接点を求める '''
        x, y = entity.get_center()
        height, width = entity.height // 2, entity.width // 2
        dx, dy = self.end_e.x - self.start_e.x, self.end_e.y - self.start_e.y
        if entity == self.end_e:
            dx, dy = -dx, -dy
        if abs(dy / dx) < (height / width):  # 垂直側
            x_pos = x + width if dx > 0 else x - width
            y_pos = y + dy * width / abs(dx)
        else:  # 水平側
            x_pos = x + dx * height / abs(dy)
            y_pos = y + height if dy > 0 else y - height
        return x_pos, y_pos


class Application(tk.Tk):
    ''' Application class '''
    def __init__(self):
        super().__init__()
        self.title("Connecter test 2")
        self.geometry("640x320")

        self.canvas = tk.Canvas(self, background="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        entity1 = Entity(self.canvas, 40, 80)
        entity2 = Entity(self.canvas, 240, 160)
        Connection(self.canvas, entity1, entity2)
        entity3 = Entity(self.canvas, 420, 60)
        Connection(self.canvas, entity2, entity3)


def main():
    ''' main function '''
    application = Application()
    application.mainloop()


if __name__ == "__main__":
    main()