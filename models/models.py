from pydantic import Field, field_validator, BaseModel, ValidationInfo
import csv
from typing import Optional, List, Tuple, Union
import re


class ModelData(BaseModel):
    model_type: str = Field(..., alias="Model Type")
    model: str = Field(..., alias="Model")
    input_per_1m_tokens: Optional[float | str] = Field(
        None, alias="Input per 1M tokens"
    )
    input_per_1k_tokens: Optional[float | str] = Field(
        None, alias="Input per 1K tokens"
    )
    input_per_token: Optional[float | str] = Field(None, alias="Input per token")
    output_per_1m_tokens: Optional[float | str] = Field(
        None, alias="Output per 1M tokens"
    )
    output_per_1k_tokens: Optional[float | str] = Field(
        None, alias="Output per 1K tokens"
    )
    output_per_token: Optional[float | str] = Field(None, alias="Output per token")
    training_per_1m_tokens: Optional[float | str] = Field(
        None, alias="Training per 1M tokens"
    )
    training_per_1k_tokens: Optional[float | str] = Field(
        None, alias="Training per 1K tokens"
    )
    training_per_token: Optional[float | str] = Field(None, alias="Training per token")
    usage_per_1m_tokens: Optional[Union[float, str]] = Field(
        None, alias="Usage per 1M tokens"
    )
    usage_per_1k_tokens: Optional[Union[float, str]] = Field(
        None, alias="Usage per 1K tokens"
    )
    usage_per_token: Optional[Union[float, str]] = Field(None, alias="Usage per token")
    usage_unit: Optional[str] = None

    @field_validator(
        "input_per_1m_tokens",
        "input_per_1k_tokens",
        "input_per_token",
        "output_per_1m_tokens",
        "output_per_1k_tokens",
        "output_per_token",
        "training_per_1m_tokens",
        "training_per_1k_tokens",
        "training_per_token",
    )
    @classmethod
    def extract_cost_and_unit(cls, v):
        # print(v, "v")
        if v is None or v == "-" or str(v) == "":
            return None
        cost_unit_re = re.compile(r"([\d.]+)\s*/\s*(.*)")
        match = cost_unit_re.match(v)
        if match:
            print(match.groups()[0], "match.groups()[0]")
            return match.groups()[0]
        return float(v)

    @field_validator(
        "usage_per_1m_tokens",
        "usage_per_1k_tokens",
        "usage_per_token",
        check_fields=True,
    )
    @classmethod
    def set_usage_unit(cls, v, info: ValidationInfo):
        if "usage_unit" in info.data or v is None:
            return v
        cost_unit_re = re.compile(r"([\d.]+)\s*/\s*(.*)")
        match = cost_unit_re.match(v)
        if match:
            info.data["usage_unit"] = match.groups()[1]
            return match.groups()[0]
        return v


def read_csv_data(filepath: str) -> List[ModelData]:
    data = []
    with open(filepath, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            model_data = ModelData.model_validate(row)
            data.append(model_data)
    return data


# Example usage
# filepath = 'your_csv_file_path_here.csv'
# model_data_list = read_csv_data(filepath)
# for model_data in model_data_list:
#     print(model_data)
