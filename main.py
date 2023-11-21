import os

from src.bgrem.pipeline.BGREM_pipeline import BG_REMOVER
from src.bgrem import logger

STAGE_NAME = "BACKGROUND REMOVAL"
try:
    logger.info(f"****************************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = BG_REMOVER()
    filename = r"H:\projects\uiuxstuff\images\image3.png"
    obj.setInput(filename)
    obj.main(save_dir='./')
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nX-------------------------------------------------X")
except Exception as e:
    logger.exception(e)
    raise e