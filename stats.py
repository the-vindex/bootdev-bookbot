def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Counts the occurrences of each character in a string (case-insensitive).

    Args:
        text: The input string.

    Returns:
        A dictionary where keys are lowercase characters and values are their counts.
    """
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


def prepare_report_data(stats):
    """
    Prepares a sorted list of character counts for reporting.

    Args:
        stats: A dictionary where keys are characters and values are their counts.

    Returns:
        A list of dictionaries, each containing a character and its count, sorted by count in descending order.
    """
    report_data = []
    for char, count in stats.items():
        report_data.append({"char": char, "count": count})
    report_data.sort(key=lambda x: x["count"], reverse=True)
    return report_data
