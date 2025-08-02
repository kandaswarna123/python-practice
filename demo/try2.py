class ErrorInCode(Exception):
    def __init__(self,data):
        
        self.data = data 
    def __str__(self):
        return repr(self.data)
try:
    raise ErrorInCode(2000)
except ErrorInCode as e:
    print("Error in code:", e.data)   
finally:
    print("Execution completed.")