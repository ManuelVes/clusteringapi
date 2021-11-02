from pydantic import BaseModel,conlist
import joblib

classes = {
    0: 'clust1',
    1: 'clust2',
    2: 'clust3'
}

class Feature_type(BaseModel):
    #description: Optional[str] = None questo è un campo opzionale
    feature1: float = 10.6 # 10.6 default value
    feature2: float = 3.16 # 3.16 default value
    feature3: float = 2.4  # 2.4  default value

    #name: constr(min_length=1)  # 1
    #scores: conlist(int, min_items=1) 



model = joblib.load("model_clu.pkl")
#model = joblib.load("model_api1_.pkl")