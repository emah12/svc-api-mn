from fastapi import FastAPI
import pandas as pd
import uvicorn

df = pd.read_csv('./data/services2019.csv')

app = FastAPI()

@app.get("/")
def home():
    return {"This is a API service for MN health care services details."}

@app.get("/preview")
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result
    
@app.get("/svc/{value}")
def svccode(value):
    print("value: ", value)
    filtered = df[df["svc_code"] == value]
    if len(filtered) <= 0:
        return {"There is nothing here"}
    else: 
        return filtered.to_json(orient="records")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)