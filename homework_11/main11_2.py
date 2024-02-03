# დაწერეთ ფუნქცია რომელიც ატრიბუტად მიიღებს ორ tuple ტიპის მონაცემს, ფუნქციამ უნდა გააერთიანოს ეს ორი tuple 
# და დააბრუნოს ერთი მთლიანი დუბლიკატების გარეშე, შექმენით სია duplicated_values და მასში დაამატეთ ის ინფორმაცია 
# მხოლოდ ერთხელ, რომელიც დუბლირებული სახით გვხვდება tuple-ში, დაბეჭდეთ მოცემული სია

def united(t1, t2):
    return tuple(set(t1 + t2))

def duplicated(t1, t2):
    return list(set(t1).intersection(set(t2)))

tuple1 = (1,2,3,4,5,6)
tuple2 = (4,5,5,6,6,7)

combined_tuple = united(tuple1, tuple2)
duplicated_values = duplicated(tuple1, tuple2)

print(combined_tuple)
print(duplicated_values)


