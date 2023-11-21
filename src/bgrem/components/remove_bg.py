from rembg import remove, new_session
from src.bgrem import logger

class BG_REM():
    def __init__(self):
        self.model_name = 'silueta' 
        # u2net_human_seg
        # u2net_cloth_seg
        # silueta 
        # isnet-anime
        # sam 
        self.session = new_session(self.model_name)

    def remove_background(self, input, only_mask=False): #input PIL image
        output = remove(input, only_mask=only_mask, session=self.session)
        return output
    
