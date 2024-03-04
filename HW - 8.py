import heapq


def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)  # Перетворення списку кабелів у купу
    connection_order = []  # Зберігає порядок об'єднання кабелів
    total_cost = 0

    while len(cables) > 1:
        # Обираємо два найменші кабелі
        cable_min_1 = heapq.heappop(cables)
        cable_min_2 = heapq.heappop(cables)

        # Об'єднуємо їх та додаємо витрати до загальних
        current_cost = cable_min_1 + cable_min_2
        total_cost += current_cost
        connection_order.append((cable_min_1, cable_min_2, current_cost))

        # Додаємо новий кабель до купи
        heapq.heappush(cables, current_cost)

    return total_cost, connection_order


# Приклад використання:
cable_lengths = [4, 1, 2, 9, 6, 8, 3]
total_cost, order = min_cost_to_connect_cables(cable_lengths)

for i, (cable_min_1, cable_min_2, current_cost) in enumerate(order, start=1):
    print(
        f"Крок {i}: Об'єднання кабелів {cable_min_1} та {cable_min_2}, Витрати: {current_cost}")

print(f"\nЗагальні витрати: {total_cost}")
