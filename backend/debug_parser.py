from langchain_core.output_parsers import JsonOutputParser
from models import QuizOutput

# Test if JsonOutputParser can be created with QuizOutput
try:
    parser = JsonOutputParser(pydantic_object=QuizOutput)
    print("JsonOutputParser created successfully!")
    print("Format instructions:")
    print(parser.get_format_instructions())
except Exception as e:
    print(f"Error creating JsonOutputParser: {e}")