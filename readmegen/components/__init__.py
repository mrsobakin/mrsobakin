from readmegen.components import stack

def unclickable_img(src: str, tags: str) -> str:
    return f"""<picture><source media="(prefers-color-scheme: dark)" srcset="{src}"><source media="(prefers-color-scheme: light)" srcset="{src}"><img src="{src}" {tags}></picture>"""
