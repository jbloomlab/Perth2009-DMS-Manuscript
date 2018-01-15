# Perth2009-DMS-Manuscript Analysis Code

## Overview

This is the analysis code directory for the deep mutational scanning of the A/Perth/16/2009(H3N2) HA manuscript repository.
Study by Juhye Lee, John Huddleston, Mike Doud, Katie Hooper, and Jesse Bloom in the Bloom lab.

## Organization

This directory is organized into the following subdirectories:

* [./data/](./data/) contains the input files necessary to run the analyses. In this directory are the following:

  * `H1toH3_renumber.csv`: file to convert from H1 sequential numbering to H3 numbering
  * `H3_human_alignment.fa`: file of subsampled human seasonal H3N2 HA sequences for running `phydms`
  * `H3renumbering_scheme.csv`: file to convert from H3 sequential numbering to H3 numbering
  * `Perth09_HA_reference.fa`: the reference sequence for the wildtype Perth/2009 HA
  * `Perth2009_WSN_aa_align.fa`: the alignment file for the Perth/2009 H3 and WSN/1933 H1 using mafft
  * `Perth2009_compareprefs_renumber.csv`: file to renumber the Perth/2009 H3 preferences to allow for comparing the preferences between H3 and H1
  * `WSN_HA_reference.fa`: the reference sequence for the wildtype WSN/1933 HA
  * `WSN_avgprefs_rescaled.csv`: the across-replicate averaged and re-scaled preferences for the WSN/1933 HA
  * `WSN_compareprefs_renumber.csv`: file to renumber the WSN/1933 H1 preferences to allow for comparing the preferences between H1 and H3
  * `abs_conserved_sites.txt`: list of sites that are absolutely conserved across all 18 HA subtypes
  * `clade_specific_sites.txt`: list of sites that have clade-specific identities in the clade containing H1 and the clade containing H3
  * `flu_h3n2_1968_6v_tree.json.gz`: tree build of human H3N2 influenza virus HA sequences using `fauna` and `augur` and in `json` file format
  * `wolf_epitope_sites.csv`: list of Wolf epitope sites in H3 numbering
  
### Organization of `Perth2009_DMS_analysis.ipynb`

The notebook is split into three main sections:

* Section 1: Infer H3 site-specific amino-acid preferences
* Section 2: Investigate lineage-specific mutational effects from H3N2 evolution
* Section 3: Compare the preferences between the HA homologs