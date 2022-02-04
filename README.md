# DeepNeo - identification of immunogenic neoepitopes


DeepNeo is a tool for predicting the immunogenicity of peptide-MHC pairs.

Installation : 
DeepNeo uses specific version of Theano(0.9) and requires GPU.

1) Recommended : Copy working environment to your miniconda/anaconda folder

- wget http://143.248.31.34/~omics/data/DeepNeo/deepneo_environment.tar.gz
- tar -zxvf deepneo_environment.tar.gz
- cp -r deepneo_environment /home/YOUR_NAME/miniconda2/envs/
- conda activate deepneo_environment

2) You can obtain working environment by installing all the packages provided in the DeepNeo_conda_environment.

conda env create -f DeepNeo_conda_environment.yml -n YOUR_ENV_NAME
conda activate YOUR_ENV_NAME


Usage:
DeepNeo is a two-part program : 
(1) predicting peptide-MHC binding (mhc)
(2) predicting TCR reactivity (tcr) of the pMHC pair.
In each part, predictions can be made with following command lines.

python make_dataset.py INPUT.dat MHC_CLASS INPUT.dat.pkl.gz
python run_cnn.py MHC_CLASS PREDICTION_TYPE INPUT.dat.pkl.gz OUTPUT.txt

For example:

python make_dataset.py class1_input.dat class1 class1_input.dat.pkl.gz

python run_cnn.py class1 mhc class1_input.dat.pkl.gz class1_mhcbinding_output.txt 

python run_cnn.py class1 tcr class1_input.dat.pkl.gz class1_immunogenicity_output.txt 

Input file:
Three column tab-delimited file containing HLA allele, peptide sequence, and 0.

For example:

HLA-A-0201	QISLFWKNL	0

HLA-B-0702	QISLFWKNL	0

Output file:

Three column tab-delimited file containing HLA allele, peptide sequence, and predicted binding(mhc)/immunogenicity(tcr) value.

For example:

HLA-A-0201	QISLFWKNL	0.3547

HLA-B-0702	QISLFWKNL	0.3845
