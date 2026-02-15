import sys
import os
print(f"Current working directory: {os.getcwd()}")
print(f"System path: {sys.path}")

try:
    import clothing
    print(f"Successfully imported clothing from {clothing.__file__}")
    from clothing.exception import CustomException
    print("Successfully imported CustomException")
except ImportError as e:
    print(f"Import failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
