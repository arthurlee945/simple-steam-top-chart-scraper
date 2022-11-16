import numpy as np
import pyautogui as pg

class DinoPyAuto:
    def start_autoplay(self):
        pg.click((1575, 45))
        pg.press("space")
        pos_1 = (1375, 640)
        pos_2 = (80, 40)
        while True:
            image = pg.screenshot(region=pos_1 + pos_2).convert("L")
            if self.location_calc(screenshot=image):
                pg.press("space")
                pg.press("space")
                pg.press("space")

    def location_calc(self, screenshot) -> bool:
        if np.amin(np.array(screenshot)) == 83:
            return True
        return False

if __name__ == "__main__":
    DinoPyAuto().start_autoplay()
