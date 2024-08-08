calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        if string.lower() == item.lower():
            return True
    return False


print(string_info("CarMen"))
print(is_contains("Moscow", ["London", "Paris", "Tokio"]))
print(is_contains("яблоко", ["ананас", "яблоко", "гранат"]))
print(string_info("Hello, Teacher!"))
print(is_contains("TEACHER", ["master", "chef", "sir", "lord"]))
print(string_info("Ragnarok"))

print(f"Количество вызовов: {calls}")
