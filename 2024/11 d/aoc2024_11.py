from functools import cache

@cache
def count(stone, blink):
    if blink == 0:
        return 1

    if stone == 0:
        return count(1, blink - 1)

    text = str(stone)

    if len(text) % 2 == 0:
        mid = len(text) // 2

        left = int(text[:mid])
        right = int(text[mid:])

        return (
            count(left, blink - 1)
            + count(right, blink - 1)
        )

    return count(stone * 2024, blink - 1)

stones = [5688, 62084, 2, 3248809, 179, 79, 0, 172169]
print(sum(count(stone, 25)for stone in stones))
print(sum(count(stone, 75)for stone in stones))
