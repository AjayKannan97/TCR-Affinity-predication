#!/bin/bash

#SBATCH -p htc
#SBATCH -N 1                        # number of compute nodes
#SBATCH -n 1                        # number of tasks your job will spawn
#SBATCH --mem=4G                    # amount of RAM requested in GiB (2^40)
#SBATCH -q wildfire                 # Run job under wildfire QOS queue
#SBATCH --gres=gpu:2                # Request two GPUs
#SBATCH -t 0-12:00                  # wall time (D-HH:MM)
#SBATCH -o slurm.%j.out             # STDOUT (%j = JobId)
#SBATCH -e slurm.%j.err             # STDERR (%j = JobId)
#SBATCH --mail-type=ALL             # Send a notification when a job starts, stops, or fails
#SBATCH --mail-user=myemail@asu.edu # send-to address
...
module purge    
# Load required modules for job's environment
module load anaconda/py3

python datagen_neg.py
...