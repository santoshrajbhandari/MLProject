import os
import sys
import dill

import numpy as np
import pandas as pd
from.exception import CustomException

def save_object(file_path, obj):
    """
    Save the object to a file using pickle.
    """
    try:
        import pickle
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)