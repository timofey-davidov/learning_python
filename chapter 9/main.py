import asyncio

# Список поваров.
chef_list = ['', 'Франсуа', 'Жан', 'Марсель']


async def cook_order(order_number, dish):
    # Повар готовит блюдо
    print(f"Повар {chef_list[order_number]} начинает готовить заказ №{order_number}: {dish}")
    await asyncio.sleep(order_number*2)  # Имитация времени на готовку
    print(f"Заказ №{order_number}: {dish} готов!")


async def serve_order(order_number, dish):
    # Официант подает блюдо
    await cook_order(order_number, dish)
    print(f"Официант подает {dish}")


async def manager():
    # Менеджер (событийный цикл) назначает задачи
    orders = [(3, 'Салат'), (2, 'Стейк'), (1, 'Суп')]
    tasks = [asyncio.create_task(serve_order(order_number, dish)) for order_number, dish in orders]

    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks)


# Запуск событийного цикла
asyncio.run(manager())