
import base64
import os
import shutil

import PIL
import requests


def draw_infra_points(
    self,
    save: str | None = None,
) -> PIL.PngImagePlugin.PngImageFile:
    """Use mermaid.js to display the infra as a graph of specificpoints

    Parameters
    ----------
    save : str | None, optional
        File name to save image, by default None

    Returns
    -------
    PIL.Image
        Inmage of the infra as a graph of points
    """

    g = 'graph LR;'

    points_all_tracks = self.points_on_track_sections(op_part_tracks=True)
    for _, points in points_all_tracks.items():
        for i, _ in enumerate(points[:-1]):
            g += (f"{points[i].id}<-->{points[i+1].id};")

    graphbytes = g.encode("ascii")
    base64_bytes = base64.b64encode(graphbytes)
    base64_string = base64_bytes.decode("ascii")
    url = "https://mermaid.ink/img/" + base64_string

    response = requests.get(url, stream=True)

    with open('tmp.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    image = PIL.Image.open('tmp.png')

    if save:
        os.rename('tmp.png', save)
    else:
        os.remove('tmp.png')

    return image
