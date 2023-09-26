import asyncio
import random

colors = (
    "\033[0m",              # end of color sequence
    "\033[38;2;255;0;0m",   # Red
    "\033[38;2;0;255;0m",   # Green
    "\033[38;2;0;0;255m"    # Blue
)

# Create a dict of colors to easily access them
colors_dict = dict(zip(colors, ("end", "Red", "Green", "Blue")))


async def display(index: int, threshold: int = 8) -> int:
    """Display the color and index of the coroutine"""
    print(
        f"{colors[index]} {colors_dict[colors[index]]} "
        f"coroutine started {colors[0]}"
    )
    i = random.randint(0, 10)
    # Run until the random value `i` is greater than the `threshold`
    while i <= threshold:
        print(
            f"{colors[index]} {colors_dict[colors[index]]} "
            f"coroutine value {i} <= {threshold} running {colors[0]}"
        )
        i = random.randint(0, 10)  # reset index
        await asyncio.sleep(i)
    print(
        f"{colors[index]} {colors_dict[colors[index]]} coroutine ended with "
        f"index: {i} > {threshold} {colors[0]}"
    )
    return i


async def main():
    res = await asyncio.gather(
        *(display(index=i) for i in range(1, 4))
    )
    return res


if __name__ == "__main__":
    red, green, blue = asyncio.run(main=main())
    print(f"\nred: {red}, green: {green}, blue: {blue}")
