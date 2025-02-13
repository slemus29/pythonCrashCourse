import this

messaje = "Hello Python word!"
print(messaje)

messaje = "Hello Python Crash Course world"
print(messaje)

name = "ada lovelace"
print (name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
# f-strings format strings
full_name = f"{first_name} {last_name}"

print(full_name)

messaje = f"Hello {full_name.title()}!"
print(messaje)

# tabs or Newlines

print("\tPython")
print("languages: \nPython\nC\nJavascript")
print("languages: \n\tPython\n\tC\n\tJavascript")

# stripping whitespace

favorite_language = "   python  "
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#removing prefixes

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

#avoiding syntax errors

print("One of Python's strengths is its diverse community")

