def test_function():
    print("я из тест функции")

    # inner_function() Выдает ошибку
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


#inner_function()  # Выдает ошибку
test_function()
