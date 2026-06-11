class Node:

    def __init__(self, value):
        self.value = value  
        self.left = None  
        self.right = None  


class BST:

    def __init__(self):
        self.root = None

    def insert(self, value): 
        if self.root is None:
            self.root = Node(value)
            print(f"Значение {value} добавлено как корень дерева")
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Рекурсивная вставка значения"""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                print(f"Значение {value} добавлено")
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                print(f"Значение {value} добавлено")
            else:
                self._insert_recursive(node.right, value)
        else:
            print(f"Значение {value} уже есть в дереве!")

    def search(self, target):
        return self._search_recursive(self.root, target)

    def _search_recursive(self, node, target):
        if node is None:
            return False
        if target == node.value:
            return True
        elif target < node.value:
            return self._search_recursive(node.left, target)
        else:
            return self._search_recursive(node.right, target)

    def inorder(self):
        if self.root is None:
            print("Дерево пустое!")
            return []

        result = []
        self._inorder_recursive(self.root, result)

        print("Значения в порядке возрастания:")
        print(" -> ".join(map(str, result)))
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)  # корень
            self._inorder_recursive(node.right, result)

    def find_kth_min(self, k):
        if self.root is None:
            print("Дерево пустое!")
            return None

        result = []
        self._inorder_recursive(self.root, result)

        if k < 1 or k > len(result):
            print(f"Ошибка! В дереве {len(result)} элементов. k должно быть от 1 до {len(result)}")
            return None

        print(f"{k}-й по величине элемент: {result[k - 1]}")
        return result[k - 1]


# Создаём дерево
bst = BST()

# Главный цикл с меню
while True:
    # Показываем меню
    print("\n" + "=" * 50)
    print("БИНАРНОЕ ДЕРЕВО ПОИСКА")
    print("=" * 50)
    print("1. Вставить значение (insert)")
    print("2. Найти значение (search)")
    print("3. Вывести все значения в порядке возрастания (inorder)")
    print("4. Найти k-й по величине элемент (k-й минимум)")
    print("0. Выход")
    print("=" * 50)

    choice = input("Выберите действие: ")

    if choice == "1":
        print("\n--- Вставка значения ---")
        try:
            value = int(input("Введите целое число для вставки: "))
            bst.insert(value)
        except ValueError:
            print("Ошибка! Введите целое число.")

    elif choice == "2":
        print("\n--- Поиск значения ---")
        if bst.root is None:
            print("Дерево пустое! Сначала добавьте значения.")
        else:
            try:
                target = int(input("Введите число для поиска: "))
                if bst.search(target):
                    print(f"Значение {target} НАЙДЕНО в дереве!")
                else:
                    print(f"Значение {target} НЕ НАЙДЕНО в дереве!")
            except ValueError:
                print("Ошибка! Введите целое число.")

    elif choice == "3":
        print("\n--- Вывод всех значений ---")
        bst.inorder()

    elif choice == "4":
        print("\n--- Поиск k-го минимума ---")
        if bst.root is None:
            print("Дерево пустое! Сначала добавьте значения.")
        else:
            try:
                k = int(input("Введите номер k (1, 2, 3...): "))
                bst.find_kth_min(k)
            except ValueError:
                print("Ошибка! Введите целое число.")

    elif choice == "0":
        print("До свидания!")
        break

    else:
        print("Неверный ввод! Пожалуйста, выберите пункт от 0 до 4")
