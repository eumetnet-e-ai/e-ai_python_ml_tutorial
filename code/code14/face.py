#!/usr/bin/env python3
from fdlite import FaceDetection, FaceDetectionModel
from fdlite.render import Colors, detections_to_render_data, render_to_image

import PIL
import typer
import pathlib


def detect_faces(image: PIL.Image):
    detect_faces = FaceDetection(model_type=FaceDetectionModel.BACK_CAMERA)
    faces = detect_faces(image)
    print(f"Found {len(faces)} faces")
    return faces


def mark_faces(image_filename: pathlib.Path):
    """Mark all faces recognized in the image"""
    image = PIL.Image.open(image_filename)

    faces = detect_faces(image)

    # Draw faces
    render_data = detections_to_render_data(
        faces, bounds_color=Colors.GREEN, line_width=3
    )
    render_to_image(render_data, image)

    image.save(image_filename.with_suffix(".out.jpg"))


if __name__ == "__main__":
    typer.run(mark_faces)
