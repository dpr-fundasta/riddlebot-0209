from langchain_core.pydantic_v1 import BaseModel, Field, root_validator
from langchain_core.output_parsers import JsonOutputParser


# Define the CheckOutput model
class CheckOutput(BaseModel):
    結果: str = Field(description="It should be one of ['Correct', 'Incorrect']")
    解説: str = Field(description="Explain the reason for the result shortly")

    @root_validator(pre=True)
    def validate_required_keys(cls, values):
        if "結果" not in values or "解説" not in values:
            raise ValueError("結果と解説は必須項目です。")
        return values


# Initialize JSONParser using CheckOutput
JSONParser = JsonOutputParser(pydantic_object=CheckOutput)


class CheckOutputForHint(BaseModel):
    hint: str = Field(description="It should be a description")
    reason: str = Field(description="Explain the reason for the hint shortly")


# Initialize JSONParser using CheckOutput
JSONParserHint = JsonOutputParser(pydantic_object=CheckOutputForHint)
