#!/usr/bin/bash

# Get image paths as an array
image_paths=($(find UFDD_val/images -type f -and -not -wholename '*labelled*'))

# Run the detection algorithm on each of them
for image_path in ${image_paths[@]};
do
    ./face.sif ${image_path}
done
