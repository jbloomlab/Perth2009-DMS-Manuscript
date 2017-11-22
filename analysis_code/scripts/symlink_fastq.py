"""Symbolically link to FASTQ files."""


import os
import glob


origpath = '/shared/ngs/illumina/jmlee34/170310_D00300_0393_AHHFMLBCXY/Unaligned/Project_jmlee34/'

fastqdir = './fastq/'
if not os.path.isdir(fastqdir):
    os.mkdir(fastqdir)

samples = ['WTplasmid', 'WTvirus'] + \
          ['mutvirus{0}'.format(r) for r in range(1, 3)] +\
          ['Plasmidlib{0}'.format(r) for r in range(1, 4)] + \
          ['mutvirus3-{0}'.format(tr) for tr in range(1, 3)]
        

for sample in samples:
    print("\nAnalyzing sample {0}".format(sample))
    dirs = [d for d in os.listdir(origpath) if sample in d]
    print("Found {0} directories.".format(len(dirs)))
    ifile = 1
    for d in dirs:
        fulld = "{0}/{1}".format(origpath, d)
        for f in glob.glob("{0}/{1}*R1_00*.fastq.gz".format(fulld, sample)):
            newf = "{0}/{1}_R1_file{2}.fastq.gz".format(fastqdir, sample, ifile)
            print("File {0} is {1} -- linking to {2}".format(ifile, f, newf))
            ifile += 1
            if not os.path.isfile(newf):
                os.symlink(f, newf)
            f2 = f.replace('_R1', '_R2')
            assert os.path.isfile(f2)
            newf2 = newf.replace('_R1', '_R2')
            if not os.path.isfile(newf2):
                os.symlink(f2, newf2)