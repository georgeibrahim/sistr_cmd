import os

# cgMLST330 distance threshold for refining overall serovar prediction
CGMLST_DISTANCE_THRESHOLD = 0.1

base_dir = os.path.join(os.path.dirname(__file__), '..', '..')
here = lambda x: os.path.abspath(os.path.join(base_dir, x))

SEROVAR_TABLE_PATH = here('data/Salmonella-serotype_serogroup_antigen_table-WHO_2007.csv')

# MLST_TO_SEROVAR_MATRIX_PATH = os.path.abspath('data/MLST_to_serovar_matrix.csv')

WZX_FASTA_PATH = here('data/antigens/wzx.fasta')
WZY_FASTA_PATH = here('data/antigens/wzy.fasta')

FLIC_FASTA_PATH = here('data/antigens/fliC.fasta')
FLJB_FASTA_PATH = here('data/antigens/fljB.fasta')

SEROGROUP_SIMILARITY_GROUPS = [
    ['E1', 'E4'],
    ['A', 'D1', 'D2'],
    ['C1', 'F'],
    ['S', 'O62']
]

# Determined the following H1 antigen similarity groups based on a
# phylogenetic tree of fliC allele sequences.
# The cluster of g antigen sequences was very convoluted hence the complex
# groupings in the list of lists below.
H1_FLIC_SIMILARITY_GROUPS = [
    ['r',
     'r,[i]',
     'r,i', ],
    ['l,[z13],[z28]',
     'l,[z13],z28',
     'l,z13',
     'l,z13,[z28]',
     'l,z13,z28',
     'l,z28', ],
    ['(g),m,[s],t',
     '(g),m,[s],t',
     'g,(m),[s],t',
     'm,t',
     'm,p,t,[u]',
     '[g],m,t',
     'g,m,t',
     'g,m,[t]',
     'g,m,[s],t',
     'g,m,[s],[t]',
     'g,[m],[s],[t]',
     'g,[m],s,t',
     'g,[m],t',
     'g,m,[s],[t]', ],
    ['f,g,m,t',
     'g,m,t',
     'g,m,[t]',
     'g,m,[s],t',
     '[g],m,t',
     'g,[m],t',
     'g,m,[s],t',
     'g,m,[s],[t]',
     'g,[m],[s],[t]', ],
    ['g,m,s,t',
     'g,[m],[s],[t]',
     'g,[m],[s],t',
     'g,[m],s,t',
     'g,m,[s],[t]', ],
    ['g,(t)',
     'g,[m],[s],[t]',
     'g,[m],[s],t',
     'g,[m],s,t',
     'g,m,[s],[t]',
     'g,[m],t', ],
    ['g,m',
     'g,m,[p],s',
     'g,m,[s]',
     'g,m,[t]',
     'g,[m],[s],[t]',
     'g,[m],[s],t',
     'g,m,[s],[t]',
     'g,m,q',
     'g,m,s',
     'g,m,s',
     'g,p',
     'g,p,s',
     'g,p,u',
     'g,q',
     'g,s,q', ],
    ['[f],g,[t]',
     'f,g',
     'f,g,[s]',
     'f,g,s',
     'f,g,[t]',
     '[f],g,[t]',
     'f,g,t',
     'g,t', ],
    ['[f],g,[t]',
     'f,g,[s]',
     'f,g,[t]',
     'f,g,s', ],
    ['[g,t]',
     'g,[s],t',
     'g,s,[t]',
     'g,s,t'
     'g,t', ],
    ['z36,[z38]',
     'z36,z38', ],
    ['z36,[z38]',
     'z36', ]
]

H2_FLJB_SIMILARITY_GROUPS = [
    ['1,5',
     '1,[2],5',
     '1,5,[7]',
     '[1,5]', ],
    ['1,6',
     '1,6,[7]', ],
    ['1,7',
     '1,[2],7',
     '1,[5],7', ],
    ['e,n,[x],z15',
     'e,n,z15', ],
    ['e,n,x',
     'e,n,x,[z15]', ]
]
