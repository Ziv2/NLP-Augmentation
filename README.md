# NLP-Augmentation


At this git you can find: 
# A tool to generate synthetic text in order to augment training NLP models. 
This tool uses WordTune app to create a synthetic text.

WordTune is designed to provide a wide variety of wordings. 
WordTune is not strict to preserve the exect originl semantic representations.

Nevertheless, as part of a chat bot progect, I choose this app because I think it is truly enrich the spatial blocks which hold similar sematic representations, relative to the client's raw questions.

This approach emphasizes quantity and enrichment over maintaining exact semantics. 
In addition, you can train your model with this augmentation, find the incorrectly classified sentences, correct their classification, and retrain it with random train-validation splits or cross-validations. 

<img width="279" alt="Ilustrated sentence semantic representation for few bolcks per class" src="https://user-images.githubusercontent.com/41025885/130994619-60d7be77-3147-437f-8fca-675fd21e5170.PNG">

At this picture I illustrated 3 blocks for each class (red and blue). 
This illustrates the semantic representations enrichment (per class) which this tool aimed to provide.

## ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) Note, if you want to use this tool, you should ask for a permission: 
#    sales@wordtune.com

## Purpose: 
By using this tool, our model precision increased from ~74% to ~95%. 
We had 70 classes, including adjecent classes with almost identical semantics. 

## Inputs: 
CSV file with the following 4 rows:

| N | Topic | Intent | Sample |
| ------ | ------ | ------ | ------ |
| class index | name of the general topic | Class name per question | original questions |


## Output:  
- A CSV file with the original + synthetic questions. 
- Each question generates 10 synthetic questions. 
- Duplicate questions are removed.
- I repeated this procedure a few times. Got 16,000 questions out of 220 original questions. 


## Few more notes: 
- It takes ~1 sec per query. 
- The script will fail if your internet connection will be shut down.
- In case you are using this script, adding break points might be helpful. 
  With adding break points, the successful synthetic questions will still be available even if the script fails midway through the run.

Thanks for reading, 

Ziv

## ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) Note, if you want to use this tool, you should ask for a permission: 
##    sales@wordtune.com
