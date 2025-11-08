from pydantic import BaseModel
from models import QuizOutput

# Check if QuizOutput is a subclass of BaseModel
print(f"QuizOutput is subclass of BaseModel: {issubclass(QuizOutput, BaseModel)}")

# Check the MRO (Method Resolution Order)
print(f"QuizOutput MRO: {QuizOutput.__mro__}")

# Try to create an instance of QuizOutput
try:
    # This should work if QuizOutput is properly defined
    instance = QuizOutput(
        title="Test",
        summary="Test summary",
        key_entities={"people": [], "organizations": [], "locations": []},
        sections=[],
        quiz=[],
        related_topics=[]
    )
    print("QuizOutput instance created successfully!")
except Exception as e:
    print(f"Error creating QuizOutput instance: {e}")