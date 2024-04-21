from textwrap import dedent


def hex2tup(h):
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def colormat(r, g, b):
    return f"{r:g} 0 0 0 0   0 {g:g} 0 0 0   0 0 {b:g} 0 0   0 0 0 1 0".replace("   ", " ")


def gen_filter(colors, bezier, frame_duration, n_frames, offset):
    n_colors = len(colors)

    duration = frame_duration * n_frames * n_colors
    begin = -offset * frame_duration
    matricies = ";".join(colormat(*hex2tup(color)) for color in (colors + [colors[0]]))
    time_points = ";".join(map(lambda x: f"{x:g}", (i / n_colors for i in range(n_colors + 1))))
    beziers = ";".join([bezier] * n_colors)

    return dedent(f"""\
        <filter id="disco">
              <feColorMatrix color-interpolation-filters="sRGB" type="matrix">
                  <animate attributeName="values" values="{matricies}" begin="{begin}ms" dur="{duration}ms" repeatCount="indefinite" calcMode="spline" keyTimes="{time_points}" keySplines="{beziers}"/>
              </feColorMatrix>
        </filter>\
""")


FRAME_DURATION = 80
N_FRAMES = 8

START_COLOR = 1
OFFSET = 6 + (N_FRAMES * START_COLOR)

BEZIER = "0.86,0,0.07,1"
COLORS = ["fb1d2e",
          "ff7b00",
          "ffff00",
          "00ff00",
          "00ffff",
          "2b65f7",
          "ff00ff"]


if __name__ == "__main__":
    print(gen_filter(COLORS, BEZIER, FRAME_DURATION, N_FRAMES, OFFSET))
