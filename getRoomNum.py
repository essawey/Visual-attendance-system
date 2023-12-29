def getRoomNum():
    try:
        with open('SYSTEM_ID.txt', 'r') as file:
            system_id_char = file.read(1)

            # Check if the file is empty
            if not system_id_char:
                raise ValueError("SYSTEM_ID.txt is empty")

        # Convert the character to an integer
        system_id_int = int(system_id_char)

        return system_id_int

    except FileNotFoundError:
        raise FileNotFoundError("SYSTEM_ID.txt not found")

    except ValueError as ve:
        raise ValueError(f"Error reading SYSTEM_ID.txt: {ve}")

    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
