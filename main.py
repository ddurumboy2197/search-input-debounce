import time

class SearchInput:
    def __init__(self):
        self.debounce_time = 500  # 500ms
        self.last_call_time = 0

    def debounced_api_call(self, func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            if current_time - self.last_call_time >= self.debounce_time:
                self.last_call_time = current_time
                return func(*args, **kwargs)
        return wrapper

    def search(self, query):
        print(f"Searching for: {query}")

# Foydalanuvchi kirishi uchun input elementi
class SearchInputComponent:
    def __init__(self, search_input):
        self.search_input = search_input
        self.input_element = None

    def render(self):
        self.input_element = input("Kiriting: ")

        # Debounced API call
        self.search_input.debounced_api_call(self.search_input.search)(self.input_element)

    def search(self, query):
        # API call
        print(f"API call: {query}")

# Arxitektura
search_input = SearchInput()
search_input_component = SearchInputComponent(search_input)

# Foydalanuvchi kirishi uchun input elementi
while True:
    search_input_component.render()
```

Kodda `SearchInput` klassi API callni debounced qilish uchun javob beradi. `debounced_api_call` metodida `debounce_time` deb nomlangan o'zgaruvchi API callni 500msdan keyin qayta bajarish uchun javob beradi. `last_call_time` o'zgaruvchisi oxirgi API call vaqti uchun javob beradi. `search` metodida API call qilish uchun javob beradi. `SearchInputComponent` klassi foydalanuvchi kirishi uchun input elementi uchun javob beradi. `render` metodida input elementi uchun kirishni o'qiydi va debounced API callni bajaradi. `search` metodida API call qilish uchun javob beradi.
