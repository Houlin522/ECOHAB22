#!/bin/bash
#SBATCH -p condo
#SBATCH -q condo
#SBATCH -A sio141
#SBATCH -N 1 -n 1 -c 16
#SBATCH --mem=16gb
#SBATCH -J blast
#SBATCH -t 08:00:00
#SBATCH -o grid_logs/blastn.slurm-%j_%N.out
#SBATCH -e grid_logs/blastn.slurm-%j_%N.err
#SBATCH --mail-type END,FAIL

#this script to determine which MATOU phaeocystaceae sequences have a hit
#in my Phaall biogeo library

### load fastp module and dependencies cleanly after purge
module purge
module load cpu slurm gcc
#export MODULEPATH=/projects/builder-group/jpg/modulefiles/applications:$MODULEPATH
export OMP_NUM_THREADS=$SLURM_JOB_CPUS_PER_NODE
export PATH=$PATH:/tscc/projects/ps-allenlab/projdata/common/bin
export PATH=$PATH:/tscc/projects/ps-allenlab/projdata/zfussy/scripts

#set TMPDIR to scratch on execution host
export TMPDIR=/scratch/$USER/job_$SLURM_JOB_ID

### Change to Run directory
#BLASTDIR="/tscc/lustre/ddn/scratch/zfussy/db/"
#RESULTS_DIR=/tscc/lustre/ddn/scratch/zfussy/trees

### Set input here
DATETIME=`date '+Date: %F Time: %T'`;
echo "Time: diamond_blastp analysis STARTED for assembly.orf: ${DATETIME}";

QUERY="/Users/houlin/Desktop/Ecohab/Ecohab22/metatranscriptoms/sequence_data/dabs_aa_queries.fasta"
PREFIX=${QUERY%.*}

FASTA="/Users/houlin/Desktop/Ecohab/Ecohab22/metatranscriptoms/sequence_data/assembly.orf.faa"
DB="/Users/houlin/Desktop/Ecohab/Ecohab22/metatranscriptoms/sequence_data"
diamond makedb --in $FASTA --db $DB #--threads $OMP_NUM_THREADS
diamond blastp --log --sensitive \
	--query $QUERY \
	--db $DB \
	--max-target-seqs 10000 --max-hsps 1 --evalue 1e-03 \
	-f 6 qseqid sseqid evalue ppos stitle full_sseq \
	--out $PREFIX.metaT.dmnd.tsv

python diamondparse_server.py --skip_dupes --pool False -q $QUERY --results $PREFIX.metaT.dmnd.tsv --suffix metaT

exit 0

DB="/tscc/projects/ps-allenlab/projdata/common/db/diamond/nr"
diamond blastp --threads $OMP_NUM_THREADS --log --sensitive \
	--query $QUERY \
	--db $DB \
	--max-target-seqs 10000 --max-hsps 1 --evalue 1e-03 \
	-f 6 qseqid sseqid evalue ppos stitle full_sseq \
	--out $PREFIX.nr_sens.dmnd.tsv

diamondparse_server.py --skip_queries --skip_dupes --pool False -q $QUERY --results $PREFIX.nr_sens.dmnd.tsv --suffix NR

DB="/tscc/projects/ps-allenlab/projdata/common/db/eukprot/eukprot3"
diamond blastp --threads $OMP_NUM_THREADS --log --sensitive \
	--query $QUERY \
	--db $DB \
	--max-target-seqs 10 --max-hsps 1 --evalue 1e-03 \
	-f 6 qseqid sseqid evalue ppos stitle full_sseq \
	--out $PREFIX.ep3_sens.dmnd.tsv

diamondparse_server.py --skip_queries --skip_dupes --pool True -q $QUERY --results $PREFIX.ep3_sens.dmnd.tsv --suffix EP3

DB="/tscc/projects/ps-allenlab/projdata/common/db/eggnog5/eg5"
diamond blastp --threads $OMP_NUM_THREADS --log --sensitive \
	--query $QUERY \
	--db $DB \
	--max-target-seqs 1000 --max-hsps 1 --evalue 1e-03 \
	-f 6 qseqid sseqid evalue ppos stitle full_sseq \
	--out $PREFIX.eg5_sens.dmnd.tsv

diamondparse_server.py --skip_queries --skip_dupes --pool True -q $QUERY --results $PREFIX.eg5_sens.dmnd.tsv --suffix EG5

DATETIME=`date '+Date: %F Time: %T'`;
echo "Time: diamond_blastp analysis FINISHED for query.fasta: ${DATETIME}";
