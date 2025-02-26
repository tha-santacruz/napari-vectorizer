import numpy as np

from napari_vectorizer._widget import (
    threshold_magic_widget,
)


def test_threshold_autogenerate_widget():
    # because our "widget" is a pure function, we can call it and
    # test it independently of napari
    im_data = np.random.random((100, 100))
    thresholded = threshold_autogenerate_widget(im_data, 0.5)
    assert thresholded.shape == im_data.shape
    # etc.


# make_napari_viewer is a pytest fixture that returns a napari viewer object
# you don't need to import it, as long as napari is installed
# in your testing environment
def test_threshold_magic_widget(make_napari_viewer):
    viewer = make_napari_viewer()
    layer = viewer.add_image(np.random.random((100, 100)))

    # our widget will be a MagicFactory or FunctionGui instance
    my_widget = threshold_magic_widget()

    # if we "call" this object, it'll execute our function
    thresholded = my_widget(viewer.layers[0], 0.5)
    assert thresholded.shape == layer.data.shape
    # etc.