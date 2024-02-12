def reverse_string(inout_string):
    if len(inout_string) <= 1:
        return inout_string
    else:
        return reverse_string(inout_string[1:]) + inout_string[0]

input_string = "Hello Oleg"
print("Inverted line:", reverse_string(input_string))