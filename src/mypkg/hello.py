def greet(name: str) -> str:
    """Вернёт приветствие для пользователя.

    Args:
        name: Имя пользователя.

    Returns:
        Строка вида "Hello, <name>!".

    Examples:
        >>> greet("Tatiana")
        'Hello, Tatiana!'
    """
    return f"Hello, {name}!"
