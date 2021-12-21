# https://www.pytry3g.com/entry/2018/02/10/104607
# https://weblabo.oscasierra.net/python/python3-beginning-file-list.html
# https://qiita.com/ytsumura/items/917de811c023ee9f3709
# https://uxmilk.jp/8680

import tkinter as tk
from PIL import Image, ImageTk
import glob

### ここにイベントが発生したときの処理 ###
pressed_x = pressed_y = 0
item_id = -1
def pressed(event):
    global pressed_x, pressed_y, item_id
    item_id = canvas.find_closest(event.x, event.y)
    tag = canvas.gettags(item_id[0])[0]
    item = canvas.type(tag)
    #print(item)
    #print(tag)
    pressed_x = event.x
    pressed_y = event.y

def dragged(event):
    global pressed_x, pressed_y, item_id
    item_id = canvas.find_closest(event.x, event.y)
    tag = canvas.gettags(item_id[0])[0]
    item = canvas.type(tag) # rectangle image
    delta_x = event.x - pressed_x
    delta_y = event.y - pressed_y
    if item == "rectangle":
        x0, y0, x1, y1 = canvas.coords(item_id)
        canvas.coords(item_id, x0+delta_x, y0+delta_y, x1+delta_x, y1+delta_y)
    else:
        x, y = canvas.coords(item_id)
        canvas.coords(item_id, x+delta_x, y+delta_y)
    pressed_x = event.x
    pressed_y = event.y

def image_open(image_name):
    width = 200
    img = Image.open(image_name)
    resize_image = img.resize((width, int(width * img.size[1] / img.size[0])))  # 画像のリサイズ
    return resize_image

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack(expand = True)

image_names = glob.glob("./images/*")

postion = 200

for i, image_name in enumerate(image_names):
    postion += 20
    tag_name = "img" + str(i)
    tkimg = "tkimg_" + str(i)

    ### 画像 ###
    img = image_open(image_name)
    # tkimg = ImageTk.PhotoImage(img)
    exec('{} = ImageTk.PhotoImage(img)'.format(tkimg))
    # canvas.create_image(postion, postion, image=tkimg, tags=tag_name)
    exec('canvas.create_image(postion, postion, image={}, tags=tag_name)'.format(tkimg))

    ### ここにオブジェクトとイベントを結びつける ###
    # クリックされたとき
    canvas.tag_bind(tag_name, "<ButtonPress-1>", pressed)

    # ドラッグされたとき
    canvas.tag_bind(tag_name, "<B1-Motion>", dragged)

root.mainloop()