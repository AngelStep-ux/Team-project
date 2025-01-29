import random

def get_suggestions(vk, user_id):
    # Получаем список пользователей на основе заданных критериев
    users = vk.users.search(age_from=18, age_to=30, count=5)
    suggestions = []
    
    for user in users['items']:
        suggestions.append({
            'id': user['id'],
            'name': f"{user['first_name']} {user['last_name']}"
        })
    
    return suggestions

def get_vk_session(token):
    # Здесь должна быть реализация функции для получения сессии VK
    pass

def get_suggestions(vk, user_id):
    # Здесь должна быть реализация функции для получения предложений
    pass

def main():
    token = "L4aESTSEH03zX9iMp3NlvSOzhfCTJ9-grFghqPl0xq1TCAp1er3SUTYNanmktUVW1BFQqRkHYm9wX3fOKxJzTCGHkjqh7Qq-DKeqIIP7ueGux0SlfjEx16Z5RAa1AioDh6bP6XgJ_pGHFSWyF0y8Q"  # Замените на ваш токен
    vk = get_vk_session(token)
    
    user_id = 123456  # Замените на ID пользователя, с которым будет взаимодействовать бот
    while True:
        user_input = input("Хотите познакомиться с кем-то? (да/нет): ")
        if user_input.lower() == 'да':
            suggestions = get_suggestions(vk, user_id)
            for suggestion in suggestions:
                print(f"Вам может понравиться: {suggestion['name']} (ID: {suggestion['id']})")
        elif user_input.lower() == 'нет':
            print("Хорошо, если передумаете, дайте знать!")
            break  # Добавлено, чтобы выйти из цикла при ответе 'нет'
        else:
            print("Пожалуйста, ответьте 'да' или 'нет'.")

if __name__ == "__main__":
    main()