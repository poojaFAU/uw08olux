import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
    new_width, new_height = resize
    PIL_image = Image.fromarray(X.astype('uint8'), 'RGB')
    PIL_image = PIL_image.resize((new_width, new_height), Image.ANTIALIAS)
    PIL_image.show()
    pass
    

   