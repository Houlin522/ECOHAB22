import pickle
import os
os.chdir('/Users/houlin/Desktop/Ecohab/Ecohab22/metatranscriptoms')

pfam_functional_gene_dict={
'cell_death':['Actin', 'Papain family cysteine protease', 'Tubulin C-terminal domain', 
    'Tubulin/FtsZ family, GTPase domain', 'Eukaryotic aspartyl protease', 'Cytochrome c',
    'NAC domain', 'Cathepsin propeptide inhibitor domain (I29)',  'Hsp90 protein',
    'Caspase domain','SAC3/GANP family','Ribosomal protein L36e'],

'cell_cycle':['Domain of unknown function (DUF202)','Skp1 family, tetramerisation domain',
    'Calcineurin-like phosphoesterase','Protein kinase domain',
    'Serine-threonine protein phosphatase N-terminal domain',
    'Protein tyrosine and serine/threonine kinase','FYVE zinc finger'],
# CDK inhibitors 
'cyclin':['Cyclin','Cyclin C-terminal domain','Cyclin D1 binding domain',
'Cyclin M transmembrane N-terminal domain','Cyclin, C-terminal domain',
'Cyclin, N-terminal domain','Cyclin-dependent kinase inhibitor 3 (CDKN3)',
'Cyclin-dependent kinase regulatory subunit'],
    
'glycolysis':['Glyceraldehyde 3-phosphate dehydrogenase, C-terminal domain', 'Glyceraldehyde 3-phosphate dehydrogenase, NAD binding domain', 
    'Phosphoglycerate kinase', 'Fructose-bisphosphate aldolase class-II', 'Triosephosphate isomerase', 'Enolase, C-terminal TIM barrel domain', 
    'Phosphofructokinase', 'Pyruvate kinase, barrel domain', 
    'Enolase, N-terminal domain', 'Histidine phosphatase superfamily (branch 1)'],

'b12':['Vitamin B12 dependent methionine synthase, activation domain','S-adenosylmethionine synthetase, C-terminal domain',
'S-adenosylmethionine synthetase, N-terminal domain','S-adenosylmethionine synthetase, central domain',
'Cobalamin-independent synthase, Catalytic domain', 'Cobalamin-independent synthase, N-terminal domain'],

'chloroplast':['Copper binding proteins, plastocyanin/azurin family',
                'Plastocyanin-like domain','Vitamin B12 dependent methionine synthase',
                'activation domain'],

'photosynthesis':['Chlorophyll A-B binding protein','Photosynthetic reaction centre protein',
'Oxidoreductase NAD-binding domain','Manganese-stabilising protein / photosystem II polypeptide',
'Photosystem I psaA/psaB protein','Photosystem II protein','Photosystem II 12 kDa extrinsic protein (PsbU)',
'ATP synthase','Cytochrome C oxidase, cbb3-type, subunit III',
'Copper binding proteins, plastocyanin/azurin family','Cytochrome b/b6/petB'],

#Allen et.ql ,Gao et.al, 2021
'iron_uptake':['Silicon transporter',
    'Nitrite/Sulfite reductase ferredoxin-like half domain',
    'NADH-ubiquinone oxidoreductase-F iron-sulfur binding region',
    'Ferric uptake regulator family','Multicopper oxidase','Transferrin',
    'Ferrous iron transport protein B','Ferric reductase NAD binding domain',
    'Ferric reductase like transmembrane component'],

# Coale et.al, 2019
'low_iron':['ISIP1', 'ISIP2A', 'ISIP2B','Flavodoxin','Fructose-bisphosphate aldolase class-I',
        'Copper amine oxidase, N3 domain','Copper amine oxidase, enzyme domain',
        'Low iron-inducible periplasmic protein'],
'nitrogen_gene':['GSIIA', 'GSIIB', 'GSIIC', 'GSIII', 'NR', 'NRT2', 'NirB', 'NirG'],
#, diatom doesn't have these
'dab':['dabA','dabC','dabD'],

# Allen et.al, 2011
'urea_cycle':['Ornithine cyclodeaminase/mu-crystallin family','Ornithine decarboxylase antizyme',
            'Aspartate/ornithine carbamoyltransferase, carbamoyl-P binding domain',
            'Arginase family','Argininosuccinate lyase C-terminal',
            'Urease beta subunit', 'Urease alpha-subunit, N-terminal domain', 'UreD urease accessory protein', 
            'Urease, gamma subunit'],


'glycerolipid':['Aldo/keto reductase family',
'Lipase (class 3)',
'Acyltransferase',
'Serine aminopeptidase, S33',
'Glycosyl transferase family group 2',
'Diacylglycerol acyltransferase',
'NAD dependent epimerase/dehydratase family',
'Alpha galactosidase A',
'Legume lectin domain',
'Alpha galactosidase C-terminal beta sandwich domain'],

'glycerolipid_dia':['Serine aminopeptidase, S33',
'Aldo/keto reductase family',
'Zinc-binding dehydrogenase',
'MBOAT, membrane-bound O-acyltransferase family',
'NAD dependent epimerase/dehydratase family',
'Lipase (class 3)',
'WS/DGAT C-terminal domain',
'Acyltransferase',
'Diacylglycerol acyltransferase',
'Patatin-like phospholipase'],

#glutamine synthetase, glutamate synthase (GOGAT)
#Remmer et.al, 2018, 
'ammoninum_assimilation':['Glutamine synthetase type III N terminal', 'Glutamine synthetase, beta-Grasp domain', 
                        'Glutamine synthetase C-terminal domain','Ammoninum transporter',
                        'Glutamate/Leucine/Phenylalanine/Valine dehydrogenase','NAD-specific glutamate dehydrogenase',
                        'Glutamate synthase central domain','Conserved region in glutamate synthase'],

'calvin_cycle':['Ribulose bisphosphate carboxylase large chain, catalytic domain',
'Glyceraldehyde 3-phosphate dehydrogenase, C-terminal domain',
'Glyceraldehyde 3-phosphate dehydrogenase, NAD binding domain',
'Phosphoglycerate kinase','Fructose-bisphosphate aldolase class-II','Triosephosphate isomerase',
'Phosphoribulokinase / Uridine kinase family','Fructose-1-6-bisphosphatase, C-terminal domain',]
}
        
        
with open("pfam_genename_dict.pkl", "wb") as pickle_file:
    pickle.dump(pfam_functional_gene_dict, pickle_file)
    print('save pfam_genename_dict.pkl to path')

'''
Kegg pathway description
'''    
ko_functional_gene_dict={
'cell_death':[],

'cell_cycle':[],

'cyclin':['G1/S-specific cyclin CLN2',
 'G1/S-specific cyclin CLN3',
 'G1/S-specific cyclin-D1',
 'G1/S-specific cyclin-D1,amyloid beta A4 protein,nucleolin',
 'G1/S-specific cyclin-D1,protein DEK',
 'G1/S-specific cyclin-D2',
 'G1/S-specific cyclin-D3',
 'G1/S-specific cyclin-E1',
 'G2/mitotic-specific cyclin 2',
 'G2/mitotic-specific cyclin 3/4',
 'G2/mitotic-specific cyclin 3/4,bestrophin-3',
 'G2/mitotic-specific cyclin 3/4,potassium intermediate/small conductance calcium-activated channel subfamily N member 1',
 'G2/mitotic-specific cyclin 3/4,von Willebrand factor C and EGF domain-containing protein',
 'G2/mitotic-specific cyclin-B, other',
 'G2/mitotic-specific cyclin-B, other,chromodomain-helicase-DNA-binding protein 1 [EC:5.6.2.-]',
 'G2/mitotic-specific cyclin-B1',
 'G2/mitotic-specific cyclin-B1,trehalose monomycolate/heme transporter,solute carrier family 39 (zinc transporter), member 6',
 'G2/mitotic-specific cyclin-B2',
 'G2/mitotic-specific cyclin-B3'],
    
'glycolysis':[],

'b12':[],

'chloroplast':[],

'photosynthesis':[],

'iron_uptake':[],

'low_iron':['ISIP1', 'ISIP2A', 'ISIP2B'],

'nitrogen_gene':['GSIIA', 'GSIIB', 'GSIIC', 'GSIII', 'NR', 'NRT2', 'NirB', 'NirG'],

'dab':['dabA','dabC','dabD'],

'urea_cycle':[],

'glycerolipid':[],

'glycerolipid_dia':[],

#glutamine synthetase, glutamate synthase (GOGAT)
#Remmer et.al, 2018, 
'ammoninum_assimilation':[],

'calvin_cycle':[]
}
        

with open("ko_genename_dict.pkl", "wb") as pickle_file:
    pickle.dump(ko_functional_gene_dict, pickle_file)
    print('save ko_genename_dict.pkl to path')