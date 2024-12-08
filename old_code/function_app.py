import azure.functions as func 
from beautifulsoup import bp

app = func.FunctionApp() 

app.register_functions(bp) 