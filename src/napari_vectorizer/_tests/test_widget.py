import numpy as np

from napari_vectorizer._widget import (
    label_vectorization_widget,
)


# make_napari_viewer is a pytest fixture that returns a napari viewer object
# you don't need to import it, as long as napari is installed
# in your testing environment
def test_label_vectorization_widget(make_napari_viewer):
    pass
    #viewer = make_napari_viewer()
    #layer = viewer.add_image(np.random.random((100, 100)))

    # our widget will be a MagicFactory or FunctionGui instance
    #my_widget = label_vectorization_widget()

    # if we "call" this object, it'll execute our function
    #thresholded = my_widget(viewer.layers[0], 0.5)
    #assert thresholded.shape == layer.data.shape
    # etc.