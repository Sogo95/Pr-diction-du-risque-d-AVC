Prédiction du risque d’avoir un AVC avec le modèle de Random Forest

Selon l’Organisation Mondiale de la Santé (OMS) Chaque année, 15 millions de personnes font un accident vasculaire cérébral (AVC) : 5 millions d'entre elles meurent et 5 millions souffrent d'une incapacité permanente, ce qui représente un poids pour la famille et la communauté. La suspicion du diagnostic d'AVC repose en règle générale sur la clinique avec deux éléments clés à savoir un déficit neurologique focalisé et une apparition brutale. L'examen neurologique confirme le déficit, en précise la topographie et permet d'évoquer le territoire atteint. C’est dans le souci d’éviter les erreurs de diagnostiques, de réduire la charge du travail des cliniciens et de minimiser les coûts supportés par les patients que nous proposons un modèle de Machine Learning qui détectera le risque pour un patient donné d’avoir un AVC sur les patients positif en fonction de certaines caractéristiques.

 Nous avons utilisé les données de Kaggle pour traiter le sujet et sont disponibles sur https://www.kaggle.com/datasets/prosperchuks/health-dataset/data


Méthodologie : 
•	Nous avons procédé à la connaissance des données par leur exploration. 
•	Nous avons traité les variables manquantes, encoder et normalisé certaines de nos variables explicatives. 
•	Nous avons observé la distribution de la variable d’intérêt (risque d’avoir un AVC) et avons fait ressortir les variables qui étaient corrélé au risque d’AVC ainsi que celles ayant un effet sur cette même variable. 
•	Les variables asymétriques ont été également détecté et corriger
•	Nous avons procédé à la construction du modèle tout en divisant notre base de données en ensemble d’entrainement (70%) et de test (30%). 
•	Le Random Forest a été utilisé et une prédiction sur l’ensemble des données test a été effectué.
