#!/bin/bash
#SBATCH -p condo
#SBATCH -q condo
#SBATCH -A sio141
#SBATCH -N 1 -n 1 -c 16
#SBATCH --mem 16gb
#SBATCH -J SpiecEasi
#SBATCH -t 2-00:00:00
#SBATCH -o grid_logs/spiec.slurm-%j_%N.out
#SBATCH -e grid_logs/spiec.slurm-%j_%N.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user <vihou@ucsd.edu> 

### load module and dependencies cleanly after purge
module purge
module load slurm shared  cpu/0.17.3  gcc/10.2.0-2ml3m2l
module load r
# Change to the working directory
export R_LIBS_USER=~/R/x86_64-pc-linux-gnu-library/4.1
cd /tscc/projects/ps-allenlab/projdata/vihou/Ecohab22/ASV_data/

# Execute your R script
Rscript spieceasi_analysis.R

