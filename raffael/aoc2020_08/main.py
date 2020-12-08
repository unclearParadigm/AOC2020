import time

start = time.time()
with open('aoc2020_08_input.txt', 'r') as f:
    commands = f.read().split('\n')

commands = [[cmd.split()[0], int(cmd.split()[1])] for cmd in commands if cmd != '']
print('reading + parsing took {0}s'.format(time.time() - start))


def execute(all_commands: list) -> (int, bool):
    accumulator = 0
    instruction_counter = 0
    executed_instructions = set()
    while instruction_counter < len(all_commands) and instruction_counter not in executed_instructions:
        executed_instructions.add(instruction_counter)
        command, number = all_commands[instruction_counter]
        if command == 'acc':
            accumulator += number
        elif command == 'jmp':
            instruction_counter += number - 1
        instruction_counter += 1
    return accumulator, instruction_counter == len(all_commands)


def execute_mod(instruction_counter, command) -> bool:
    previous_ic = commands[instruction_counter][0]
    commands[instruction_counter][0] = command
    accumulator, done = execute(commands)
    commands[instruction_counter][0] = previous_ic
    return accumulator if done else False


def part2(program) -> int:
    accumulator = False
    nop_instruction_indices = [pc for pc, (instruction, _) in enumerate(program) if instruction == 'nop']
    jmp_instruction_indices = [pc for pc, (instruction, _) in enumerate(program) if instruction == 'jmp']

    for jmp in jmp_instruction_indices:
        accumulator = accumulator or execute_mod(jmp, 'nop')
    for nop in nop_instruction_indices:
        accumulator = accumulator or execute_mod(nop, 'jmp')
    return accumulator


start = time.time()
p1 = execute(commands)[0]
print('Part 1:', p1, 'took {0}s'.format(time.time() - start))
start = time.time()
p2 = part2(commands)
print('Part 2:', p2, 'took {0}s'.format(time.time() - start))
