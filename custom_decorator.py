def custom_decorator(original_function):
    def wrap_function():
        print('Before original function work')
        original_function()
        print('After original function work')

    return wrap_function


@custom_decorator
def function_for_decorator():
    print('Function for decorator')


if __name__ == "__main__":
    print('Test Custom Decorator')
    function_for_decorator()
