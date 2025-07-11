#!/usr/bin/bash

#SBATCH --qos=nf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --time=05:00
#SBATCH --output=%x.out

# Set the environment
module load apptainer
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}

# Get image paths as an array
image_paths=($(find UFDD_val/images -type f -and -not -wholename '*labelled*'))

# Run the detection algorithm on each of them
for image_path in ${image_paths[@]};
do
    ./face.sif ${image_path}
done
