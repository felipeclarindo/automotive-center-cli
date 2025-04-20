def validate_string_input(user_input: str) -> bool:
    """
    Validate if the user_input is a string and not empty.

    Args:
        user_input (str): The input string to validate.

    Raises:
        ValueError: If the input is not a string or is empty.

    Returns:
        bool: True if the input is a valid string, False otherwise.
    """
    try:
        validation = False
        user_input = user_input.strip()
        if len(user_input) > 0:
            if not user_input.isalpha():
                raise ValueError("Valor invalido!")
            else:
                validation = True
        else:
            raise ValueError("O valor não pode ser vazio!")
        return validation
    except Exception as e:
        print(e)
    return False


def validate_exit(confirm: str) -> bool:
    """
    Validate if the input is a confirmation string for exit.

    Args:
        confirm (str): The input string to validate.

    Raises:
        ValueError: If the input is not a valid confirmation string.

    Returns:
        bool: True if the input is a valid confirmation string, False otherwise.
    """
    try:
        validation = False
        confirm = confirm.strip().replace(" ", "")
        if len(confirm) == 0:
            raise ValueError("O valor não pode ser vazio!")
        else:
            validation = (
                True
                if confirm.isalpha()
                and confirm.lower() in ["s", "n", "sim", "nao", "não"]
                else False
            )
            if not validation:
                raise ValueError("Valor invalido!")
        return validation
    except Exception as e:
        print(e)
    return False
