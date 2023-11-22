import os
from src.bgrem.components.remove_bg import BG_REM
import PIL
from PIL import Image

class BG_REMOVER():
    def __init__(self):
        self.opt = None
        self.bgrem_model = BG_REM()

    def setInput(self, filename):
        self.filename = filename
    
    def main(self, save_dir, only_mask=False):
        self.img = Image.open(self.filename)
        self.foreground = self.bgrem_model.remove_background(self.img, only_mask=only_mask)
        save_prefix = os.path.basename(self.filename).split('.')[0]+'-bg.png'
        savename = os.path.join(save_dir, save_prefix)
        self.foreground.save(savename)
        return save_prefix