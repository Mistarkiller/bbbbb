data = "string"
print(hasattr(data, "string"))
print(hasattr(data,"index"))

print(f'!!! {(data.startswish("st")} !!!')

starts = getattr(data, "startswish")



print(type(starts))
