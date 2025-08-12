from mcp_server.data_models.base import SharedBaseModel
from pydantic import Field
from typing import List


class ExampleToolRequest(SharedBaseModel):
    array: List[int] = Field(
        description="Unsorted array of integers to be sorted.",
        example=[5, 3, 8, 1, 2],
    )


class ExampleToolResponse(SharedBaseModel):
    sorted_array: List[int] = Field(
        description="Sorted array of integers.",
        example=[1, 2, 3, 5, 8],
    )


class ExternalToolRequest(SharedBaseModel):
    array: List[int] = Field(
        description="Unsorted array of integers to be sorted.",
        example=[5, 3, 8, 1, 2],
    )


class ExternalToolResponse(SharedBaseModel):
    sorted_array: List[int] = Field(
        description="Sorted array of integers returned from the external API.",
        example=[1, 2, 3, 5, 8],
    )
