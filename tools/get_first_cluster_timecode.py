
from ebml.utils.ebml_data import *

import sys

if __name__ == '__main__':
    ebml_obj = EBMLData(sys.argv[-1])
    print ebml_obj.get_first_cluster_timecode()





