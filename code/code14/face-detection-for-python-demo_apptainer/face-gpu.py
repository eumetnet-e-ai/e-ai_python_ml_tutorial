#!/usr/bin/env python3
from fdlite import FaceDetection, FaceDetectionModel
from fdlite.render import Colors, detections_to_render_data, render_to_image

import PIL
import typer
import pathlib

import onnxruntime as ort
ort.preload_dlls(cuda=True, cudnn=True)

def detect_faces(image: PIL.Image):

    # Instantiate model with CUDA
    detect_faces = FaceDetection(model_type=FaceDetectionModel.BACK_CAMERA)
    detect_faces.session = ort.InferenceSession(detect_faces.model_path, providers=['CUDAExecutionProvider'])

    # Detect faces & log some output
    faces = detect_faces(image)
    print(f"Found {len(faces)} faces in {image.filename}")

    # Return faces
    return faces

def mark_faces(image_filename: pathlib.Path):
    """Mark all faces recognized in the image"""

    # Open the image & detect faces
    image = PIL.Image.open(image_filename)
    faces = detect_faces(image)

    # Draw faces in a new image
    render_data = detections_to_render_data(
        faces, bounds_color=Colors.GREEN, line_width=3
    )
    render_to_image(render_data, image)

    # Save the new image to a new file
    image.save(image_filename.with_suffix(".labelled.jpg"))


if __name__ == "__main__":
    typer.run(mark_faces)
