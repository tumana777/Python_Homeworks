'''
დაწერეთ ფუნქცია, რომელიც უბრალოდ აბრუნებს არგუმენტად გადაწოდებულ რიცხვს, დაუწერეთ დეკორატორი, რომელიც 
შეამოწმებს, რომ რიცხვი უნდა იყოს დადებითი, თუ არის უარყოფითი ამ შემთხვევაში დააბრუნეთ ValueError შესაბამისი ტექსტით, 
სხვა შემთხვევაში აამოქმედეთ ფუნქცია, შედეგი კი დაბეჭდეთ დეკორატორიდან 
'''
def decorator(func):
    def wrapper(*args, **kwargs):
        num = args[0]
        if num > 0:
            print(func(num))
        else:
            raise ValueError('Please, input positive number!')
    return wrapper


@decorator
def simple_func(n):
    return n

simple_func(5)