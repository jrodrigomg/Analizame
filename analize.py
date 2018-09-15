
#libreries
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions, SentimentOptions, EmotionOptions



def analizarTexto(USER):
  #Open the file with the name of the user.
  resultfile = open("result_"+USER+".json", "w+")

  targets =[
      'vida', 'Guatemala', 'amor', 'sexo', 'politico',
      'poliltica','Yo', 'sonrisa', 'pais','novio','novia',
      'enojo', 'hermano', 'hermana','mama','papa','familia',
      'deporte', 'relacion'
    ]
  #Get the configuration file
  with open('config.json', 'r') as f:
      config = json.load(f)

  #reading the data file
  datafile = open("data_" +USER+".txt","r")
  data = datafile.read()
  
  #print the data... remove this..
  print (data)

  #Authentication
  natural_language_understanding = NaturalLanguageUnderstandingV1(
      version=config["version"],
      username=config["username"],
      password=config["password"]
  )

  response = natural_language_understanding.analyze(
    text=data,
    features=Features(
      entities=EntitiesOptions(
        emotion=True,
        sentiment=True,
        limit=2),
      keywords=KeywordsOptions(
        emotion=True,
        sentiment=True,
        limit=2),
      sentiment=SentimentOptions(
        targets=targets
      )
      #Doesn't support spanish language yet
      # ,
      # emotion=EmotionOptions(
      #   targets=targets
      # )
    )
  )

  result = str(response)
  print (result)
  resultfile.write(result + "")
  resultfile.close()
  f.close()
  datafile.close()
  #print(json.dumps(response, indent=2))

