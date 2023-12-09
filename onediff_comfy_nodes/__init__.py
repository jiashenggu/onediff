"""OneFlow ComfyUI Speedup Module"""
from ._config import _USE_UNET_INT8
from ._nodes import (
    ModelSpeedup,
    ModelGraphLoader,
    ModelGraphSaver,
    VaeSpeedup,
    VaeGraphLoader,
    VaeGraphSaver,
    ControlNetSpeedup,
    ControlNetGraphLoader,
    ControlNetGraphSaver,
    SVDSpeedup,
)
from ._compare_node import CompareModel, ShowImageDiff


NODE_CLASS_MAPPINGS = {
    "ModelSpeedup": ModelSpeedup,
    "CompareModel": CompareModel,
    "ShowImageDiff": ShowImageDiff,
    "ModelGraphLoader": ModelGraphLoader,
    "ModelGraphSaver": ModelGraphSaver,
    "VaeSpeedup": VaeSpeedup,
    "VaeGraphSaver": VaeGraphSaver,
    "VaeGraphLoader": VaeGraphLoader,
    "ControlNetSpeedup": ControlNetSpeedup,
    "ControlNetGraphLoader": ControlNetGraphLoader,
    "ControlNetGraphSaver": ControlNetGraphSaver,
    "SVDSpeedup": SVDSpeedup,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ModelSpeedup": "Model Speedup",
    "CompareModel": "Model Weight Comparator",
    "ShowImageDiff": "Image Distinction Scanner",
    "ModelGraphLoader": "Model Graph Loader",
    "ModelGraphSaver": "Model Graph Saver",
    "VaeSpeedup": "VAE Speedup",
    "VaeGraphLoader": "VAE Graph Loader",
    "VaeGraphSaver": "VAE Graph Saver",
    "ControlNetSpeedup": "ControlNet Speedup",
    "ControlNetGraphLoader": "ControlNet Graph Loader",
    "ControlNetGraphSaver": "ControlNet Graph Saver",
    "SVDSpeedup": "SVD Speedup",
}

if _USE_UNET_INT8:
    from ._nodes import UNETLoaderInt8

    NODE_CLASS_MAPPINGS.update({"UNETLoaderInt8": UNETLoaderInt8})
    NODE_DISPLAY_NAME_MAPPINGS.update({"UNETLoaderInt8": "UNET Loader Int8"})
