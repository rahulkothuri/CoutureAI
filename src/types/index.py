from typing import TypedDict, Optional

class ClothingDescription(TypedDict):
    color: str
    fabric: str
    style: str
    additional_features: Optional[str]