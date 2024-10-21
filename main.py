def draw_rectangle(width, height):
    if width < 2 or height < 2:
        print("Width and height must be at least 2.")
        return

    # Top border
    print("|" + "-" * (width - 2) + "|")

    # Middle empty rows
    for _ in range(height - 2):
        print("|" + " " * (width - 2) + "|")

    # Bottom border
    print("|" + "-" * (width - 2) + "|")


# Example usage
draw_rectangle(10, 3)
