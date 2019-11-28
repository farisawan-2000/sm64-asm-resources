# sm64-asm-resources
Various ASM resources and tools for Super Mario 64, including a **fully labeled disassembly** of the main code segment


# What's Included
## Checksum Area Disassembly
- Based off Frauber's work, this disassembly utilizes the most modern of resources to document, correct, format, and label the disassembled code segment. Function calls are replaced with their respective symbols from the Super Mario 64 [Decompilation Project](https://github.com/n64decomp/sm64), along with various variable names. Additionally, the file can be modified and assembled directly to a Super Mario 64 ROM image with [armips](https://github.com/Kingcom/armips) or its N64-focused [GUI](https://github.com/DavidSM64/SimpleArmipsGui)

## Tools
Various Python tools were developed for this project, including:
- Converting the original checksum_area_11_9.txt file into an assembler-friendly format
- Converting the linker map for Super Mario 64 into an assembler-friendly symbols file
- **MIPSFuncLinker.py** - Converting the above two files into one single file which smartly replaces addresses with their respective function and variable symbols
