from pydantic import Field, field_validator, BaseModel, validator
import csv
from typing import Optional, List, Tuple, Union
import re


class ModelData(BaseModel):
    model_type: str
    model: str
    input_per_1m_tokens: Optional[float] = Field(None, alias="Input per 1M tokens")
    input_per_1k_tokens: Optional[float] = Field(None, alias="Input per 1K tokens")
    input_per_token: Optional[float] = Field(None, alias="Input per token")
    output_per_1m_tokens: Optional[float] = Field(None, alias="Output per 1M tokens")
    output_per_1k_tokens: Optional[float] = Field(None, alias="Output per 1K tokens")
    output_per_token: Optional[float] = Field(None, alias="Output per token")
    training_per_1m_tokens: Optional[float] = Field(
        None, alias="Training per 1M tokens"
    )
    training_per_1k_tokens: Optional[float] = Field(
        None, alias="Training per 1K tokens"
    )
    training_per_token: Optional[float] = Field(None, alias="Training per token")
    usage_per_1m_tokens: Optional[Union[float, str]] = Field(None, alias="Usage per 1M tokens")
    usage_per_1k_tokens: Optional[Union[float, str]]= Field(None, alias="Usage per 1K tokens")
    usage_per_token: Optional[Union[float, str]]= Field(None, alias="Usage per token")
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
        pre=True,
    )
    def extract_cost_and_unit(cls, v):
        if v is None or v == "-":
            return None
        cost_unit_re = re.compile(r"([\d.]+)\s*/\s*(.*)")
        match = cost_unit_re.match(v)
        if match:
            return match.groups()[0]
        return v

    @field_validator(
        "usage_per_1m_tokens",
        "usage_per_1k_tokens",
        "usage_per_token",
        check_fields=True,
    )
    def set_usage_unit(cls, v, values, field):
        if "usage_unit" in values or v is None:
            return v
        cost_unit_re = re.compile(r"([\d.]+)\s*/\s*(.*)")
        match = cost_unit_re.match(v)
        if match:
            values["usage_unit"] = match.groups()[1]
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
