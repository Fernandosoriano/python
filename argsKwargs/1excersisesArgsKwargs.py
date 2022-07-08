# DOC: https://j2logo.com/args-y-kwargs-en-python/
#1.-Python Arbitrary Arguments, ejercicio que hago para practicar el cómo pasar 
# una cantidad indefinida de argumentos a una fucnción
def pruebaParamsInfinitos (*params): # se reciben los params como una tupla
        for i in params:
                print(f"Hola {i}")
pruebaParamsInfinitos('Fernando','Bob','daby','nena', 'joc', 'chow')
# al momento de probar esta función, me salió este error:No module named 'typing_extensions',
# y se solucionó, instalando desde pip lo siguiente: pip install typing-extensions
# que su  doc está en la liga: https://pypi.org/project/typing-extensions/

# la función anterior la hice basado en el siguiente ejemplo:
# que sale de la url: https://www.programiz.com/python-programming/function-argument
def greet(*names):
    """This function greets all
    the person in the names tuple."""
    # names is a tuple with arguments
    #DOC para tuplas que me parece buena: https://ellibrodepython.com/tuplas-python
    for name in names:
        print("Hello", name)
# greet("Monica", "Luke", "Steve", "John")