from .blender import BlenderDataset

from .tensoIR_rotation_setting import TensoIR_Dataset_unknown_rotated_lights
from .tensoIR_relighting_test import tensoIR_Relighting_test
from .tensoIR_simple import TensoIR_Dataset_simple
from .tensoIR_material_editing_test import tensoIR_Material_Editing_test
from .tensoIR_general_multi_lights import TensoIR_Dataset_unknown_general_multi_lights
from .tensoIR_nerfactor import TensoIR_Dataset_nerfactor
from .tensoIR_relighting_test_nerfactor import tensoIR_Relighting_test_nerfactor

dataset_dict = {'blender': BlenderDataset,
                'tensoIR_unknown_rotated_lights': TensoIR_Dataset_unknown_rotated_lights,
                'tensoIR_unknown_general_multi_lights': TensoIR_Dataset_unknown_general_multi_lights,
                'tensoIR_relighting_test': tensoIR_Relighting_test,
                'tensoIR_material_editing_test': tensoIR_Material_Editing_test,
                'tensoIR_simple': TensoIR_Dataset_simple,
                'nerfactor': TensoIR_Dataset_nerfactor,
                'nerfactor_relighting': tensoIR_Relighting_test_nerfactor,
                }
