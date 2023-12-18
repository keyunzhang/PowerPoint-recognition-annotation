from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class PptDataset(BaseSegDataset):
    # 类别和对应的 RGB配色
    METAINFO = {
        'classes':['Title', 'Subtitle', 'Text', 'Equation', 'Figure'],
        'palette':[[127,127,127], [200,0,0], [0,200,0], [144,238,144], [30,30,30]]
    }
    
    # 指定图像扩展名、标注扩展名
    def __init__(self,
                 seg_map_suffix='.png',   # 标注mask图像的格式
                 reduce_zero_label=False, # 类别ID为0的类别是否需要除去
                 **kwargs) -> None:
        super().__init__(
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)
