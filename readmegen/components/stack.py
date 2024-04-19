from typing import Any
from collections.abc import Mapping
from pathlib import Path


ICONS = Path("./assets/")


def _link(base: str, link: str) -> str:
    return f"""<a href="{link}">{base}</a>"""


def _icon_img(icon: Path, alt: str, tooltip: str) -> str:
    if not icon.exists():
        raise ValueError(f"""The icon "{icon}" does not exist.""")

    return f"""<img src="{icon}" alt="{alt}" title="{tooltip}" height="32">"""


def _icon_themed(light_icon: Path, dark_icon: Path, alt: str, tooltip: str) -> str:
    base = _icon_img(dark_icon, alt, tooltip)

    if not light_icon.exists():
        raise ValueError(f"""The icon "{light_icon}" does not exist.""")

    return f"""<picture><source media="(prefers-color-scheme: dark)" srcset="{dark_icon}"><source media="(prefers-color-scheme: light)" srcset="{light_icon}">{base}</picture>"""


def _icon(icon: Path, alt: str, tooltip: str) -> str:
    return _icon_themed(icon, icon, alt, tooltip)


def generate(stack: Mapping[str, Any]) -> str:
    component = """<div id="tools">"""

    for tool, info in stack.items():
        name, desc = info["name"], info.get("description")

        if not desc:
            tooltip = name
        else:
            tooltip = "\n".join([name, desc])

        use_themed_icons = "themed_icons" in info and info["themed_icons"]

        icon = ICONS / f"{tool}.svg"
        if use_themed_icons:
            icon_light = ICONS / f"{tool}_light.svg"
            base = _icon_themed(icon_light, icon, name, tooltip)
        else:
            base = _icon(icon, name, tooltip)

        if "link" in info:
            link = info["link"]
            component += _link(base, link)
        else:
            component += base

        component += "\n"

    component += """</div>\n"""
    # component += """<div align="right"><sub>(<i>Hover on the icons to get more info</i> 😉)</sub></div>"""

    return component
