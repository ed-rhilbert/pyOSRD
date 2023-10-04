import os

import PIL


def test_point_switch_infra_draw_infra_returns_image(use_case_point_switch):
    image = use_case_point_switch.draw_infra_points()
    assert isinstance(image, PIL.JpegImagePlugin.JpegImageFile)


def test_point_switch_infra_draw_infra_save(use_case_point_switch):
    use_case_point_switch.draw_infra_points(save='image.png')
    assert os.path.exists('image.png')
    os.remove('image.png')
