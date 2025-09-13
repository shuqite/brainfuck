## BRAINFUCK on RUST and PYTHON

RUST READY:
- [ ] CLI
- [ ] I / O ( , / . )
- [ ] + / -
- [ ] Cycles ( '[]' )
- [ ] > / <

PYTHON READY:
- [x] CLI
- [ ] - [ ] I / O ( , / . )
- [ ] + / -
- [ ] Cycles ( '[]' )
- [ ] > / <

INSTALL:
```sh
git clone https://github.com/shuqite/brainfuck
```

TO RUN RUST:
```sh
cd brainfuck/brainfuck-rust
cargo run
```

TO RUN PYTHON:
```sh
cd brainfuck/brainfuck-python
python brainfuck.py
```

## GUIDE TO USE BRAINFUCK

- `+` - increases current slot by 1
- `-` - reduses current slot by 1
- `.` - output slot (if u use . more then one time output will be summed)
- `,` - input number to current slot
- `>` - change slot up
- `<` - change slot down
- `[]` - cycles (infinite cycle, that breaks when swithching to zero slot)
- `start` - start command
