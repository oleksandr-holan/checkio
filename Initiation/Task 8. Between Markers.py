def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.find(begin) + len(begin) ** (begin in text):text.find(end) + (len(text) + 1) * (not (end in text))]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

assert between_markers("What is >apple<", ">", "<") == "apple"
print(between_markers("<head><title>My new site</title></head>", "<title>", "</title>"))
assert (
        between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
        == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
print(between_markers("No [b]hi", "[b]", "[/b]"))
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
