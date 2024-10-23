#!/bin/bash 
#SBATCH --time=16:00:00
#SBATCH --nodes=2
#SBATCH -o /dev/null
#SBATCH --ntasks-per-node=32
#SBATCH --account=owner-guest
#SBATCH --partition=notchpeak-guest
#SBATCH --mem=180G  # Added line to request 128 GB of total memory

# Editable parameters
BASE="2D"
ORDER="l"
REF_SUBSTRATE="1"
REF_IND="0"
SUFFIX=""

# Construct the full NAME
NAME="${BASE}_${ORDER}${REF_SUBSTRATE}${SUFFIX}"

# Construct DATADIR and SCRATCH using the updated NAME
DATADIR="/uufs/chpc.utah.edu/common/home/u1015301/moose/${BASE}_${ORDER}${REF_SUBSTRATE}"
SCRATCH="/scratch/general/vast"

# Construct the input file name
INPUT_FILE="ind_${BASE}_${ORDER}.i"

# Load necessary modules (adjust as needed)
module purge
module load moose

cd $DATADIR

# Run your MOOSE application
mpiexec -np $SLURM_NTASKS combined-opt -i $INPUT_FILE \
    -input-params ref=${REF_SUBSTRATE} refi=${REF_IND} E=139 K=7.26 n=0.195 hm=0.226 \
    > $DATADIR/$NAME.$SLURM_JOB_ID.out 2>&1
