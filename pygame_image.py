import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    # バックグラウンドイメージ設定
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_flip = pg.transform.flip(bg_img, True, False)
    # こうかとん 設定
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    # 10度回転
    kk_img_trans = [pg.transform.rotozoom(
        kk_img, 0.1*i, 1.0) for i in range(100)]
    kk_img_trans += [pg.transform.rotozoom(
        kk_img, 0.1*i, 1.0) for i in range(100, 1, -1)]
    # kk_img_list = [kk_img, kk_img_trans]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        x = tmr % 1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_flip, [1600-x, 0])
        if x == 0:
            bg_img = pg.transform.flip(bg_img, True, False)
            bg_img_flip = pg.transform.flip(bg_img_flip, True, False)

        # こうかとん
        screen.blit(kk_img_trans[tmr % 199], [300, 200])
        pg.display.update()
        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
