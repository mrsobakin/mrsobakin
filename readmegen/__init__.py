from collections.abc import Mapping
from pathlib import Path
import toml

from readmegen import components


print("""<h1 align="center">Sup. <code>@mrsobakin</code>'s here. 👋</h1>""")
print()

print(components.unclickable_img("assets/dogsiftheywerepurple.svg", 'title="Literally me 🐶" height="330px" align="right"'))
print()

print("""## 🤔 Who am I?

- 🦀 Rust enjoyer

- ⚡ Async deadlocks virtuoso

- 🌐 Network protocols enthusiast

- 👾 Reverse <sub><sup>(and forward 😉)</sup></sub> Engineer

- 😎 239% Pretentious

Feel free to contact me on [<img src="assets/telegram.svg" height="16"> Telegram](https://t.me/sbknnn).""")
print()

with open("./stack.toml") as f:
    stack = toml.load(f)

print("## 🔧 Tools that I use: ")
print()

print(components.stack.generate(stack))
