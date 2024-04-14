import azure.functions as func
from src.main import bp

# Create a function app instance with the HTTP auth level set to FUNCTION
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
app.register_functions(bp)
